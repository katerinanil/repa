import datetime, db, kb

class chatbot:
    monthes_names = ['января', 'февраля', 'марта', 'апреля', 
                     'мая', 'июня', 'июля', 'августа', 
                     'сентября', 'октября', 'ноября', 'декабря']

    def __init__(self, data, base, morph):
        self.data = data
        self.base = base
        self.morph = morph
        now = datetime.datetime.now()
        self.date = db.make_date(now.day, now.month, now.year)

    def check_film_name(self, msg):
        for film in db.get_films_names(self.data, self.date):
            count = 0
            film_words = kb.knowledge_base.split_words(film)
            for film_word in film_words:
                film_word_norm = self.morph.normal_forms(film_word)[0]
                if film_word_norm in msg: count += 1
            if count >= 2 or (len(film_words) == 1 and count == 1):
                self.base.film_name = film; break

    def check_film_price(self, msg):
        check_phrases = ['почем', 'сколько стоит',
            'сколько стоят', 'какую цену', 'на сколько потянет']
        pass

    def chat(self, msg):
        self.check_film_name(msg)
        self.check_film_price(msg)

        if self.base.is_first:
            print('|Добро пожаловать в CHAPLIN! Сегодня, ' +  str(datetime.datetime.now().day) + ' ' +\
                chatbot.monthes_names[datetime.datetime.now().month - 1] + ', у нас в прокате:|\n')
            for film in db.get_films_names(self.data, self.date):
                line = '  ' + film + ' ' * (30 - len(film))
                for time in db.get_times_by_film(self.data, self.date, film):
                    line += time + ' '
                print(line)
            print('\nЧаплин: Пожалуйста, выберите сеанс')
        elif self.base.is_film_price:
            pass
        else:
            pass
