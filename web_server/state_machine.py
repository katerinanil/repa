from itertools import product
from aho_rec import aho

class MorphSM:
    Start = 0
    Pr = 1
    R = 2
    I = 3
    S = 4
    F = 5
    Ps = 6
    End = 7
    Fail = 8
    StateNames = {
                    Start : 'Start',
                    Pr : 'Pr',
                    R : 'R',
                    I : 'I',
                    S : 'S',
                    F : 'F',
                    Ps : 'Ps',
                    End : 'End',
                    Fail : 'Fail'
                 }
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
        else: return True
        return False

morphs = { 'a' : {MorphSM.Pr}, 'b' : {MorphSM.R, MorphSM.S}, 'c' : {MorphSM.Ps} }

if __name__ == '__main__':
    for ans in aho(morphs.keys(), 'abc'):
        lst = [morphs[sub] for i, sub in ans]
        ps = product(*lst)
        for p in ps:
            if MorphSM.check(p):
                for i in range(len(ans)):
                    print(ans[i][0], ans[i][1], MorphSM.StateNames[p[i]], ', ', end='')
                print()
