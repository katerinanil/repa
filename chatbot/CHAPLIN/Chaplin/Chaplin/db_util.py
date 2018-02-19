import shelve
from config import DB_NAME
import db

if __name__ == '__main__':
    data = shelve.open(DB_NAME)
    db.add_date(data, db.make_date(19, 2, 2018), \
        ['Человек-Носорог', 'Великолепный удар 7',
         'Оно', '1945', 'Расписание', 'Невский 4D'])
    db.add_date(data, db.make_date(20, 2, 2018), \
        ['Иннокентий', 'Бой с ленью',
         'Чаплин', 'Диплом'])
    db.add_date(data, db.make_date(21, 2, 2018), \
        ['Как Витька Чеснок вёз Лёху Штыря в дом инвалидов'])
    data.close()