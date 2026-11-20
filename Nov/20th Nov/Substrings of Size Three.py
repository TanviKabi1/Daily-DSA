class Solution(object):
    def countGood(self, s):
        ans = 0
        freq = {}
        for right in range(len(s)):
            ch = s[right]
            freq[ch] = freq.get(ch, 0) + 1  #add new char
            if right >= 3:
                old = s[right - 3]
                freq[old] -= 1  #remove char outside window
                if freq[old] == 0:
                    del freq[old]
            if right >= 2 and len(freq) == 3:
                ans += 1  #all three chars are distinct
        return ans

print(Solution().countGood("aababcabc"))
