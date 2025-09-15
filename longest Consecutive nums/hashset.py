class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        heap = set(nums)

        streak = 1
        curr_streak = 1

        for num in heap:
            if nums - 1 not in heap:
                curr_streak = 1
                curr_num = num

                while num + 1 in heap:
                    curr_streak += 1
                    curr_num += 1

                streak = max(streak, curr_streak)


        return streak      