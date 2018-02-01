from protection import protections
from DB import DB
from dealer import Dealer

class Chatter:
    def __init__(self):
        self.hello_flag = True
    def getAnswer(self, protect, msg):
        if protect != None:
            if protect == protections.BackToChatter:
                self.getAnswer(None, "")
            else:
                return None
        else:
            if len(msg) == 0:
                self._printTable()
                return None
            elif self._checkInfo(msg):
                return protections.TicketInfo
            else:
                self._printTable()
                return None
    def _printTable(self):
        if self.hello_flag:
            print('Добро пожаловать в CHAPLIN! Сегодня у нас в прокате:')
            self.hello_flag = False
        else:
            print('У нас всё еще в прокате:')
        for film in DB.getFilms():
            print(film[0].upper(), film[1:], ': ', sep='', end='')
            tcs = DB.getTimesAndCostsByFilm(film)
            print(tcs[0][0], ' (', tcs[0][1], ' руб.)', sep='', end='')
            for tc in tcs[1:]:
                print(', ', tc[0], ' (', tc[1], ' руб.)', sep='', end='')
            print()
        print('Пожалуйста, выберите сеанс.')  
    def _checkInfo(self, msg):
        res = Dealer._getFilmName(msg)
        if res != None: return res
        time, isTimeInDB = Dealer._getFilmTime(msg)
        if time != None and not isTimeInDB:
            print('Увы, в это время сегодня не начинается ни один фильм. Выберете другое время?')
            return None
        return time
