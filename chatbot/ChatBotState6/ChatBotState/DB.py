class Item:
    def __init__(self, film, time, cost):
        self.film = film
        self.time = time
        self.cost = cost

class DB:
    db = []
    db.append(Item('марсианин', '10:00', '150'))
    db.append(Item('марсианин', '12:00', '150'))
    db.append(Item('игра', '13:00', '150'))
    db.append(Item('интерстеллар', '15:00', '250'))
    db.append(Item('экзамен', '16:00', '300'))
    db.append(Item('турист', '17:00', '200'))
    db.append(Item('охранник', '18:00', '200'))
    db.append(Item('легенда', '19:00', '300'))
    db.append(Item('гладиатор', '20:00', '200'))
    db.append(Item('иллюзионист', '21:00', '280'))
    db.append(Item('подмена', '22:00', '250'))
    
    @staticmethod
    def add(film, time, cost):
        self.db.append(Item(film, time, cost))

    @staticmethod
    def getFilms():
        films = set()
        for item in DB.db:
            films.add(item.film)
        return films

    @staticmethod
    def getTimes():
        times = set()
        for item in DB.db:
            times.add(item.time)
        return times

    @staticmethod
    def getTimesAndCostsByFilm(film):
        tc = []
        for item in DB.db:
            if item.film == film:
                tc.append((item.time, item.cost))
        return tc
