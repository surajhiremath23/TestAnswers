arr=list(map(int,input().split()))
n = len(arr)
arr.sort()
Darr= arr[n//2:n]
Darr.sort()
print(*arr[0:n//2],*Darr[::-1])
