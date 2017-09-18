import shelve
import config

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
    #lst = []
    for i in range(len(text)):
        ch = text[i]
        #print(ch, i, ch.isalpha())
        if not state:
            if ch.isalpha():
                first = i
                state = 1
        elif not ch.isalpha():
            state = 0
            yield text[first:i], first, i
            #print('first =', first, ', i =', i)
            #lst.append((text[first:i], first, i))
    #if state: lst.append((text[first:len(text)], first, len(text)))
    if state: yield text[first:len(text)], first, len(text)
    #print(text)
    #print('len =', len(text))
    #print(lst)


def makeDB(files):
    """
    Функция в качестве аргумента принимает список из путей и создаёт базу данных
    вида: {'слово': {'путь к файлу': [(индекс начала, индекс конца слова)]}}
    """
    db = shelve.open(config.DATABASE_NAME, writeback = True) 
    for f in files:        
        for word, left, right in getWords(f):
            word = word.lower()        
            s = db.setdefault(word, {})
            l = s.setdefault(f, [])
            l.append((left, right))
            db[word] = s
    db.close()

if __name__ == '__main__':
    makeDB(['small_text_1.txt'])
    #makeDB(['ViM Part 4.txt'])
    #makeDB(['ViM Part 3.txt'])
    #makeDB(['ViM Part 4.txt'])
