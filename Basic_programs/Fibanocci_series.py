
def Fibonnaci(num):
    if(num<0):
        print("Incorrect Input")
    if(num==0):
        return 0
    if(num==1):
        return 1
    if(num>=2):
        return Fibonnaci(num-1)+Fibonnaci(num-2)
    
num=int(input("Enter the fibonacci nth number "))
print(Fibonnaci(num))