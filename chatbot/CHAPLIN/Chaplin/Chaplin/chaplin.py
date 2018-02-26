﻿import datetime
import db

class chatbot:
    monthes_names = ['января', 'февраля', 'марта', 'апреля', 
                     'мая', 'июня', 'июля', 'августа', 
                     'сентября', 'октября', 'ноября', 'декабря']

    def __init__(self, data, base):
        self.data = data
        self.base = base
    def chat(self, msg):
        now = datetime.datetime.now()
        date = db.make_date(now.day, now.month, now.year)
        print('|Добро пожаловать в CHAPLIN! Сегодня, ' +  str(now.day) + ' ' +\
            chatbot.monthes_names[now.month - 1] + ', у нас в прокате:|\n')
        for film in db.get_films_names(self.data, date):
            line = '  ' + film + ' ' * (30 - len(film))
            for time in db.get_times_by_film(self.data, date, film):
                line += time + ' '
            prices = db.get_prices_by_film(self.data, date, film)
            min_price, max_price = min(prices), max(prices)
            line += ' ' * (50 - len(line)) + str(min_price)
            if min_price != max_price:
                line += '-' + str(max_price)
            line += ' руб.'
            print(line)
        print('\n|Пожалуйста, выберите сеанс|')
