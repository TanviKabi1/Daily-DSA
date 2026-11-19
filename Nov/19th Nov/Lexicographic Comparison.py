class Solution(object):
    def isSmaller(self, s, t):
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                return s[i] < t[i]  #compare first difference
        return len(s) < len(t)  #shorter prefix is smaller
print(Solution().isSmaller("apple", "banana"))
