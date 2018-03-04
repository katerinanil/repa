import shelve

HALLS_COUNT = 3
SEATS_COUNT = 100

class Seat:
    FREE = 0
    BOOK = 1
    BUSY = 2
    def __init__(self, price):
        self.state = Seat.FREE
        self.price = price

def make_date(day, month, year):
    return str(day)+'.'+str(month)+'.'+str(year)

def add_date(db, date):
    db[date] = {}

def add_film(db, date, film, timesAndHalls):
    for i in range(len(timesAndHalls)):
        seats = []
        for j in range(SEATS_COUNT):
            price = 200
            if j == 4 or j == 5: price += 100
            time = timesAndHalls[i][0]
            hour = int(time[:2])
            if hour > 17:
                if hour < 23:
                    price += 50 * (hour - 18)
                else: price += 150
            seats.append(Seat(price))
        thPair = timesAndHalls[i]
        thPair.append(seats)
    films_dict = db[date]
    films_dict[film] = timesAndHalls
    db[date] = films_dict
    #print(list(db.items()))
    #pass

def get_dates(db):
    return db.keys()

def get_films_names(db, date):
    films = db[date]
    return films.keys()

def get_times_by_film(db, date, film):
    return [t for t, h, s in db[date][film]]
