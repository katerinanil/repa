import shelve
import stem_2_1
import config

def stemmer(query, db_stems_name = config.DATABASE_2000_STEMS_NAME, \
                   db_flex_name = config.DATABASE_2000_FLEX_NAME):
    db_stems = shelve.open(db_stems_name)
    db_flex = shelve.open(db_flex_name)
    flag = True
    for i in range(len(query), 0, -1):
        stem = query[:i]
        flex = query[i:]
        if stem in db_stems and \
           flex in db_flex and \
           db_stems[stem] & db_flex[flex]:
            flag = False
            yield stem
    #if flag:
    #   for el in stem_2_1.stemmer(query):
    #       yield el
    db_stems.close()
    db_flex.close()
    if flag:
        #print('LJKA')
        yield from stem_2_1.stemmer(query)
    else:
        print('NELOSHKA')