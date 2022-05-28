num =  input()
for i in range(len(num)):
    if int(num[i]) == 9:
       num=num.replace(num[i],'0')
    else:
        temp=int(num[i]) + 1
        num=num.replace(num[i],str(temp))
        
print(num)