import datetime
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
        print('Добро пожаловать в CHAPLIN! Сегодня, ' +  str(now.day) + ' ' +\
            chatbot.monthes_names[now.month - 1] + ', у нас в прокате:')
        for film in db.get_films_names(self.data, date):
            print(film)
        print('Пожалуйста, выберите сеанс.')
