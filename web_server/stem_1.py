from flex_arr import flexion_arr, max_len

def stemmer(query):
    """"функция перебирает псевдофлексии слова запроса и, если находит их
    в мн-ве, возвращает по ним псевдоосновы. нулевая флексия предполагается всегда"""
    flexs = []
    for i in range(max_len, 0, -1):
        if len(query) > i and query[len(query) - i:] in flexion_arr:
            flexs.append(query[:len(query) - i])
    flexs.append(query)
    return flexs

def print_flex(query):
    print(query, stemmer(query)) 
	# print_flex('лаял')
	# print_flex('мам')
	# print_flex('бабах')
	# print_flex('лаял')
	# print_flex('ба')
	# print_flex('ого')
	# print_flex('пам')
	# print_flex('а')
	# print_flex('абвгдейку')
	# print_flex('мала')

#comments
#вынести список флексий за пределы функции (иначе он создает этот список для каждой словоформы)
#добавить алгоритм вычисления максимальной длины флексии в словаре и тоже вынести за пределы функции
#вынести список флексий и алгоритм вычисления максимальной длины флексии в отдельный модуль и импортировать их в стем0 и стем1
