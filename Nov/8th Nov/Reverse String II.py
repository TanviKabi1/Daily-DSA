class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        chars = list(s)  #converting string into a character list

        for i in range(0, len(chars), 2 * k):
            l = i
            r = min(i + k - 1, len(chars) - 1)  #finding the end of the section

            while l < r:
                chars[l], chars[r] = chars[r], chars[l]  #reversing first k characters
                l += 1
                r -= 1

        return ''.join(chars)  #converting list back into a string
print(Solution().reverseStr("abcdefg", 2)) 
