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

def add_date(db, date, films):
    db[date] = {}

def add_film(db, date, film, times, halls):
    seats = []
    for ia in range(SEATS_COUNT):
        price = 250
        if i == 4 or i == 5: price += 100
        seats.append(Seat(price))
    db[date][film] = (times, halls, seats)

#get films