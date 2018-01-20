from itertools import product
from aho_rec import aho

class MorphSM:
    Start = 'Start'
    Pr = 'Pr'
    R = 'R'
    I = 'I'
    Si = 'Si'
    So = 'So'
    F = 'F'
    Ps = 'Ps'
    Zf = 'Zf'
    End = 'End'
    
    #rule dict
    Graph = {
                Start : { Pr, R },
                Pr : { Pr, R },
                R : { I, Si, So, F, Zf, End },
                I : { Pr, R },
                Si : { Si, F, Zf, End },        #without
                So : { Si, So, F, Zf, End },
                F : { Ps, End },                #without
                Zf : { Ps, End },
                Ps : { End },
            }
    
    """making acceptable combos
    according to rule dict"""
    def check(path):
        curr = MorphSM.Start
        for t in path:
            if t in MorphSM.Graph[curr]:
                curr = t
            else: return False
        return True

def getCombo(word, morphs):
    #ans - combo
    for ans in aho(word, morphs.keys()):
        #list of sets of morph types for every morph in combo
        lst = [morphs[sub] for i, sub in ans]
        #p is potentional path in graph
        for p in product(*lst):
            #if path is acceptable
            if MorphSM.check(p):
                st = ''
                for i in range(len(ans)):
                    if p[i] != MorphSM.Si and p[i] != MorphSM.F:
                        st += ans[i][1]
                yield st

#if __name__ == '__main__':
#    for c in getCombo('понасмотревшийся', morphs):
#        print(c)
