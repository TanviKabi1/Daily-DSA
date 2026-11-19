class Solution(object):
    def longestWord(self, s, dictionary):
        ans = ""
        for word in dictionary:
            i = j = 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1  #match character
                i += 1
            if j == len(word):
                if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                    ans = word  #choose longest, then smallest
        return ans
print(Solution().longestWord("abpcplea", ["ale", "apple", "monkey", "plea"]))
