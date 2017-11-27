from string_algorithm import aho_corrasick

morphArr = ['мам','ами','а','ми','ам','и']

def getMorph(query):
    morphemes = aho_corrasick.find(morphArr, query)
    return(morphemes)

def
