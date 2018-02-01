import re
from protection import protections
from DB import DB

class DState:
    GetInfo = 1

class Dealer:
    def __init__(self):
        self.state = None
        self.film = None
        self.time = None
    def getAnswer(self, protect, msg):
        if protect != None:
            if protect == protections.TicketInfo:
                self.film = Dealer._getFilmName(msg)
                time, isTimeInDB = Dealer._getFilmTime(msg)
                if isTimeInDB:
                    if self.film != None and \
                       not Dealer._checkTimeByFilm(self.film, time):
                        print('Извините, в это время фильма "' + self.film + ' " нет в прокате :(')
                    else: self.time = time
                elif time != None:
                    print('Но в это время не начинается ни один из наших фильмов!')
                self.state = DState.GetInfo
                
                if self._getInfo():
                    print('Билет куплен! Приятного просмотра! Ваш сеанс:\n' +
                          self.film + ' ' + self.time + '\n')
                    self.film = self.time = None
                    return protections.BackToChatter
                return None
            else:
                return None
        else:
            if self.state == DState.GetInfo:
                if self.film == None:
                    self.film = Dealer._getFilmName(msg)
                    if self.film != None and not\
                       Dealer._checkTimeByFilm(self.film, self.time):
                        self.film = None
                        print('К сожалению, у данного фильма нет старта в ' + self.time)
                else:
                    film = Dealer._getFilmName(msg)
                    if film != None: self.film = film
                if self.time == None:
                    self.time = Dealer._getFilmTime(msg)[0]
                    if self.film != None and self.time != None:
                        if not Dealer._checkTimeByFilm(self.film, self.time):
                            print('К сожалению, у фильма "' + self.film + '" нет старта в данное время..')
                            self.time = None

                if self._getInfo():
                    print('Билет куплен! Приятного просмотра! Ваш сеанс:\n' +
                          self.film + ' ' + self.time + '\n')
                    self.film = self.time = None
                    return protections.BackToChatter
                return None
            else:
                return None
    def _getInfo(self):
        if self.film == None:
            print('Пожалуйста, введите название фильма.')
            return False
        if self.time == None:
            print('Пожалуйста, выберите время сеанса  в формате чч:мм.')
            return False
        return True
    @staticmethod
    def _getFilmName(msg):
        for film in DB.getFilms():
            if film in msg: return film
        return None
    #returns (time, isTimeInDB)
    @staticmethod
    def _getFilmTime(msg):
        pattern = r'(\d\d:\d\d)'
        res = re.search(pattern, msg)
        if res == None: return None, False
        time = res.group()
        return time, time in DB.getTimes()

    #film exists
    @staticmethod
    def _checkTimeByFilm(film, time):
        return time in list(zip(*DB.getTimesAndCostsByFilm(film)))[0]

    ##time exists
    #@staticmethod
    #def _checkFilmByTime(film, time):
    #    return time in DB.getTimesByFilm(film)
