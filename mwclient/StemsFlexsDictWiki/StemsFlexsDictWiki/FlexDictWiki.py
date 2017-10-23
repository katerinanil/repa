from pprint import pprint
import mwclient
from StemsDictWiki import templs


site = mwclient.Site('ru.wiktionary.org')
templDict = {}
templArr = []

for t in templs:
    tem = 'Шаблон:%s' % t
    templArr.append(tem)
    #return (templArr)
    print(templArr)
    for temp in templArr:
        page = site.Pages[temp]
        for p in page:
            temp = temp[7:]
            isFlex = False
            for l in page.text().split('\n'):
                if not isFlex:
                    if l[8:17] == '={{{основа':
                        isFlex = True
                        stNumStart = l.find('}', 12)
                        stNumEnd = l.find('о', 10)
                        stemNum = l[stNumStart:stNumEnd]
                        flexStart = l.find('}', 12)
                        flex = l[flexStart+2:]
                        templDict.setdefault(flex, set()).add((temp, stemNum))

if __name__ == '__main__':
    pprint(templDict)
