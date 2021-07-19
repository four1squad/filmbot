import telebot

bot = telebot.TeleBot('1817895224:AAH8aEZywuJpSFpZMSDMil6ow2jSVYGLPAE')

keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('детектив', 'комедия', 'драма')
keyboard.row('боевик', 'романтика', 'триллер',)

def send(id, text):
    bot.send_message(id, text, reply_markup = keyboard)

@bot.message_handler(commands =['start'])
def answer(message):
    send(message.chat.id, 'Доброго времени суток!\nВыбирайте жанр фильмов, который Вам нравится.\nНадеюсь, Вы еще не пересмотрели всё предложенное.')

@bot.message_handler(content_types = ['text'])
def main(message):
    id = message.chat.id
    msg = message.text

    if msg == 'привет':
        send(id, 'Чем могу быть Вам полезна?')

    elif msg == 'пока':
        send(id, 'До скорых встреч!')
    
    elif msg == 'детектив':
        send(id, 'Остров проклятых\n Клаустрофобы:Квест в Москве\nКомната желаний\nАмнезия\nДостать ножи\nНочной портье\nНезванный гость')
        
    elif msg == 'комедия':
        send(id, 'Очень страшное кино\nБатя\nУдивительно путешествие доктора Дулиттла\nКролик Питер\nУик-энд у Берни\nКрасотка на всю голову')

    elif msg == 'драма':
        send(id, 'Секрет\nСумасшедшая любовь\nМавританец\nЗемля кочевников\nПальма\nПобег из Претории')

    elif msg == 'боевик':
        send(id, 'Гнев человеческий\nНикто\nДовод\nВойна будущего\nЗаступник\nАнна')

    elif msg == 'романтика':
        send(id, 'Жизнь за год\nВ метре друг от друга\nЕсли я останусь\nВиноваты звезды\nВсем парням, которых я любила\nС любовью, Рози')

    elif msg == 'триллер':
        send(id, 'Кто не спрятался\nТихое место\nОбратный отсчет\nПравда или действие\nОстров фантазий\nНечестивые')

    else:
        send(id, 'Повторите еще раз.')

bot.polling()
