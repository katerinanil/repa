from state_machine import MorphSM

morphs = { 'князь' : {MorphSM.R}, 'княз' : {MorphSM.R},'я' : {MorphSM.F},
           'ю' : {MorphSM.F},'ями' : {MorphSM.F},'под' : {MorphSM.Pr},
           'при' : {MorphSM.Pr},'ех' : {MorphSM.R},'а' : {MorphSM.So, MorphSM.F},
           'л' : {MorphSM.Si}, 'по' : {MorphSM.Pr, MorphSM.R},
           'на' : {MorphSM.Pr}, 'а' : {MorphSM.So, MorphSM.F},
           'смотр' : {MorphSM.R}, 'е' : {MorphSM.So, MorphSM.F},
           'вш' : {MorphSM.R, MorphSM.Si}, 'ий' : {MorphSM.F},
           'ся' : {MorphSM.Ps}, 'на' : {MorphSM.R}, 'по' : {MorphSM.R},
           'над' : {MorphSM.R}, 'в' : {MorphSM.R}, 'ех' : {MorphSM.R},
           'из' : {MorphSM.R}, 'под' : {MorphSM.R} }
