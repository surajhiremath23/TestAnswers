Str = input()

i=0
j=1
count=0
def trim(temp,i,j):
    a = temp[0:i]
    n=len(temp)
    b= temp[j:n]
    temp = a+b
    print(temp)
    # return temp

for k in range(len(Str)-2):
    if Str[i] != Str[j]:
        if count >= 2:
            trim(Str,i,j)
            i=i-1
            j=j+1
            print(i,j)
            count = 0
    if Str[i] == Str[j] :
        count += 1
        j +=1
    else:
        i+=1
        j+=1 
