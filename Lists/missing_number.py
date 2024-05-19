#Sn=n/2*(2*a+(n-1)*d)
def missing_number(arr, n):
    Sn=(n)/2*(2+(n-1))
    sum=0
    for i in arr:
        sum+=i
    
    ele=Sn-sum
    return ele
    
    
print(missing_number([1,2,3,4,5,7],7))