from string_algorithms import aho_corrasick, naive_find

def _aho_rec(ans, lst):
    i = ans[-1][0] #first element of last taken tuple
    sub = ans[-1][1] #2nd element of last taken tuple
    nextI = i + len(sub) #index of next substring
    """in case we got full combo or made our best
    we return them, otherwise we continue making combos"""
    if nextI == len(lst):# or not len(lst[nextI]):
        yield ans
    else: 
        for nextSub in lst[nextI]:
            lst_copy = list(ans)
            lst_copy.append((nextI, nextSub))
            yield from _aho_rec(lst_copy, lst)

def aho(word, morph_arr):
    """make the list of lists which equal to the number of letters
    and append substrings returned by aho to the related list"""
    lst = [[] for i in range(len(word))]
    for i, sub in aho_corrasick.find(morph_arr, word):
        lst[i].append(sub)
    """here we get the algorithm started"""
    for sub in lst[0]:
        yield from _aho_rec([(0, sub)], lst)


if __name__ == '__main__':
    for ans in aho('мама', ('a','b','cde','ab','abc', 'мам','ами','мама','ми','и','ам','а','ма','м')):
        print(ans)
    pass
