from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#import os

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

bot=ChatBot('Bot')
trainer=ListTrainer(bot)
#bot.set_trainer(ListTrainer)

#'''for files in os.listdir('C:/Users/Acer/Downloads\chatterbot-corpus-master\chatterbot_corpus\data\english/'):
    #data=open('C:/Users/Acer/Downloads\chatterbot-corpus-master\chatterbot_corpus\data\english/'+files,'r').readlines()
trainer.train(conversation)

while True:
    message=input('you:')
    if message.strip() !='bye':
        reply=bot.get_response(message)
        print('ChatBot:',reply)
    if message.strip()=='bye':
        print('ChatBot:bye')
        break
