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

    def get_norm(self, word):
        return self.morph.normal_forms(word)[0]

    def check_film_name(self, msg):
        for film in db.get_films_names(self.data, self.date):
            count = 0
            film_words = kb.knowledge_base.split_words(film)
            for film_word in film_words:
                film_word_norm = self.get_norm(film_word)
                if film_word_norm in msg: count += 1
            if count >= 2 or (len(film_words) == 1 and count == 1):
                self.base.film_name = film; break

    def check_number(self, st, nxt):
        nums = ['ноль', 'один', 'два', 'три', 'четыре',
         'пять', 'шесть', 'семь', 'восемь', 'девять',
         'десять', 'одиннадцать', 'двенадцать',
         'тринадцать', 'четырнадцать', 'пятнадцать',
         'шестнадцать', 'семнадцать', 'восемнадцать',
         'девятнадцать']
        tens = ['двадцать', 'тридцать',
                  'сорок', 'пятьдесят']
        st = self.get_norm(st)
        try: num = int(st); return num
        except ValueError: pass
        try: index = nums.index(st); return index
        except ValueError: pass
        try:
            index = tens.index(st)
            try:
                nxt = self.get_norm(nxt)
                index2 = nums[1:10].index(nxt)
                return index * 10 + 20 + index2 + 1
            except ValueError: return index * 10 + 20
        except ValueError: return None

    def check_film_time(self, msg):

        pass

    def check_film_price(self, msg):
        for check in ['почем', 'сколько стоит',
            'сколько стоят', 'какую цену']:
            count = 0
            check_words = kb.knowledge_base.split_words(check)
            for check_word in check_words:
                check_word_norm = self.get_norm(check_word)
                if check_word_norm in msg: count += 1
            if count == len(check_words):
                self.base.is_film_price = True
                self.base.is_first = False; break

    def chat(self, msg):
        self.check_film_name(msg)
        self.check_film_time(msg)
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
            if self.base.film_name != None:
                print('Чаплин: Цены билетов фильма ' + self.base.film_name + ':\n')
                for time in db.get_times_by_film(self.data, self.date, self.base.film_name):
                    print('\t' + time + '\t', end='')
                    mn, mx = db.get_minmax_price_by_film_and_time(self.data, self.date, self.base.film_name, time)
                    print(mn, '-', mx, ' руб.', sep='')
            else: print('Чаплин: Цена какого фильма интересует?')
        else:
            pass
