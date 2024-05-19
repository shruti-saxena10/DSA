import numpy as np
# l1=[1,2,3]
# l2=[4,5,6]
# l3=l1+l2
# print(l3)

# l4=l1*4
# print(l4)

#---------------------
# #len() function
# l5=[1,2,3,4,5,12,14]
# print(len(l5))

# #---------------------
# print(max(l5))
# print(min(l5))
# print(sum(l5))
# average=sum(l5)/len(l5)
# print(average)



# def average():
#     total=0
#     count=0
#     while(True):
#         inp=input("Enter the number :")
#         if inp=="done":break
#         value=float(inp)
        
#         total=total+value
#         count=count+1
        
#         avg=total/count
#     print("Average is ",avg)

# average()

#converting into List

# mylistavg=list()
# while(True):
#     inp=input("Enter the numbers in the list")
#     if inp=="done": break
#     value=float(inp)
#     mylistavg.append(value)
# avlist=sum(mylistavg)/len(mylistavg)
# print(avlist)


# def avgmethod2(l1):
#     totalsum2=0
#     count2=0
#     for element in l1:
#         totalsum2=totalsum2+element
#     avmethod2=totalsum2/len(l1)
#     return avmethod2

# l1=[]
# n=int(input("Enter the no of elements :"))
# for i in range(0,n):
#     ele=int(input())
#     l1.append(ele)

# print(avgmethod2(l1))


#---------------------------
#List from string

# a='spam-spam-spam'
# print(a)
# delimiter='-'
# b=a.split(delimiter)
# print(b)
# print(delimiter.join(b))

#---------Pitfalls of List and how to avid them
mylist=[1,2,3,4,0,-1]
# #mylist.append(10)
# mylist=mylist+[10]
# print(mylist)

# orig=mylist
# print(orig)
# mylist.sort()
# print(mylist)

#Difference Array vs List
# myList1=[4,6,8,10]
# myarray1=np.array([4,6,8,10])
# print([myarray1/2])
# #print(myList1/2){Not possible}

myArray2=np.array([1,2,3,4,5,6,'a'])
myList2=[1,2,3,4,5,6,'a']
print(myArray2)
print(myList2)








