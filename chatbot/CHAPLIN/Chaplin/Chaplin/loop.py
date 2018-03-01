import shelve
import config, db
from kb import knowledge_base 
from chaplin import chatbot

if __name__ == '__main__':
    data = shelve.open(config.DB_NAME)
    base = knowledge_base()
    chaplin = chatbot(data, base)

    msg = ''
    while True:
        chaplin.chat(msg)
        print('    Вы: ', end='')
        msg = input()
        pass