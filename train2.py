from chatbot import chatbot
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(chatbot)

trainer.train([
    "I need some help.",
    "What do you need help with? I can offer help regarding:\nAccount Information\nForgot Password\nSystem Status",
])
