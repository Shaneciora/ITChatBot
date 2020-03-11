from flask import Flask, render_template, request
from chatbot import chatbot
from train import train_bot

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    train_bot()
    app.run()
