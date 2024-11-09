import telebot

TELEGRAM_API_TOKEN = '[YOUR BOT API TOKEN HERE]' #The token of bot created using BotFather
bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

group_chat_id = 'GROUP CHAT ID HERE'  # Replace with your actual group chat ID
allowed_users = [YOUR CHAT ID HERE] # Replace with your chat ID 

#Basic Hi command
@bot.message_handler(commands=['hi', 'hello']) # you can replace Hi and hello with whatever commands you want
def check_command(message):
    if message.from_user.id in allowed_users : # this checks if the message sent by the person is allowed to access bot or no
        bot.send_message(message.chat.id, "Hey there! How are you doing")#This gives back the reply to your corresponding message

#By this method the people who can access the bot is limited and only the users given by you can access the bot
