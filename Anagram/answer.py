class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s:
            if i in t:
                t = t.replace(i, "", 1)
            else:
                return False
        print(t)
        if t:
            return False
        else:
            return True