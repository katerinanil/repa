from itertools import chain
def sort(*lists): return sorted(chain(*lists))

if __name__ == '__main__':  
    for s in sort([1,5,6,9,90],[90,800],[1.1,5]):
        print(s)