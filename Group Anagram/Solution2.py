class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            dictionary[tuple(count)].append(s)
        return list(dictionary.values())
    





# strs = ["aabb", "baba", "cba", "bbcca"]
# dictionary = {[2, 2, 0, 0,...]:["aabb", "baba"], [1, 1, 1, 0, 0, ...]:["cba"], [1, 2, 2, 0, 0, ...]:["bbcca"]}
# the keys in the dictionary indicate 26 alphabets and each index has a number which indicates number of characters in each string in the input list