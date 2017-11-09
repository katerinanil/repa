from pprint import pprint
import mwclient
import shelve
import config

def createStemsTempls():
    site = mwclient.Site('ru.wiktionary.org')
    category = 'Слова из списка Сводеша/ru'
    stems = {}
    templs = set()

    #n = 82000
    #count = 2000
    #step = n / count
    #i = 0
    for page in site.Categories[category]:
        #if i >= n: break
        #i += 1
        #if i % step != 0: continue
        isStem = False
        templ = ''  
        for l in page.text().split('\n'):
            if not isStem: 
                if l[:8] == '{{сущ ru':
                    isStem = True
                    templ = l[2:]
            else:
                if l[:7] == '|основа':
                    stI = l.find('=', 7)
                    if stI == -1: continue
                    stem = l[stI+1:].replace('\u0301', '')
                    stem = stem.replace('\u045d', '')
                    stem = stem.replace('\u0300', '')
                    stem = stem.replace('\u030D', '')
                    stemNum = l[1:stI]
                    if not len(stem): continue
                    stems.setdefault(stem, {})\
                        .update({(templ,stemNum):page.page_title})
                else:
                    isStem = False
                    templs.add(templ)
    return stems, templs

def saveDict(d, name):
    db = shelve.open(name)
    for k in d: db[k] = d[k]
    db.close()

def loadDict(name):
    d = {}
    db = shelve.open(name)
    for k in db: d[k] = db[k]
    db.close()
    return d

if __name__ == '__main__':
    stems, templs = createStemsTempls()
    pprint(stems)
    print()
    pprint(templs)
    saveDict(stems, config.DATABASE_STEMS_NAME)
    saveDict({'templs': templs}, config.DATABASE_TEMPLS_NAME)
