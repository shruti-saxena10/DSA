def Fibonacci(num):
    if(num==0):
        return 0
    if(num==1):
        return 1
    else: 
        return Fibonacci(num-1)+Fibonacci(num-2)


flag=False   
def isFibonacci(num):
    for i in range(0,100):
        if(num==Fibonacci(i)):
            flag=True
            break
        else:
            flag=False
    if(flag==True):
        return "Yes"
    else:
        return "No"
num=int(input("Enter the Fibonavvi Number to be checked "))

print(isFibonacci(num))