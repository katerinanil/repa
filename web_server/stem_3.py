import shelve
import stem_2_1

def stemmer(query, db_stems_name, db_flex_name):
    db_stems = shelve.open(db_flex_name)
    db_flex = shelve.open(db_flex_name)
    count = 0
    for i in range(len(query), 0, -1):
        stem = query[:i]
        flex = query[i:]
        if stem in db_stems and \
           flex in db_flex and \
           db_stems[stem] & db_flex[flex]:
            count += 1
            yield stem
    #for el in stem_2_1.stemmer(query):
    #    yield el
    if not count: yield from stem_2_1.stemmer(query)
