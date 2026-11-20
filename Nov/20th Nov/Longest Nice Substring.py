class Solution(object):
    def longestNice(self, s):
        ans = ""
        for i in range(len(s)):
            lower = set()
            upper = set()
            for j in range(i, len(s)):
                ch = s[j]
                if ch.islower():
                    lower.add(ch)  #store lowercase
                else:
                    upper.add(ch)  #store uppercase
                if {c.upper() for c in lower} == upper and j - i + 1 > len(ans):
                    ans = s[i:j + 1]  #save longest nice substring
        return ans

print(Solution().longestNice("YazaAay"))
