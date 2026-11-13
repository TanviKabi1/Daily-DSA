class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        i = len(s) - 1

        while i >= 0 and s[i] == ' ':  #skipping trailing spaces
            i -= 1

        while i >= 0 and s[i] != ' ':  #counting characters of last word
            count += 1
            i -= 1

        return count


print(Solution().lengthOfLastWord("Hello World"))  #5
