

n=int(input("How many day's temperature? "))

arr=[]
for i in range(0, n):
    ele=int(input(f"Day {i}'s high temp: "))
    arr.append(ele)
print(arr)

def average(arr, n):
    sum=0
    for i in arr:
        sum+=i
        avg=sum/n
    return avg  

res=average(arr,n)
print(res)

count=0
for i in arr:
    if i > res:
        count+=1
    
print(count,"day(s) above average")
    