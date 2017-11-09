import shelve
import stem_2_1
import config

class lemmatizer():
    def __init__(self, db_stems_name = config.DATABASE_2000_STEMS_NAME, \
                       db_flex_name = config.DATABASE_2000_FLEX_NAME):
        self.db_stems = shelve.open(db_stems_name)
        self.db_flex = shelve.open(db_flex_name)
    def __del__(self):
        db_stems.close()
        db_flex.close()
    def lemmatize(self, query):
        flag = True
        for i in range(len(query), 0, -1):
            stem = query[:i]
            flex = query[i:]
            lemmas = set()
            if stem in self.db_stems and flex in self.db_flex:
                for t in self.db_stems[stem].keys() & self.db_flex[flex]:
                    lemmas.add(self.db_stems[stem][t])
            if lemmas: flag = False
            for l in lemmas: yield l
        if flag: yield from stem_2_1.stemmer(query)
