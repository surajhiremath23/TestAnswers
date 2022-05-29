Str = input()

i = 0
j = 1
count = 0


def trim(temp, i, j):
    a = temp[0:i]
    n = len(temp)
    b = temp[j:n]
    temp = a+b
    print(temp)
    return temp


for k in range(len(Str)-1):
    if Str[i] != Str[j] or j >= len(Str)-1:
        if count >= 2:
            Str = trim(Str, i, j)
            i = i-1
            # print(j)
            j = j-count-1
            if i< 0:
                i=0
                j=1
            # print(i,j)
            count = 0
    if j > len(Str)-1:
        pass
    else:
        if Str[i] == Str[j]:
            count += 1
            if j > len(Str)-1:
                pass
            else:
                j += 1
        else:
            i += 1
            if j >len(Str)-1:
                pass
            else:
                j += 1
print(Str)
