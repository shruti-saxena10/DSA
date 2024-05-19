def arms(num):
    s=num
    pow=len(str(num))
    sum=0

    while num !=0:
        r=num%10
        sum=sum+(r**pow)
        num=num//10

    if s==sum:
        print(s, "Is a Armstrong number")
    else:
        print(s, "Not a Armstrong Number")


num=int(input("Enter the number"))
arms(num)