# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


#--------------Time Complexity:-O(N*N)
# class Solution(object):
#     def twoSum(self, nums, target):
#         # """
#         # :type nums: List[int]
#         # :type target: int
#         # :rtype: List[int]
#         # """

        
#         for i in range(0,len(nums)-1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []
# class main:
#     s=Solution()
#     nums=[2,7,10,11]
#     target=9
#     print(s.twoSum(nums,target))
x=('Shruti','Vaibhav','Renu')
print(x)
y=enumerate(x)
a=list(y)
print(a)