from stem_flex_arr import stem_arr, flexion_arr, getMaxLen

def stemmer(query):
  """ Мы сперва проходимся по словарю окончаний
  (в первую очередь все так же предполагая максимально длинную флексию)
  и для каждого псевдоокончания выделяем псевдооснову, проверяя, есть ли
  она в словаре основ. Если есть, мы заносим ее в базу и ищем дальше (то
  есть не удовлетворяемся первой найденной). И только если ни одну основу
  таким образом вплоть до нулевого окончания мы не нашли, то возвращаемся
  к нашему старому алгоритму и просто отсекаем возможные флексии, получая
  псевдоосновы."""

  lenq = len(query)
  maxflexlen = getMaxLen(flexion_arr)
  count = 0
  for i in range(maxflexlen, -1, -1):
    if lenq > i and (query[lenq - i:] in flexion_arr or i == 0):
      if query[:lenq - i] in stem_arr:
        count += 1
        yield query[:lenq - i]

  if count: return
  for i in range(maxflexlen, 0, -1):
    if lenq > i and query[lenq - i:] in flexion_arr:
      yield query[:lenq - i]
  yield query
