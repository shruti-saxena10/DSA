from array import *


arr1=array('i',[1,23,454,7778,8888])

def accessElement(array,index):
    if(index>len(array)):
        print("there are no elements in the array")
    else:
        print(array[index])

accessElement(arr1,9)

#Time complexity:-O(1)
#Space complexity:-O(1)