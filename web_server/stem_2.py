from flex_arr import flexion_arr, max_len

stem_arr = {'мам', 'мыл', 'рам'}

def getMaxLen():
  """функция возвращает максимальную длину основы в stem_arr, если он не пустой"""
  if not len(stem_arr): return 0
  maxlen = next(iter(stem_arr))
  for st in stem_arr:
      if len(st) > len(maxlen):
          maxlen = st
  return len(maxlen)

getmaxlen = getMaxLen()

def stemmer(query):
    """"функция перебирает псевдоосновы слова запроса и, если находит их
    в мн-ве, возвращает по ним основы"""
    for i in range(getmaxlen, 0, +1): #(0, getmaxlen, +1)
        if len(query) > i and query[:len(query) - i] in stem_arr:
            stems = query[:len(query) - i] #как я поняла нам теперь хватает одной основы (уточнить)
    return stems

    if stems = 0:
    """в общем тут я хотела сказать, что если верхний новый стеммер для
    отдельно взятого слова запроса не сработал, что возвращаемся к старому стеммеру"""
        flexs = []
        for i in range(max_len, 0, -1):
        if len(query) > i and query[len(query) - i:] in flexion_arr:
            flexs.append(query[:len(query) - i])
        flexs.append(query)
        return flexs

#а как у нас обрабатывался случай, когда флексия = query и случай с пустой строкой?
