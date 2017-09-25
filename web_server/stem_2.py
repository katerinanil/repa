from stem_flex_arr import stem_arr, flexion_arr

def getMaxLen(arr):
  """функция возвращает максимальную длину флексии в flexion_arr, если он не пустой"""
  if not len(arr): return 0
  maxlen = next(iter(arr))
  for flex in arr:
    if len(flex) > len(maxlen):
      maxlen = flex
  return len(maxlen)

def stemmer(query):
  """функция перебирает псевдоосновы слова запроса и, если находит их
  в мн-ве, возвращает по ним основы. в противном случае выполняется
  старый алгоритм: функция перебирает псевдофлексии слова запроса и,
  если находит их в мн-ве флексий, возвращает по ним псевдоосновы.
  нулевая флексия предполагается всегда"""
  maxlen = getMaxLen(stem_arr)
  lenq = len(query)
  count = 0
  for i in range(1, maxlen + 1):
    if lenq > i and query[:i] in stem_arr:
      count += 1
      yield query[:i]

  if count: return
  maxlen = getMaxLen(flexion_arr)
  for i in range(maxlen, 0, -1):
    if lenq > i and query[lenq - i:] in flexion_arr:
      yield query[:lenq - i]
  yield query
