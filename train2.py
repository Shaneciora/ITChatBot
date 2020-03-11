from chatbot import chatbot
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(chatbot)

trainer.train([
    "I need some help.",
    "What do you need help with? I can offer help regarding: \n Account Information \n Forgot Password \n System Status",
    "Account Information",
    "Your account information:",
])

trainer.train([
    "What do you need help with? I can offer help regarding: \n Account Information \n Forgot Password \n System Status",
    "Forgot Password",
    "Please enter your account email and we will send you a verification code to reset your password.",
])
