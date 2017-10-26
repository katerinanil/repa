from pprint import pprint
import mwclient
from StemsDictWiki import loadDict, db_templs

site = mwclient.Site('ru.wiktionary.org')
templDict = {}
templArr = loadDict(db_templs)

print(templs)

for t in templs:
    tem = 'Шаблон:%s' % t
    templArr.append(tem)
    print(tem)
print(templArr)
for temp in templArr:    
    page = site.Pages[temp]
    temp = temp[7:]
    isFlex = False
    for l in page.text().split('\n'):
        #print (l[:2])
        #if not isFlex:
        if l[8:17] == '={{{основа':
            isFlex = True
            stNumStart = l.find('}', 12)
            stNumEnd = l.find('о', 10)
            stemNum = l[stNumStart:stNumEnd]
            print(stemNum)
            flexStart = l.find('}', 12)
            flex = l[flexStart+2:]
            print(flex)
            templDict.setdefault(flex, set()).add((temp, stemNum))

if __name__ == '__main__':
    pprint(templDict)
