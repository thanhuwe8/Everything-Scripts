# Questions

'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

nums = [1,2,3,1]
output = True
'''

# SUBMISSION

nums = [1,2,3,1]

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        ThisHash = {}
        for value in nums: # O(n)
            ThisHash[value] = 1 + ThisHash.get(value, 0)
        
        counter = False
        for i, value in ThisHash.item(): # O(n)
            if value != 1:
                counter = True
                break
        
        return counter


# SOLUTIONS

# Approach 1: Brute Force
'''
- Check element with every other element in the array to check for duplicates. If any duplicates are found, return True
- Complexity of O(n^2)

'''

class Solution:
    def containDuplicate(self, nums:list[int]) -> bool:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
        return False


# Approach 2: Sorting
'''
- Sort the array in ascending order and then checks
- Sorting has the complexity of O(nlogn) and O(n) to find the duplicate -> O(nlogn)

'''

class Solution:
    def containsDuplicate(self, nums:list[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                return True
        return False


# Approach 3: Hashset 
'''
- loop through the array and add element to a set (cannot contain a duplicate)
- Sorting has the complexity of O(nlogn)
'''

class Solution:
    def containsDuplicate(self, nums:list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False



# Approach 4: hash table

# Reduce the amount of loop as the code terminates when there is duplicated value found
class Solution:
    def containsDuplicate(self, nums:list[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num, 0) + 1


'''

useful link: https://leetcode.com/problems/contains-duplicate/solutions/3672475/4-method-s-c-java-python-beginner-friendly/?submissionId=1200150124
Related problems:


----------------------------------------------------------------------------
Two Sum
Roman to Integer
Palindrome Number
Maximum Subarray
Remove Element
Contains Duplicate
Add Two Numbers
Majority Element
Remove Duplicates from Sorted Array

'''





















