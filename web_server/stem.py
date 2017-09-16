def stemmer(query):
    flexion_arr = {'а', 'ам', 'ами', 'ас', 'ах', 'ая', 'е', 'её', 'ей', 'ем', 'ла', 
                   'еми', 'емя', 'ex', 'ею', 'ёт', 'ёте', 'ёх', 'ёшь', 'и', 'ие',  
                   'ий', 'им', 'ими', 'ит', 'ите', 'их', 'ишь', 'ию', 'ми', 'мя', 'о',  
                   'ов', 'ого', 'ое', 'ой', 'ом', 'ому', 'ою', 'у', 'ум', 'умя', 'ут', 'ух', 
                   'ую', 'шь', 'ать', 'ять', 'еть', 'уть', 'у', 'ю', 'ем', 'ешь', 'ете', 'ет',
                   'ут', 'ют', 'ал', 'ял', 'ала', 'яла', 'али', 'яли', 'ул', 'ула', 'ули'} 
    flexs = [query]
    for i in range(3, 0, -1):
        if len(query) > i and query[len(query) - i:] in flexion_arr:
            flexs.append(query[:len(query) - i])
    return flexs

def print_flex(query):
    print(query, stemmer(query)) 
"""print_flex('лаял')
print_flex('мам')
print_flex('бабах')
print_flex('лаял')
print_flex('ба')
print_flex('ого')
print_flex('пам')
print_flex('а')
print_flex('абвгдейку')
print_flex('мала')"""
