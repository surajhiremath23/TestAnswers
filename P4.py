number =int(input())

for i in range(1,number+1):
    for j in range(1,i+1):
        print(j,end=' ')
    for j in range(i-1,0,-1):
        print(j,end=' ')
    print()