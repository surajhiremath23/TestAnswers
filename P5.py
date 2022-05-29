def findPrime(num):
    if num < 2:
        return 0
    else:
        for i in range(2, num//2):
            if num % i == 0:
                return 0
        return num


def getPrimeNumbers(lowerBond, upperBond):
    for i in range(lowerBond, upperBond+1):
        temp = findPrime(i)
        if temp == 0:
            pass
        else:
            print(temp,end=' ')
    pass


if __name__ == '__main__':
    lowerBond= int(input("Enter the lower bound value:"))
    upperBond = int(input("Enter the upper bound value:"))
   
    getPrimeNumbers(lowerBond, upperBond)
