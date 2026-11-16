class Solution(object):
    def charRep(self, s, k):
        freq = {}
        left = 0
        maxFreq = 0
        ans = 0

        for right in range(len(s)):
            ch = s[right]
            freq[ch] = freq.get(ch, 0) + 1  #add character
            maxFreq = max(maxFreq, freq[ch])  #track highest frequency

            while (right - left + 1) - maxFreq > k:
                leftChar = s[left]
                freq[leftChar] -= 1  #remove left character
                left += 1  

            ans = max(ans, right - left + 1)  #update max length

        return ans

print(Solution().charRep("AABABBA", 1))
