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

    def _get_norm(self, word):
        return self.morph.normal_forms(word)[0]

    def check_film_name(self, msg):
        for film in db.get_films_names(self.data, self.date):
            count = 0
            film_words = kb.knowledge_base.split_words(film)
            for film_word in film_words:
                film_word_norm = self._get_norm(film_word)
                if film_word_norm in msg: count += 1
            if count >= 2 or (len(film_words) == 1 and count == 1):
                self.base.film_name = film; break

    def _check_number(self, st, nxt):
        nums = ['ноль', 'один', 'два', 'три', 'четыре',
         'пять', 'шесть', 'семь', 'восемь', 'девять',
         'десять', 'одиннадцать', 'двенадцать',
         'тринадцать', 'четырнадцать', 'пятнадцать',
         'шестнадцать', 'семнадцать', 'восемнадцать',
         'девятнадцать']
        tens = ['двадцать', 'тридцать',
                  'сорок', 'пятьдесят']
        st = self._get_norm(st)
        try: num = int(st); return num, 1
        except ValueError: pass
        try: index = nums.index(st); return index, 1
        except ValueError: pass
        if st == 'час': return 1, 1
        try:
            index = tens.index(st)
            try:
                nxt = self._get_norm(nxt)
                index2 = nums[1:10].index(nxt)
                return index * 10 + 20 + index2 + 1, 2
            except ValueError: return index * 10 + 20, 1
        except ValueError: return None, 0

    def check_film_time(self, msg):
        pmam = ['день', 'вечер', 'полдень', 'полночь']
        half = ['половина', 'четверть']
        ft = self.base.film_time
        for w in msg:
            if w in pmam: ft.pmam = w
            if w in half: ft.half = w
                
        if not ft.pmam in pmam[-2:]:
            for i in range(len(msg)):
                next_word = msg[i+1] if i != len(msg)-1 else ''
                num_h, num_h_count = self._check_number(msg[i], next_word)
                if num_h != None:
                    if ft.minutes == None:
                        if i < len(msg) - num_h_count:
                            next_word = msg[i+num_h_count+1] if i != len(msg)-num_h_count-1 else ''
                            num_m, num_m_count = self._check_number(msg[i+num_h_count], next_word)
                            if num_m != None:
                               ft.hours = num_h
                               ft.minutes = num_m
                               break
                            elif self._get_norm(next_word) == 'минута':
                               ft.minutes = num_h
                            elif ft.hours == None: ft.hours = num_h
                        else: ft.hours = num_h; break
                    else: ft.hours = num_h; break
        else: ft.hours = 0 if ft.pmam == pmam[-1] else 12; ft.minutes = 0
        if not ft.hours in range(0, 24): ft.hours = None
        elif not ft.minutes in range(0, 60): ft.minutes = None
        if ft.hours != None:
            if ft.minutes == None: ft.minutes = 0
            if ft.pmam in pmam[0:2]: ft.hours += 12
            if ft.half != None:
                d = datetime.datetime(1970, 1, 1, ft.hours, ft.minutes, 0)
                span = 30 if ft.half == half[0] else 45
                d -= datetime.timedelta(minutes=span)
                ft.hours = d.hour
                ft.minutes = d.minute
            time_ex = '%02d:%02d' % (ft.hours, ft.minutes)
            self.base.film_time = kb.knowledge_base.film_time_type()
            self.base.film_time.time = time_ex
        else: self.base.film_time = kb.knowledge_base.film_time_type()

    def check_film_price(self, msg):
        for check in ['почем', 'сколько стоит',
            'сколько стоят', 'какую цену']:
            count = 0
            check_words = kb.knowledge_base.split_words(check)
            for check_word in check_words:
                check_word_norm = self._get_norm(check_word)
                if check_word_norm in msg: count += 1
            if count == len(check_words):
                self.base.is_film_price = True
                self.base.is_first = False; break

    def chat(self, msg):
        self.check_film_name(msg)
        self.check_film_time(msg)
        self.check_film_price(msg)

        print('TIME=' + str(self.base.film_time.time) + '\n')

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
