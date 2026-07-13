class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for idx, val in enumerate(nums):
            if val in dic:
                return True
            dic[val] = idx
        return False