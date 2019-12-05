import telebot

mySlaveToken = 'yor token here'
bot = telebot.TeleBot(mySlaveToken)


def notification(masage):
    bot.send_message(518356070, masage)

def send_capcha():
    bot.send_document(518356070, open('capcha.gif', 'rb'))


if __name__ == '__main__':
    #notification('hello')
    send_capcha()