import datetime
import db

class chatbot:
    def __init__(self, db, kb):
        self.db = db
        self.kb = kb
    def chat(slef, msg):
        print('����� ���������� � CHAPLIN! ������� � ��� � �������:')
        now = datetime.datetime.now()
        date = db.make_date(date.day, date.month, date.year)
        print('����������, �������� �����.')
