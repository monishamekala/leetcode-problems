class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        streak = 0
        curr_streak = 1

        for i in nums:
            curr = i
            curr_streak = 1

            while curr + 1 in nums:
                curr_streak += 1
                curr += 1

            streak = max(streak, curr_streak)

        return streak