from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
    return """<h1 style="color:#000;font-family:system-ui;font-weight:300;font-size:28pt;">Nikity Prime</h1> <h2 
    style="font-family:sans-serif;color:gray;font-weight:100;">Hello! I'm Nikity Prime and I'm a discord bot</h2> 
    <br><a href="https://github.com/saminsakur/nikity_prime" 
    style="text-decoration:none;color:#27AEEA;font-family:system-ui;">Github</a> """


def run():
    app.run(host='127.0.0.1', port=8080)


def keep_running():
    t = Thread(target=run)
    t.start()
