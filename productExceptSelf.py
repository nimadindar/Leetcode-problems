
"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
# My non-efficient Answer with time complexity of O(mn)

def productExceptSelf(nums):

    result = [1] * len(nums)
    for i in range(len(nums)):
        new_nums = nums[:i] + nums[i+1:]
        product = 1
        for j in range(len(new_nums)):
            product *= new_nums[j]
        result[i] *= product
    return result
  
  # Efficient answer with Time complexity O(n)
  
  def productExceptSelf(nums):

    result = [1] * len(nums)

    prefix = 1 
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
        
    return result
  
  
