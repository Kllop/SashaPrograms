array = [3,5,1,7,4]
i = 0
newarray = []
while (len(array)):
    minValue = None
    for elem in array:
        if (minValue==None):
            minValue = elem
        else:
            minValue = min(minValue, elem)
    newarray.append(minValue)
    array.remove(minValue)
    i = i+1
print (newarray)
