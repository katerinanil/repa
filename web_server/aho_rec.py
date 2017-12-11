from string_algorithms import aho_corrasick, naive_find

morph_arr = ('a','b','cde','ab','abc')

def _aho_rec(ans, lst):
    i = ans[-1][0]
    sub = ans[-1][1]
    nextI = i + len(sub)
    if nextI == len(lst) or not len(lst[nextI]):
        yield ans
    else: 
        for nextSub in lst[nextI]:
            lst_copy = list(ans)
            lst_copy.append((nextI, nextSub))
            yield from _aho_rec(lst_copy, lst)

def aho(word):
    lst = [[] for i in range(len(word))]
    for i, sub in aho_corrasick.find(morph_arr, word):
        lst[i].append(sub)

    for sub in lst[0]:
        yield from _aho_rec([(0, sub)], lst)


if __name__ == '__main__':
    for ans in aho('abcde'):
        print(ans)
    pass