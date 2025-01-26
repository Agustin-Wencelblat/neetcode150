# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Primera solucion: O(nlogn) tiempo y O(n) espacio
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
      
#Solucion mejorada: O(n) tiempo y O(n) espacio
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
         
