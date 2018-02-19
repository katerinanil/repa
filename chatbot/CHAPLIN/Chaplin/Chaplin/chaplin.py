import datetime
import db

class chatbot:
    def __init__(self, db, kb):
        self.db = db
        self.kb = kb
    def chat(slef, msg):
        print('Добро пожаловать в CHAPLIN! Сегодня у нас в прокате:')
        now = datetime.datetime.now()
        date = db.make_date(date.day, date.month, date.year)
        print('Пожалуйста, выберите сеанс.')
