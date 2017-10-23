from pprint import pprint
import mwclient

site = mwclient.Site('ru.wiktionary.org')
categories = ['Отглагольные существительные на -ка',
			  'Отглагольные существительные на -ание',
			  'Отглагольные существительные на -ение‎'
              ]
stems = {}
templs = set()

for c in categories:
    for page in site.Categories[c]: # почему от с
        isStem = False
        templ = ''  
        for l in page.text().split('\n'):
            if not isStem: #что за иф нот, зачем вообще флаг
                if l[:8] == '{{сущ ru':
                    isStem = True
                    templ = l[2:]
            else:
                if l[:7] == '|основа':
                    stI = l.find('=', 7)
                    if stI == -1: continue
                    stem = l[stI+1:].replace('\u0301', '')
                    stem = stem.replace('\u045d', '')
                    stemNum = l[1:stI]
                    if not len(stem): continue
                    stems.setdefault(stem, set()).add((templ, stemNum))
                else:
                    isStem = False
                    templs.add(templ)
if __name__ == '__main__':
    pprint(stems)
    print()
    pprint(templs)

