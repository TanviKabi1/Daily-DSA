class Solution(object):
    def ana(self, s, p):
        ans = []
        m = len(p)

        if m == 0 or m > len(s):
            return ans

        need = {}
        window = {}

        for ch in p:
            need[ch] = need.get(ch, 0) + 1  #count pattern characters

        for i in range(len(s)):
            ch = s[i]
            window[ch] = window.get(ch, 0) + 1  #add character

            if i >= m:
                old = s[i - m]
                window[old] -= 1  #remove outgoing character

                if window[old] == 0:
                    del window[old]

            if i >= m - 1 and window == need:
                ans.append(i - m + 1)  #store anagram index

        return ans

print(Solution().ana("cbaebabacd", "abc"))
