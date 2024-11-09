import telebot

TELEGRAM_API_TOKEN = '[YOUR BOT API TOKEN HERE]' #The token of bot created using BotFather
bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

group_chat_id = 'GROUP CHAT ID HERE'  # Replace with your actual group chat ID
allowed_users = [YOUR CHAT ID HERE] # Replace with your chat ID 

#Basic Hi command
@bot.message_handler(commands=['hi', 'hello'])
    if message.from_user.id in allowed_users : 
        bot.send_message(message.chat.id, "Hey there! How are you doing")

@bot.message_handler(commands=['start'])
    if message.from_user.id : 
        bot.send_message(message.chat.id, "Please specify a task for me to follow sir!")
        

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
Here are the commands you can use:
/hi or /hello - Say hello to the bot.
/help - Get this help message.
/start - Start the bot.
    """
    bot.send_message(message.chat.id, help_text)
