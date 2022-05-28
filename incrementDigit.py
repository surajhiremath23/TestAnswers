num =  input()
num = list(num)
for i in range(len(num)):
    if int(num[i]) == 9:
       num[i]='0'
    else:
        temp=int(num[i]) + 1
        num[i]=temp

print(*num)
