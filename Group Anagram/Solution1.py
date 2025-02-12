class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = collections.defaultdict(list)
        for s in strs:
            dictionary[tuple(sorted(s))].append(s)
        return list(dictionary.values())

# Sort each string s in strs 
# all the anagram strings will be equal
# all such same strings will be in single list
# dictionary = {(abt):["bat"],(ant):["nat","tan"],(aet):["ate","eat","tea"]}



# Time Complexity: O(NKlogK), where N is the length of strs, and K is the maximum length of a string in strs. The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(KlogK) time.

# Space Complexity: O(NK), the total information content stored in ans.