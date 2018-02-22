import os
import datetime
import shelve
from config import DB_NAME
import db

if __name__ == '__main__':
    if os.path.exists(DB_NAME + '.dat'): os.unlink(DB_NAME + '.dat')
    if os.path.exists(DB_NAME + '.bak'): os.unlink(DB_NAME + '.bak')
    if os.path.exists(DB_NAME + '.dir'): os.unlink(DB_NAME + '.dir')

    now = datetime.datetime.now()
    data = shelve.open(DB_NAME)
    db.add_date(data, db.make_date(now.day, now.month, now.year))
        #['Человек-Носорог', 'Великолепный удар 7',
        # 'Оно', '1945', 'Расписание', 'Невский 4D'])
    db.add_film(data, db.make_date(now.day, now.month, now.year),
                'Человек-Носорог', ('13:00', '14:00'), (0, 1))
    db.add_date(data, db.make_date(now.day + 1, now.month, now.year))
        #['Иннокентий', 'Бой с ленью',
        # 'Чаплин', 'Диплом'])
    db.add_date(data, db.make_date(now.day + 2, now.month, now.year))
        #['Как Витька Чеснок вёз Лёху Штыря в дом инвалидов'])
    #print(list(data.items()))
    data.close()