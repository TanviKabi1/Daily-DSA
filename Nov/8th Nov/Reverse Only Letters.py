class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)  #converting string into a list

        l = 0
        r = len(chars) - 1

        while l < r:
            if not chars[l].isalpha():  #skipping non-letter characters
                l += 1
            elif not chars[r].isalpha():  #skipping non-letter characters
                r -= 1
            else:
                chars[l], chars[r] = chars[r], chars[l]  #swapping letters
                l += 1
                r -= 1

        return ''.join(chars)  #joining characters into a string
print(Solution().reverseOnlyLetters("ab-cd"))      
