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

def add_film(db, date, film, times, halls):
    seats = []
    for i in range(SEATS_COUNT):
        price = 250
        if i == 4 or i == 5: price += 100
        seats.append(Seat(price))
    films_dict = db[date]
    films_dict[film] = (times, halls, seats)
    db[date] = films_dict

def get_films_names(db, date):
    films = db[date]
    return films.keys()

def get_times_by_film(db, date, film):
    return db[date][film][0]

def get_prices_by_film(db, date, film):
    prices = set()
    for seat in db[date][film][2]:
        prices.add(seat.price)
    return prices
