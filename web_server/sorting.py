import math

def sort(*arrays):
    listOfIndeces = [] #list of indices of minimal elements
    listMinEl = [] #list of current minimal elements
    length = 0 #length of all elements in all lists
    for ar in arrays:
        length += len(ar)
        listOfIndeces.append(0) #append 0 for every list
        listMinEl.append(ar[0]) #append first element of every list
    for i in range(length):
        minimum = min(listMinEl) #minimal element
        pos = listMinEl.index(minimum) #its position
        listOfIndeces[pos] +=1
        ar = arrays[pos] #list number pos
        print("---------", "\n", "позиция массива из запроса =", pos, "| сам массив =", ar)
        if listOfIndeces[pos] < len(ar):
            listMinEl[pos] = ar[listOfIndeces[pos]] #replace yielded element with the following
        else:
            listMinEl[pos] = float("inf") #if all elements in the arr are out,
                                    #we replace them with positive infinity
        yield minimum
      
#def sort(*lists):
#	indicies = [0] * len(lists)
#	minI = -1
#	for i in range(1, len(lists)):
#		if minI == -1 and len(lists[i]) > indicies[i]:
#			pass
#		if lists[i][indicies[i]] < lists[i][indicies[minI]]:
#			minI = i

if __name__ == '__main__':  
    for s in sort([1,5,6,9,90],[90,800],[1.1,5]):
        print(s)
#что если входной список пуст