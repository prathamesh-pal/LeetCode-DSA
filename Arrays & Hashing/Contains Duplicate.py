# Given an integer array nums, 
# return true if any value appears at least twice in the array, 
# and return false if every element is distinct.


nums = [1,2,3,1]

def chackDuplicate(nums):
    Distinct = set()
    for num in nums:
        if num in Distinct:
            return True
        Distinct.add(num)
    return False

print(chackDuplicate(nums))