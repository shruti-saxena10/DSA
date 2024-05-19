#Time Complexity:-O(mn)
#Space Complexity:-O(mn)

#[[1 ,2, 3],[2,34,78],[10,13,56]]=>new array will be create after deleting new column/row

import numpy as np

arr=np.array([[1 ,2, 3],[2, 34, 78],[10, 13, 56]])
print(arr)

newarr=np.delete(arr,1,axis=0)
print(newarr)