import shelve
import config
import stem_2_1

class lemmatizer():
    def __init__(self, db_stems_name = config.DATABASE_STEMS_NAME, \
                       db_flex_name = config.DATABASE_FLEX_NAME):
        self.db_stems = shelve.open(db_stems_name)
        self.db_flex = shelve.open(db_flex_name)
    def __del__(self):
        self.db_stems.close()
        self.db_flex.close()
    def lemmatize(self, query):
        flag = True
        for i in range(len(query), 0, -1):
            stem = query[:i]
            flex = query[i:]
            lemmas = set()
            """in case we find our stem in db_stems and flex in db_flex,
            we intersect the keys of inner dict of db_stems (the tuples) with
            the values of db_flex (also the tuples); and if the intersection
            is not empty we add the values of the inner dict of db_stems (lems)
            to set lemmas"""
            if stem in self.db_stems and flex in self.db_flex:
                for t in self.db_stems[stem].keys() & self.db_flex[flex]:
                    lemmas.add(self.db_stems[stem][t])
            if lemmas:
                flag = False
            for l in lemmas: yield l
        """returning to the previous algorithm if this one failed"""
        if flag:
            yield from stem_2_1.stemmer(query)
        #else: print("New algorithm is on duty")
