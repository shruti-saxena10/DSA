import array as arr

arr1=arr.array('i',[1,2,3,4,5,6])
tar=0


def LinearSearch(arr,target):
    

    for i in range(len(arr)):
        
        if arr[i]==target:
            return i
    return -1

print(LinearSearch(arr1,tar))
#Time Complexity=O(N)
#Space Complexity=>O(1)
