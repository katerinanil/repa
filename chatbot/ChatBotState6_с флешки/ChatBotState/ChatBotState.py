import re
from pymorphy2 import MorphAnalyzer
from chatter import Chatter
from dealer import Dealer

def makeRequest(msg):
    morph = MorphAnalyzer()
    words = list(filter(None, str.split(re.sub(r'[^\w\d\s:]', \
                 r' ', msg).lower())))
    for i in range(len(words)):
        words[i] = morph.normal_forms(words[i])[0]
    #return words
    msg = ''
    for word in words: msg += word + ' '
    return msg

if __name__ == '__main__':
    chatter = Chatter()
    dealer = Dealer()
    #True=chatter, False=dealer
    state = True
    ans = None
    msg = ''

    while True:
        if state: ans = chatter.getAnswer(ans, msg)
        else: ans = dealer.getAnswer(ans, msg)
        if ans != None: state = not state
        else: msg = makeRequest(input())
