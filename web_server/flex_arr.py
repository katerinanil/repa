from functools import reduce

flexion_arr = {'а', 'ам', 'ами', 'ас', 'ах', 'ая', 'е', 'её', 'ей', 'ем', 'ла', 
               'еми', 'емя', 'ex', 'ею', 'ёт', 'ёте', 'ёх', 'ёшь', 'и', 'ие',  
               'ий', 'им', 'ими', 'ит', 'ите', 'их', 'ишь', 'ию', 'ми', 'мя', 'о',  
               'ов', 'ого', 'ое', 'ой', 'ом', 'ому', 'ою', 'у', 'ум', 'умя', 'ут', 'ух', 
               'ую', 'шь', 'ать', 'ять', 'еть', 'уть', 'у', 'ю', 'ем', 'ешь', 'ете', 'ет',
               'ут', 'ют', 'ал', 'ял', 'ала', 'яла', 'али', 'яли', 'ул', 'ула', 'ули'}
def getMaxLen():
  if not len(flexion_arr): return 0
  maxlen = next(iter(flexion_arr))
  for flex in flexion_arr:
      if len(flex) > len(maxlen):
          maxlen = flex
  return len(maxlen)

def getMaxLen():
  return len(reduce(lambda acc, next: acc if len(acc) > len(next) else next, flexion_arr))