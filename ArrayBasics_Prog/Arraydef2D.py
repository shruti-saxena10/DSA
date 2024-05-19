# 2 D array definition

# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9
import numpy as np

# twoDArray=np.array([[11, 15, 10, 6],[10, 14, 11, 5],[12, 17, 12, 8],[15, 18, 14, 9]])
# print(twoDArray)

# Time Complexity:- O(mn)   m:-no. of columns  n:-no. of rows
# Space Complexity:- O(mn)   m:-no. of columns  n:-no. of rows
#------------------------------------------------------------
#Insertion a new value in 2D array
# for adding Rows and column
# Time Complexity=> O(mn)

# Day 1 - 10, 14, 11, 5
# Day 2 - 12, 17, 12, 8
# Day 3 - 15, 18, 14, 9

# twoDArray1=np.array([[10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

# twoDArray2=np.insert(twoDArray1, 2, [[1,2,3]], axis=1)
# print(twoDArray1)
# print(twoDArray2)
# new2Darray=np.append(twoDArray1, [[1,2,3,4]], axis=0)
# print(new2Darray)
#-----------------------------------------------------
#Accessing the 2 D array

# accessArray=np.array([[12, 17, 12, 8],[11, 15, 10, 6],[10, 14, 11, 5],[15, 18, 14, 9]])
# print(accessArray)

#function for access Array
# def accessElement(accessArray,noRows,noCols):
#     if noRows>=len(accessArray) or noCols>=len(accessArray[noRows]):
#         print("Invalid Element")
#     else:
#         print(accessArray[noRows][noCols])


# accessElement(accessArray,1,9)

#Time Complexity:- O(1)
#Space Complexity:- O(1)

#-------------------------------------------------------------
#Traversal array

# traversal2Darray=np.array([[2,17,12,8],[11,15,10,6],[10,14,11,5]])
# print(traversal2Darray)

# def traversal(traversal2Darray):
#     for i in range(len(traversal2Darray)):
#         for j in range(len(traversal2Darray[0])):
#             print(traversal2Darray[i][j])

# traversal(traversal2Darray)

#Time Complexity:- O(mn)
#Space Complexity:- O(1)

#--------------------------------------------
#Searching in two dimensional Array
arraySearch=np.array([[10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(arraySearch)
def Search(arraySearch,target):
    for i in range(len(arraySearch)):
        for j in range(len(arraySearch[0])):
            if arraySearch[i][j]==target:
                #return str(i)+str(j)
                #return i,j
                return [i,j]
    
    return "Element not found"
        

print(Search(arraySearch,9))

