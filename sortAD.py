arr=list(map(int,input().split()))
n = len(arr)
Aarr= arr[0:n//2]
Darr= arr[n//2:n]
Aarr.sort()
Darr.sort()
print(*Aarr,*Darr[::-1])