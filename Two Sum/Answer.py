class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashTable:
                return [hashTable[difference], i]
            else:
                hashTable[nums[i]] = i