from collections import Counter
import heapq

def topKFrequent(k, nums):
    if k == len(nums):
        return nums
    counts = Counter(nums)
    print(counts)
    for key, freq in counts.items():
        print(key, ":", freq)
    return heapq.nlargest(k, counts, counts.get)


nums = [2,3,4,4,4,5,6,7,7,7,7,7]
print(topKFrequent(3, nums))