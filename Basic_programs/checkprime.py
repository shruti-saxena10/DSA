#Given a positive integer N, The task is to write a Python program to check if the number is Prime or not in Python.

#Examples: 

#Input:  n = 11
#Output: True
#Input:  n = 1
#Output: False


def Prime(num):
    isPrime=False
    flag=0

    for i in range(2,num):
        if (num%i==0):
            flag=1
            break
        else:
            flag=0

    if (flag!=0 or num==0 or num==1):
        isPrime=False
        print(isPrime)
    
    else:
        isPrime=True
        print(isPrime)

num=int(input("Enter the positive integer N"))
Prime(num)