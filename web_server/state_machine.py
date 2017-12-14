from string_algorithms import aho_corrasick, naive_find

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
    Graph = {
                Start : { Pr, R },
                Pr : { Pr, R },
                R : { I, S, F, End },
                I : { Pr, R },
                S : { S, F, End },
                F : { Ps, End },
                Ps : { End },
            }
    def __init__(self, sub, morphs):

        return super().__init__(**kwargs)

    #@staticmethod
    #def can_move(

#morphs = {'a' : }