from collections import OrderedDict
import shelve
from stem_2 import stemmer

class Token:
	def __init__(self, str, type):
		self.string = str
		self.token_type = type

def getalltokens(query):
	for w in filter(bool, query.split()):
		for st in stemmer(w):
			if st.isalpha(): yield Token(st, 'alpha')
			elif st.isdigit(): yield Token(st, 'digit')
			else: yield Token(st, 'other')
			#st = '<b>' + st + '</b>'

def query(query, db, limit_doc=-1, offset_doc=-1, pairs=None):
	#Множества пересечений имен файлов для каждого токена
	number_of_quotes = []
	newarray = []
	res = OrderedDict()
	intersec = set()
	#Токенизация запроса
	database = shelve.open(db)
	first_token = True
	for i in getalltokens(query):
		#Проверяем, содержится ли токен в db
		# print('IST', i.string)
		if i.string in database:
			if i.token_type == 'alpha' or i.token_type == 'digit':
				#Создаем мн-во имен файлов, в которых найден токен
				setOfFileNames = set(database[i.string])
				#Проверяем, выполняется ли цикл впервые
				if first_token:
					intersec = setOfFileNames
					first_token = False
				#Если цикл выполняется не в первый раз
				else: intersec &= setOfFileNames

	#Выбираем порцию файлов, указанных пользователем
	filenames_array = []
	intersection_list = sorted(list(intersec))
	#print('off =', offset_doc, 'lim =', limit_doc)
	if offset_doc < 1: offset_doc = 1
	if limit_doc == -1:
		limit_doc = len(intersection_list)
	else:
		limit_doc += offset_doc - 1
		if limit_doc > len(intersection_list):
			limit_doc = len(intersection_list)
	#print('off =', offset_doc, 'lim =', limit_doc)
	for i in range(offset_doc - 1, limit_doc):
		#print('BOO', i, end=' ')
		filenames_array.append(intersection_list[i])

	#print('RRRR')
	if pairs != None and len(pairs) < len(filenames_array):
		for i in range(len(filenames_array) - len(pairs)):
			pairs.append((None, None))
	for num_file, filename in enumerate(filenames_array):
		maxlen = 0
		for t in getalltokens(query):
			if t.token_type == 'alpha' or t.token_type == 'digit':
				l = len(database[t.string][filename])
				if l > maxlen: maxlen = l
		count = 0
		#Выбираем указанные позиции
		for i in range(maxlen):
			for t in getalltokens(query):
				if t.token_type == 'alpha' or t.token_type == 'digit':
					if len(database[t.string][filename]) <= i:
						continue
					pos = database[t.string][filename][i]
					count += 1
					if pairs != None:
						pair_start = pairs[num_file][1]
						if pair_start == None:
							pair_start = 0
						pair_end = pairs[num_file][0]
						if pair_end == None:
							pair_end = len(pairs[num_file])
						if count <= pair_start: continue
						if count > pair_end + pair_start: break
					positions = res.setdefault(filename, [])
					positions.append(pos)
	database.close()
	return res

#избавиться от дубликатов контекстов
def makeContexts(d):
	res = OrderedDict()
	for path in d:
		f = open(path)
		text = f.read()
		f.close()
		for st, end in d[path]:
			new_st = st
			#Добавляем левый контекст
			while new_st > 0:
				if text[new_st-1] in ['.', '!', '?', '—'] and \
                                   text[new_st].isspace() and \
				   text[new_st + 1].isupper():
					new_st += 1
					break
				new_st -= 1
			#Добавляем правый контекст
			new_end = end
			while new_end < len(text):
				if text[new_end] in ['.', '!', '?', '—']:
					break
				new_end += 1
			contexts = res.setdefault(path, [])
			#Объединяем контексты
			context = text[new_st:new_end]
			if not context in contexts:
				contexts.append(context)
		#Исключаем повторение контекстов для нескольких слов в запросе
		exLst = []
		exSet = set()
		for el in res[path]:
			if not el in exSet:
				exLst.append(el)
				exSet.add(el)
		res[path] = exLst
	#print("муааа", list(res))
	return res

if __name__ == '__main__':
	qres = query('но', 'db')
	print('-' * 80 + '\n', qres, sep='')
	mcRes = makeContexts(qres)
	for path in mcRes:
		print('^' * 80, path)
		for context in mcRes[path]:
			print('-' * 80, '\t', context)
