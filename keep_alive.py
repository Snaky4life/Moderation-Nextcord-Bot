from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "I wonder how much storage these webpages take up and I wonder if a very precise and weirdly worded Google search could bring this Replit keep_alive page up."

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()

#keep_alive()	