from collections import OrderedDict
import shelve

class Token:
	def __init__(self, str, type):
		self.string = str
		self.token_type = type

def getalltokens(query, lemma):
	for w in filter(bool, query.split()):
		for st in lemma.lemmatize(w):
			if st.isalpha(): yield Token(st, 'alpha')
			elif st.isdigit(): yield Token(st, 'digit')
			else: yield Token(st, 'other')
			#st = '<b>' + st + '</b>'

def query(query, db, lemma, limit_doc=-1, offset_doc=-1, pairs=None):
	#Множества пересечений имен файлов для каждого токена
	number_of_quotes = []
	newarray = []
	intersec = set()
	#Токенизация запроса
	database = shelve.open(db)
	first_token = True
	for i in getalltokens(query, lemma):
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
	res = OrderedDict()
	for num_file, filename in enumerate(filenames_array):
		maxlen = 0
		for t in getalltokens(query, lemma):
			if t.string in database:
				if t.token_type == 'alpha' or t.token_type == 'digit':
				    l = len(database[t.string][filename])
				    if l > maxlen: maxlen = l
		#Выбираем указанные позиции
		for i in range(maxlen):
			for t in getalltokens(query, lemma):
				if t.string in database and (t.token_type == 'alpha' or t.token_type == 'digit'):
					if len(database[t.string][filename]) <= i: continue
					pos = database[t.string][filename][i]
					positions = res.setdefault(filename, [])
					if not pos in positions: positions.append(pos)
	database.close()
	return res

#нужно отсекать дубликаты не в makeContexts
#for i in range(len(res[path][1])):
#   res[path][1][i] = list(set(res[path][1][i]))
#но выше где-то здесь
#if pair_end == None:
#	pair_end = 1000
#if count <= pair_start: continue
#if count > pair_end + pair_start: break

#избавиться от дубликатов контекстов
def makeContexts(d, pairs=None):
	res = OrderedDict()
	punc = ['.', '!', '?', '—', '–', '[', ']']
	for path in d:
		f = open(path)
		text = f.read()
		f.close()
		for st, end in d[path]:
			new_st = st
			#Добавляем левый контекст
			while new_st > 0:
				if text[new_st-1] in punc and  text[new_st].isspace() and \
                    (text[new_st + 1].isupper() or text[new_st + 1] in punc):
					new_st += 1
					break
				new_st -= 1
			#Добавляем правый контекст
			new_end = end
			while new_end < len(text) - 2:
				if text[new_end] in punc and text[new_end + 1].isspace() and \
				    (text[new_end + 2].isupper() or text[new_end + 2] in punc):
					new_end += 1
					break
				new_end += 1
			contexts, positions = res.setdefault(path, ([], []))
			#Объединяем контексты
			context = text[new_st:new_end]
			if not context in contexts:
				contexts.append(context)
				positions.append([(st - new_st, end - new_st)])
			else:
				conI = contexts.index(context)
				positions[conI].append((st - new_st, end - new_st))
		#for i in range(len(res[path][1])):
		#	res[path][1][i] = list(set(res[path][1][i]))
		for pos in res[path][1]:
			for i in range(len(pos)-1):
				for j in range(len(pos)-i-1):
					if pos[j][0] > pos[j+1][0]:
						pos[j], pos[j+1] = pos[j+1], pos[j]
	#print("муааа", list(res))

	if pairs != None:
		for num, key in enumerate(res):
			st = pairs[num][1]
			if st == None: st = 0
			end = pairs[num][0]
			if end == None:
				end = len(res[key][0])
			else: end += st
			res[key] = (res[key][0][st:end], \
                        res[key][1][st:end])

	return res

if __name__ == '__main__':
	qres = query('но', 'db')
	print('-' * 80 + '\n', qres, sep='')
	mcRes = makeContexts(qres)
	for path in mcRes:
		print('^' * 80, path)
		for context in mcRes[path]:
			print('-' * 80, '\t', context)
