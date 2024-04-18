import time, os

def run():
    while True:
        os.system("rm -rf /app/users/*")

        os.system("rm -rf /app/notes/*")
        os.system("rm -rf /app/user_notes/*")

        time.sleep(60 * 10)
        