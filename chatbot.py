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


print('[Dave]: Hello, I am Dave. How can I help you?')

bot_name = '[Dave]: '
# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input("[User]: ")

        bot_response = chatbot.get_response(user_input)

        print (bot_name + str(bot_response))

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
