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
        "What do you need help with? I can offer help regarding: <br>| <strong>Account Information</strong> |<br>| <strong>Forgot Password</strong> |<br>| <strong>Server Status</strong> |<br>| <strong>New Support Request</strong> |<br>| <strong>Support Tickets</strong> |",
        "Account Information",
        "Your account information:<br>Username: admin<br>Email: admin@mac.com<br>Account Type: ADMINISTRATOR<br><strong>Manage Information</strong>",
    ])

    trainer2.train([
        "Forgot Password",
        "Please reply with your account email and we will send you a verification code to reset your password.",
    ])

    trainer2.train([
        "Server Status",
        "Your server (Server 1) is online, for more information, type 'List Servers'",
    ])

    trainer2.train([
        "List Servers",
        "User: admin <br>Pass: ***** <br><strong>Server 1</strong> | Status: Online | Ping: 86 |<br><strong>Server 2</strong> | Status: Online | Ping: 130 |<br><strong>TEST Server</strong> | Status: Offline | Ping: N/A |",
    ])

    trainer2.train([
        "New Support Request",
        "Follow this link to create a new support request: www.company.com/newsupportticket",
    ])

    trainer2.train([
        "Support Tickets",
        "Here is a list of your support tickets:<br>325678 | <strong>I need to change my email address</strong> | Status: Unresolved <br>329765 | <strong>No Server 2 access</strong> | Status: Resolved",
    ])

#lowercase options
    trainer2.train([
        "i need some help",
        "What do you need help with? I can offer help regarding: <br>| <strong>Account Information</strong> |<br>| <strong>Forgot Password</strong> |<br>| <strong>Server Status</strong> |<br>| <strong>New Support Request</strong> |<br>| <strong>Support Tickets</strong> |",
        "account information",
        "Your account information:<br>Username: admin<br>Email: admin@mac.com<br>Account Type: ADMINISTRATOR<br><strong>Manage Information</strong>",
    ])

    trainer2.train([
        "forgot password",
        "Please reply with your account email and we will send you a verification code to reset your password.",
    ])

    trainer2.train([
        "server status",
        "Your server (Server 1) is online, for more information, type 'List Servers'",
    ])

    trainer2.train([
        "list servers",
        "User: admin <br>Pass: ***** <br><strong>Server 1</strong> | Status: Online | Ping: 86 |<br><strong>Server 2</strong> | Status: Online | Ping: 130 |<br><strong>TEST Server</strong> | Status: Offline | Ping: N/A |",
    ])

    trainer2.train([
        "new support request",
        "Follow this link to create a new support request: www.company.com/newsupportticket",
    ])

    trainer2.train([
        "support tickets",
        "Here is a list of your support tickets:<br>325678 | <strong>I need to change my email address</strong> | Status: Unresolved <br>329765 | <strong>No Server 2 access</strong> | Status: Resolved",
    ])
