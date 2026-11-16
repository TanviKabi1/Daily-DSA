class Solution(object):
    def longSub(self, s):
        charIndex = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            ch = s[right]

            if ch in charIndex and charIndex[ch] >= left:
                left = charIndex[ch] + 1  #skip duplicate

            charIndex[ch] = right  #update character position
            ans = max(ans, right - left + 1)  #update max length

        return ans

print(Solution().longSub("abcabcbb"))
