array = [4,3,1,2,3,4,5]
minValue = None
for elem in array:
    if (minValue == None):
        minValue = elem
    else:
        minValue = min(minValue,elem)
print(minValue) 