class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if (len(nums) > 0) & (len(set(nums)) != len(nums)):
            return True
        else:
            return False