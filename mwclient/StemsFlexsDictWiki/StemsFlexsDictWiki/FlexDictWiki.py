from pprint import pprint
import mwclient
from StemsDictWiki import loadDict, saveDict

def createFlexes():
    site = mwclient.Site('ru.wiktionary.org')
    templDict = {}
    for t in loadDict('db_2000_templs')['templs']:    
        page = site.Pages['Шаблон:%s' % t]
        for l in page.text().split('\n'):
            if l.find('={{{основа') != -1:
                rOpenBrace = l.rfind('{')
                lCloseBrace = l.find('}')
                rCloseBrace = l.rfind('}')
                flex = l[rCloseBrace+1:]
                for i in range(768, 879):
                    flex = flex.replace(chr(i), '')
                    flex = flex.replace(' ', '')
                stemNum = l[rOpenBrace+1:lCloseBrace]
                templDict.setdefault(flex, set()).add((t, stemNum))
    return templDict

if __name__ == '__main__':
    templDict = createFlexes()
    pprint(templDict)
    saveDict(templDict, 'db_2000_flex_2')
    print(templDict.keys())
