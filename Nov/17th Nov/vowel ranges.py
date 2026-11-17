class Solution(object):
    def vowelRanges(self, words, queries):
        pref = [0]
        vowels = "aeiou"

        for word in words:
            valid = word[0] in vowels and word[-1] in vowels
            pref.append(pref[-1] + valid)  #build prefix count

        ans = []
        for l, r in queries:
            ans.append(pref[r + 1] - pref[l])  #get range count

        return ans
print(Solution().vowelRanges(["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]]))
