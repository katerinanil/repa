stem_arr = {'мам', 'мамам', 'мыл', 'рам', 'про', 'при', 'на', 'но'}

flexion_arr = {'а', 'ам', 'ами', 'ас', 'ах', 'ая', 'е', 'её', 'ей', 'ем', 'ла', 
               'еми', 'емя', 'ex', 'ею', 'ёт', 'ёте', 'ёх', 'ёшь', 'и', 'ие',  
               'ий', 'им', 'ими', 'ит', 'ите', 'их', 'ишь', 'ию', 'ми', 'мя', 'о',  
               'ов', 'ого', 'ое', 'ой', 'ом', 'ому', 'ою', 'у', 'ум', 'умя', 'ут', 'ух', 
               'ую', 'шь', 'ать', 'ять', 'еть', 'уть', 'у', 'ю', 'ем', 'ешь', 'ете', 'ет',
               'ут', 'ют', 'ал', 'ял', 'ала', 'яла', 'али', 'яли', 'ул', 'ула', 'ули'}

def getMaxLen(arr):
  """функция возвращает максимальную длину флексии в flexion_arr, если он не пустой"""
  if not len(arr): return 0
  maxlen = next(iter(arr))
  for flex in arr:
    if len(flex) > len(maxlen):
      maxlen = flex
  return len(maxlen)


maxflexlen = getMaxLen(flexion_arr)

#from functools import reduce
#def getMaxLen2():
#return len(reduce(lambda acc, next: acc if len(acc) > len(next) else next, fl_ar))
