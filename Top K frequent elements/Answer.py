class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        counts = Counter(nums)
        
        return heapq.nlargest(k, counts, counts.get)



# Complexity Analysis

# Time complexity : O(Nlogk) if k<N and O(N) in the particular case of N=k. That ensures time complexity to be better than O(NlogN).

# Space complexity : O(N+k) to store the hash map with not more N elements and a heap with k elements.