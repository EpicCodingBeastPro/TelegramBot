import telebot

TELEGRAM_API_TOKEN = '[YOUR BOT API TOKEN HERE]' #The token of bot created using BotFather
bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

#Basic Hi command
@bot.message_handler(commands=['hi', 'hello']) # you can replace Hi and hello with whatever commands you want
def check_command(message):
        bot.send_message(message.chat.id, "Hey there! How are you doing")#This gives back the reply to your corresponding message
