myList=[1,15,16,17,19,20,34]

# def Search(myList,target):
#     for i in range(len(myList)):
#         if myList[i]==target:
#             return i
    
#     return "Element not found"

# result=Search(myList,10)
# print(result)

#Using in operator
# def Search1(myList,target):
#     if target in myList:
#         return f"{target} is in the list " #Time Complexity:- O(n)
#     else:
#         return f"{target} not found"

# result1=Search1(myList,34)
# print(result1)

def Search2(myList,target):
    for i,value in enumerate(myList): #enumerate function=>keeps track of index
        if value==target:             #Time Complexity:-O(N) and Space Complexity:-O(1)
            return i
    return -1


result2=Search2(myList,10)
print(result2)