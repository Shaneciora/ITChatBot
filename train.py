from chatbot import chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

trainer = ChatterBotCorpusTrainer(chatbot)
trainer2 = ListTrainer(chatbot)

def train_bot():
    trainer.train(
        "chatterbot.corpus.english.greetings",
        "chatterbot.corpus.english.conversations"

    )

    trainer2.train([
        "I need some help.",
        "What do you need help with? I can offer help regarding: Account Information, Forgot Password, Server Status, New Support Request, Current Support Tickets",
        "Account Information",
        "Your account information:",
    ])

    trainer2.train([
        "Forgot Password",
        "Please enter your account email and we will send you a verification code to reset your password.",
    ])

    trainer2.train([
        "Server Status",
        "The server is online, for more information, type 'Detailed Information'",
        "Detailed Information",
        "display admin log in and server information",
    ])

    trainer2.train([
        "New Support Request",
        "Please use this webpage to file a new support ticket",
    ])

    trainer2.train([
        "Current Support Tickets",
        "list current account tickets",
    ])
