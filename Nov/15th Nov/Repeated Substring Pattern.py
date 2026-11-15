class Solution(object):
    def Pattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)

        for length in range(1, n // 2 + 1):
            if n % length != 0:
                continue  #length must divide string equally

            match = True

            for i in range(length, n):
                if s[i] != s[i % length]:
                    match = False  #pattern does not repeat
                    break

            if match:
                return True  #repeated pattern found

        return False

print(Solution().Pattern("abab"))
