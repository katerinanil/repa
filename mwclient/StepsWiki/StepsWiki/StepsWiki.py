import mwclient

categories = ['Отглагольные существительные на -ка',
			  'Отглагольные существительные на -ание',
			  'Отглагольные существительные на -ение‎']
site = mwclient.Site('ru.wiktionary.org')
for c in categories:
	for page in site.Categories[c]:
		if page.page_title != 'компилирование': continue
		for l in page.text().split():
			if l[:7] == '|основа':
				print("L='''", l.replace('\u0301', ''), "'''", sep='')
				stI = l.find('=', 7)
				stem = l[stI+1:].replace('\u0301', '')
				# if len(stem):
				# 	print(page.page_title, '-', stem)