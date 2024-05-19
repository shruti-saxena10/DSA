# previous_list=[1,2,3,5,7]
# # new_list=[i*2 for i in previous_list]
# # print(new_list)

# n_list=[]
# for i in previous_list:
#     new_ele=i*2
#     n_list.append(new_ele)
# print(n_list)

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]
 
    for row in m:
        for element in row:
            if v < element: v = element
 
    return v
print(fun(data[0]))