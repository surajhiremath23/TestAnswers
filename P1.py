if __name__ == "__main__":
    num = input("Enter 5 digit number: ")
    for i in num:
        if int(i)==9:
            print(0,end='')
        else:
            print(int(i)+1,end='')