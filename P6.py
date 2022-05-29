num = int(input())
arr = []

for i in range(num):
    arr.append(input())

myDict = {}
j = 1

for i in arr:
    if i[0] in myDict:
        myDict[i[0] + str(j)] = i
        j += 1
    else:
        myDict[i[0]] = i
        
myDict = sorted(myDict.items())
myDict = dict(myDict)
[print(val) for val in myDict.values()]