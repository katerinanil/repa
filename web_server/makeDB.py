import shelve
import config
from lemmatizer import lemmatizer

def getWords(path):
    """
    Функция в качестве аргумента принимает путь к файлу и возвращает список кортежей,
    в которых первый элемент - слово, второй - индекс начала слова,
    третий - индекс первого символа после конца слова
    """
    with open(path) as f: text = f.read()
    #state=1 - accumulating word
    #state=0 - passing letters
    state = 0
    first = -1
    for i in range(len(text)):
        ch = text[i]
        if not state:
            if ch.isalpha():
                first = i
                state = 1
        elif not ch.isalpha():
            state = 0
            yield text[first:i], first, i
    if state: yield text[first:len(text)], first, len(text)

def makeDB(files, dbname):
    """
    Функция в качестве аргумента принимает список из путей и создаёт базу данных
    вида: {'псевдооснова': {'путь к файлу': [(индекс начала, индекс конца слова)]}}
    """
    db = shelve.open(dbname, writeback = True)
    lemma = lemmatizer()
    for f in files:        
        for word, left, right in getWords(f):
            for st in lemma.lemmatize(word.lower()):
                s = db.setdefault(st, {})
                l = s.setdefault(f, [])
                l.append((left, right))
                #useless line below
                #db[st] = s
    db.close()

if __name__ == '__main__':
    makeDB(['ViM Part 1.txt', 'ViM Part 2.txt', 'ViM Part 3.txt', 'ViM Part 4.txt'], config.DATABASE_NAME)
    #makeDB(['small_text_1.txt', 'small_text_2.txt'], config.DATABASE_NAME)
