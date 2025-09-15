class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        streak = 1
        curr_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i - 1] + 1:
                    curr_streak += 1
                else:
                    streak = max(curr_streak, streak)
                    curr_streak = 1

        return max(streak, curr_streak)