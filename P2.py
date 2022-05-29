if __name__ == "__main__":
    num = input("Enter a four digit number: ")
    j=3
    for i in num:
        i=int(i)
        print('{}*{}={}'.format(i,10**j,i*10**j))
        j-=1