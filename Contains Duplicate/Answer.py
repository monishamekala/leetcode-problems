class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = []
        for i in nums:
            if i in dup:
                return True
            else:
                dup.append(i)
        return False