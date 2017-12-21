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
    End = 'End'
    
    #rule dict
    Graph = {
                Start : { Pr, R },
                Pr : { Pr, R },
                R : { I, Si, So, F, End },
                I : { Pr, R },
                Si : { Si, F, End },
                So : { Si, So, F, End },
                F : { Ps, End },
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

morphs = { 'по' : {MorphSM.Pr, MorphSM.R}, 'на' : {MorphSM.Pr}, 'а' : {MorphSM.So, MorphSM.F}, 'смотр' : {MorphSM.R}, 'е' : {MorphSM.So, MorphSM.F},
           'вш' : {MorphSM.R, MorphSM.Si}, 'ий' : {MorphSM.F}, 'ся' : {MorphSM.Ps} }

def getCombo(word, morphs):
    #ans - com
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
    for c in getCombo('понасмотревшийся', morphs):
        print(c)
