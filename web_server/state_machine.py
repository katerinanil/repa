from itertools import product
from aho_rec import aho

class MorphSM:
    Start = 'Start'
    Pr = 'Pr'
    R = 'R'
    I = 'I'
    S = 'S'
    F = 'F'
    Ps = 'Ps'
    End = 'End'
    Graph = {
                Start : { Pr, R },
                Pr : { Pr, R },
                R : { I, S, F, End },
                I : { Pr, R },
                S : { S, F, End },
                F : { Ps, End },
                Ps : { End },
            }
    @staticmethod
    def check(path):
        curr = MorphSM.Start
        for t in path:
            if t in MorphSM.Graph[curr]:
                curr = t
            else: return False
        return True

morphs = { 'po' : {MorphSM.Pr, MorphSM.R}, 'na' : {MorphSM.Pr}, 'smotr' : {MorphSM.R}, 'e' : {MorphSM.S, MorphSM.F},
           'vsh' : {MorphSM.R, MorphSM.S}, 'iy' : {MorphSM.F}, 'sya' : {MorphSM.Ps} }

def making_combo(word, morphs):
    for ans in aho(word, morphs.keys()):
        #list of sets of morph types for every morph in combo
        lst = [morphs[sub] for i, sub in ans]
        #p is potentional path in graph
        for p in product(*lst):
            #if path is acceptable
            if MorphSM.check(p):
                st = ''
                for i in range(len(ans)):
                    st += ans[i][1] + ' ' + p[i] + ', '
                yield st

if __name__ == '__main__':
    for c in making_combo('ponasmotrevshiysya', morphs):
        print(c)
    
