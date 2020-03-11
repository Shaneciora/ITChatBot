from chatbot import chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

trainer = ChatterBotCorpusTrainer(chatbot)
trainer2 = ListTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"

)

trainer2.train([
    "I need some help.",
    "What do you need help with? I can offer help regarding: \n Account Information \n Forgot Password \n System Status",
    "Account Information",
    "Your account information:",
])

trainer2.train([
    "Forgot Password",
    "Please enter your account email and we will send you a verification code to reset your password.",
])

trainer2.train([
    "System Status",
    "The system is operational, for more information, type 'info'",
    "info",
    "<display system information>",
])
