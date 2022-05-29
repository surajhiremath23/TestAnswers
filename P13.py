
import math
import os
import random
import re
import sys


def repeatedString(s, n):
    # Write your code here
    count=0
    for i in range(len(s)):
        if s[i]=='a':
            count+=1
    num = n // len(s)
    temp= n % len(s)
    count2=0
    for i in range(temp):
        if s[i]=='a':
            count2+=1
    return (num*count+count2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()