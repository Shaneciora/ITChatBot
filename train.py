from chatbot import chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

trainer = ChatterBotCorpusTrainer(chatbot)
trainer2 = ListTrainer(chatbot)

def train_bot():
    '''
    trainer.train(
        "chatterbot.corpus.english.greetings",
        "chatterbot.corpus.english.conversations"

    )'''

    trainer2.train([
        "I need some help.",
        "What do you need help with? I can offer help regarding: <br>| <strong>Account Information</strong> |<br>| <strong>Forgot Password</strong> |<br>| <strong>Server Status</strong> |<br>| <strong>New Support Request</strong> |<br>| <strong>Current Support Tickets</strong> |",
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

    trainer2.train([
        "Hey",
        "Hi",
        "Sup",
        "Nm hbu",
        "test",
    ])

    trainer2.train([
        "Hello Dave""Hey Dave""Hi Dave",
        "Greetings, human",
    ])


