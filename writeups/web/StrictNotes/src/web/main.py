from flask import Flask, request, render_template, redirect, url_for, session, make_response
import random, hashlib, time, asyncio, bot, json, os, shlex, threading, cleaner, uuid
from config import config
from utils import nonce
from datetime import datetime

app = Flask(
    'strict',
    static_folder='static',
    template_folder='templates'
)

config = config.Config()

app.secret_key = config.session_key

def simple_csp_render(template):
    nonce_value = nonce.generate(config.nonce_secret)
    resp = make_response(render_template(template, nonce=nonce_value))
    resp.headers['Content-Security-Policy'] = config.csp_config.format(nonce_value)
    return resp

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('add_note'))
    return redirect(url_for("login", error='You are not logged in'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'username' in session:
        return redirect(url_for('add_note'))
    
    if request.method == 'GET':
        return simple_csp_render("register.html")

    username = request.form.get('username')
    password = request.form.get('password')

    if not (password is not None and username is not None and 0 < len(os.path.basename(username)) < 20 and 0 < len(password) < 20):
        return redirect(url_for('register', error='Invalid username or password'))

    if os.path.basename(username) in os.listdir("users"):
        return redirect(url_for('register', error='User already exists'))
    
    with open(f"/app/users/{os.path.basename(username)}", 'w', encoding='utf-8') as file:
        user = dict()
        user['password'] = hashlib.md5(password.encode()).hexdigest()
        user['time_created'] = str(int(time.time()))
        json.dump(user, file, ensure_ascii=False, indent=4)
    session['username'] = username
    dirname = shlex.quote(f"/app/user_notes/{os.path.basename(username)}")
    os.system(f"mkdir {dirname}")

    return redirect(url_for("add_note", message='Register succesfull'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('add_note'))
    
    if request.method == 'GET':
        return simple_csp_render("login.html")

    username = request.form.get('username')
    password = request.form.get('password')

    if not (password is not None and username is not None and len(os.path.basename(username)) < 20 and 0 < len(password) < 20):
        return redirect(url_for('login', error='Invalid username or password'))

    if os.path.basename(username) not in os.listdir("users"):
        return redirect(url_for('login', error='No such user'))

    with open(f"users/{os.path.basename(username)}", 'r') as file:
        info = json.loads(file.read())
        if hashlib.md5(password.encode()).hexdigest() != info['password']:
            return redirect(url_for('login', error='Invalid password'))
    
    session['username'] = os.path.basename(username)
    return redirect(url_for("add_note", message='Login succesfull'))
    
@app.route('/add_note', methods=['GET', 'POST'])
def add_note():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'GET':
        return simple_csp_render("add_note.html")

    title = request.form.get('title')
    message = request.form.get('message')

    if not (title is not None and message is not None and 0 < len(title) < 200 and 0 < len(message) < 200):
        return redirect(url_for('add_note', error='Invalid notes Info'))

    note = dict()

    stamp = int(time.time())
    time_creation = datetime.fromtimestamp(stamp).strftime('%c')
    id = str(uuid.uuid4())
    
    note['id'] = id
    note['title'] = title    
    note['time_creation'] = time_creation

    file = open(f"/app/notes/{id}", 'w+')
    json.dump(note, file, ensure_ascii=False, indent=4)
    file.close()

    note['message'] = message
    note['owner'] = session['username']

    with open(f"/app/user_notes/{session['username']}/{id}", 'w+', encoding='utf-8') as file:
        json.dump(note, file, ensure_ascii=False, indent=4)

    return redirect(url_for("public_notes", id=id))

@app.route('/public-notes', methods=['GET'])
def public_notes():
    notes = []
    if 'id' in request.args:
        if request.args['id'] not in os.listdir("/app/notes"):
            return redirect(url_for("public_notes"))
        notes.append(json.loads(open(f"/app/notes/{os.path.basename(request.args['id'])}").read()))
        nonce_value = nonce.generate(config.nonce_secret)
        resp = make_response(render_template("filtered_notes.html", nonce=nonce_value, safe=['title'], title="Public notes", notes=notes))
        resp.headers['Content-Security-Policy'] = config.csp_config.format(nonce_value)

        return resp

    for filename in os.listdir("/app/notes"):
        notes.append(json.loads(open(f"/app/notes/{filename}").read()))
    
    settings = dict()
    settings['next_handler'] = "public-notes"
    settings['title'] = "Public notes"

    nonce_value = nonce.generate(config.nonce_secret)
    resp = make_response(render_template("notes.html", nonce=nonce_value, notes=notes, settings=settings))
    resp.headers['Content-Security-Policy'] = config.csp_config.format(nonce_value)

    return resp

@app.route('/my')
def my():
    if 'username' not in session:
        return redirect(url_for('login'))
    notes = []
    if 'id' in request.args:
        if request.args['id'] not in os.listdir(f"/app/user_notes/{session['username']}"):
            return redirect(url_for("public_notes"))
        notes.append(json.loads(open(f"/app/user_notes/{session['username']}/{os.path.basename(request.args['id'])}").read()))

        nonce_value = nonce.generate(config.nonce_secret)
        resp = make_response(render_template("filtered_notes.html", nonce=nonce_value, safe=['title'], title="Public notes", notes=notes))
        resp.headers['Content-Security-Policy'] = config.csp_config.format(nonce_value)

        return resp

    for filename in os.listdir(f"/app/user_notes/{session['username']}"):
        notes.append(json.loads(open(f"/app/user_notes/{session['username']}/{filename}").read()))
    
    settings = dict()
    settings['next_handler'] = "my"
    settings['title'] = "My notes"

    nonce_value = nonce.generate(config.nonce_secret)
    resp = make_response(render_template("notes.html", nonce=nonce_value, notes=notes, settings=settings))
    resp.headers['Content-Security-Policy'] = config.csp_config.format(nonce_value)

    return resp


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route('/visit')
async def visit_web():
    if 'id' not in request.args:
        return "nothing to do"
    await bot.visit(request.args['id'])
    return "visited"

if __name__ == '__main__':
    threading.Thread(target=cleaner.run).start()
    app.run(host='0.0.0.0', port=1234, debug=False)
