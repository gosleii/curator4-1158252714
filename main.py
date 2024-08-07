import telebot

bot = telebot.TeleBot("7228285296:AAGEgLjYCuRQkW-lpnT1_3O6Geeh8W-u418")

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет! Это бот о русском писателе Александре Ивановиче Куприне.')
    bot.send_message(message.chat.id, 'Бот имеет следующие команды: \n'
                                      '1. Биография писателя \n'
                                      '2. Самые известные произведения \n'
                                      '3. Краткие содержания книг')

@bot.message_handler(commands=['biograthy'])
def main(message):
    bot.send_message(message.chat.id, 'В биографии классика русской литературы Александра Ивановича Куприна затейливо переплелись масштабные события истории нашей Родины, происходящие на стыке эпох. Отличительными чертами его произведений стали чётко очерченные сюжетные линии, тщательная прорисовка персонажей и фона событий, что делает писателя одним из непревзойдённых мастеров реализма.')
    bot.send_message(message.chat.id, '[Полная биография](https://histrf.ru/read/biographies/aleksandr-ivanovich-kuprin?ysclid=lzjmy3ww9n152797626)', parse_mode="Markdown")

@bot.message_handler(commands=['popular_books'])
def main(message):
    bot.send_message(message.chat.id, 'Самые известные книги: \n'
                                      '1. Суламифь \n'
                                      '2. Поединок \n'
                                      '3. Гранатовый браслет \n'
                                      '4. Олеся \n'
                                      '5. Яма \n')
    bot.send_message(message.chat.id, 'Также хочу отметить книгу "Куст сирени", которая лично мне очень понравилась.')

@bot.message_handler(commands=['summary'])
def main(message):
    bot.send_message(message.chat.id, '1. [Краткое содержание "Суламифь"](https://obrazovaka.ru/books/kuprin/sulamif?ysclid=lzjngwmfle959869113) \n'
                                      '2. [Краткое содержание "Поединок"](https://obrazovaka.ru/books/kuprin/poedinok?ysclid=lzjni20puu100422973) \n'
                                      '3. [Краткое содержание "Гранатовый браслет"](https://obrazovaka.ru/books/kuprin/granatovyy-braslet?ysclid=lzjnjw404e726095194) \n'
                                      '4. [Краткое содержание "Олеся"](https://obrazovaka.ru/books/kuprin/olesya?ysclid=lzjnkj7b48131924805) \n'
                                      '5. [Краткое содержание "Яма"](https://briefly.ru/kuprin/jama/?ysclid=lzjnlf0fp0193011292)', parse_mode="Markdown")

bot.infinity_polling()