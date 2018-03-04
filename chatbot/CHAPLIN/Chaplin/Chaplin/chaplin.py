import datetime
import db

class chatbot:
    monthes_names = ['января', 'февраля', 'марта', 'апреля', 
                     'мая', 'июня', 'июля', 'августа', 
                     'сентября', 'октября', 'ноября', 'декабря']

    def __init__(self, data, base):
        self.data = data
        self.base = base

        
    def check_film_name(self, msg):
        pass

    def check_film_price(self, msg):
        pass

    def chat(self, msg):
        self.check_film_name(msg)
        self.check_film_price(msg)

        if self.base.is_first:
            now = datetime.datetime.now()
            date = db.make_date(now.day, now.month, now.year)
            print('|Добро пожаловать в CHAPLIN! Сегодня, ' +  str(now.day) + ' ' +\
                chatbot.monthes_names[now.month - 1] + ', у нас в прокате:|\n')
            for film in db.get_films_names(self.data, date):
                line = '  ' + film + ' ' * (30 - len(film))
                for time in db.get_times_by_film(self.data, date, film):
                    line += time + ' '
                print(line)
            print('\nЧаплин: Пожалуйста, выберите сеанс')
        elif self.base.is_film_price:
            pass
        else:
            pass
