def prime(start,end):
    lst=[]
    flag=0
    if (start==0 or start==1):
        start=2
    for i in range(start,end):
        for j in range(2,i):
            if (i%j==0):
                flag=1
                break
            else:
                flag=0
            
        if (flag==0):
            lst.append(i)

    return lst

start=int(input("Enter the starting range"))
end =int(input("Enter the end range"))
lst=prime(start,end)
if len(lst)==0:
    print("No prime numbers in this range")
else:
    print("Prime numbers in this range are ",lst)