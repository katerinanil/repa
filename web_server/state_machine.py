from itertools import product
from aho_rec import aho

class MorphSM:
    Start = 'Start'
    Pr = 'Pr'
    R_n = 'R_n'
    R_v = 'R_v'
    I = 'I'
    Si = 'Si'
    So_v = 'So_v'
    So_n = 'So_n'
    F_a = 'F_a'
    F_v = 'F_v'
    F_n = 'F_n'
    Ps = 'Ps'
    Zf = 'Zf'
    End = 'End'
    
    #rule dict
    Graph = {
                Start : { Pr, R_n, R_v },
                Pr : { Pr, R_n, R_v },
                R_n : { I, Si, So_n, F_n, End },
                R_v : { I, Si, So_v, F_v, End },
                I : { Pr, R_n, R_v },
                Si : { Si, F_n, F_v, F_a, End },
                So_v : { Si, So_v, F_v, End },
                So_n : { Si, So_n, F_n, End },
                F_n : { Ps, End },
                F_v : { Ps, End },
                F_a : { Ps, End },
                Ps : { End },
                            
            }
    
    """making acceptable combos
    according to rule dict"""
    @staticmethod
    def check(path):
        curr = MorphSM.Start
        for t in path:
            if t in MorphSM.Graph[curr]:
                curr = t
            else: return False
        return True

morphs = { 'князь' : {MorphSM.R_n}, 'княз' : {MorphSM.R_n},'я' : {MorphSM.F_n},
           'ю' : {MorphSM.F_n},'ями' : {MorphSM.F_n},'под' : {MorphSM.Pr},
           'при' : {MorphSM.Pr},'ех' : {MorphSM.R_v},'л' : {MorphSM.Si,},
           'по' : {MorphSM.Pr},'на' : {MorphSM.Pr}, 'а' : {MorphSM.So_v, MorphSM.F_n, MorphSM.F_v},
           'смотр' : {MorphSM.R_n, MorphSM.R_v}, 'е' : {MorphSM.So_v, MorphSM.F_n},
           'вш' : {MorphSM.R_n, MorphSM.Si}, 'ий' : {MorphSM.F_a},'ся' : {MorphSM.Ps},
           'на' : {MorphSM.Pr}, 'по' : {MorphSM.Pr}, 'над' : {MorphSM.Pr}, 'в' : {MorphSM.Pr},
           'ех' : {MorphSM.R_v},'из' : {MorphSM.Pr}, 'под' : {MorphSM.Pr}, 'мам' : {MorphSM.R_n},
           'ами' : {MorphSM.F_n}, 'ам' : {MorphSM.F_n},'ми' : {MorphSM.R_n, MorphSM.F_n,},
           'и' : {MorphSM.F_n, MorphSM.F_v, MorphSM.So_v,}, 'ть' : {MorphSM.F_v,}, 'ит' : {MorphSM.F_v,},
           'ишь' : {MorphSM.F_v,},'им' : {MorphSM.F_v,},'ите' : {MorphSM.F_v,},'ят' : {MorphSM.F_v,}}


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
                    if p[i] not in {MorphSM.Si, MorphSM.So_v, MorphSM.F_v, MorphSM.F_n, MorphSM.F_a}:
                        st += ans[i][1]
                yield st
                
if __name__ == '__main__':
    for c in getCombo('мамами', morphs):
        print(c)
