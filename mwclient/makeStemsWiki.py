import mwclient

f = open('stems.txt', 'w')
categories = ['Отглагольные существительные на -ка',
			  'Отглагольные существительные на -ание',
			  'Отглагольные существительные на -ение‎']
site = mwclient.Site('ru.wiktionary.org')
for c in categories:
	for page in site.Categories[c]:
		for l in page.text().split():
			if l[:7] == '|основа':
				stI = l.find('=', 7)
				if stI == -1: continue
				stem = l[stI+1:].replace('\u0301', '')
				stem = stem.replace('\u045d', '')
				if len(stem):
					print(page.page_title, '-', stem)
					f.write(stem + ', ')
f.close()
