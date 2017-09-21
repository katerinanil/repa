import before_stem

def stemmer(query):
        """"функция перебирает псевдофлексии слова запроса и, как только находит одну из них
    в словаре(?), возвращает по ней псевдооснову. таким образом предполагается флексия максимальной длины"""
    for i in range(3, 0, -1):
        if len(query) > i and query[len(query) - i:] in flexion_arr:
            return query[:len(query) - i]
    return query

if __name__ == '__main__':
  print(stemmer('лаял'))
  print(stemmer('мам'))
  print(stemmer('бабах'))
  print(stemmer('лаял'))
  print(stemmer('ба'))
  print(stemmer('ого'))
  print(stemmer('пам'))
  print(stemmer('а'))
  print(stemmer('их'))
  print(stemmer('ъъъъъ'))

#comments
#вынести список флексий за пределы функции
#добавить алгоритм вычисления максимальной длины флексии в словаре и тоже вынести за пределы функции
