from string_algorithms import aho_corrasick, naive_find

morph_arr = ('ами','мам','а','ми','ма','и')

def aho(word):
    res = []
    lst = [[]] * len(word)
    for i, sub in aho_corrasick.find(morph_arr, word):
        lst[i].append(sub)
    
    for sub in lst[0]:
        pass

    for s in substring[s-1]:
        if len(s[s-1:]) >= 0:
            yield s[s-1]

    visit = False
    index = 0
    walk = []
    while index < len(word):
        if visit:
            currI = walk[-1][0]
        else:
            if len(lst[index]):
                walk.append((index, 0))
            else: index += 1

    walk = [(0,0)]

    currI = walk[-1][0]
    curr = [(currI, lst[currI][walk[-1][1]])]
    newI = currI + len(walk[-1][1])

    if len(lst[newI]):
        walk.append((newI, 0))


    res.append(curr)
