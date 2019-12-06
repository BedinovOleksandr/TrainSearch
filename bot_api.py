import telebot
from config import botToken


bot = telebot.TeleBot(botToken)


# def notification(masage):
#     bot.send_message(518356070, masage)
#
#
def send_capcha(chat_id):
     bot.send_document(chat_id, open('capcha.gif', 'rb'))


@bot.message_handler()
def messege_bot(message):
    print(message)
    bot.send_message(message.chat.id, 'Привет')
    send_capcha(message.chat.id)

bot.infinity_polling()

# if __name__ == '__main__':
#     notification('hello')
#     send_capcha()