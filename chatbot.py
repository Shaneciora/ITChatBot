from chatterbot import ChatBot


# Create a new instance of a ChatBot

chatbot = ChatBot(
    'Dave',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///db.sqlite3'
)

