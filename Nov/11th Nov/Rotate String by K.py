class Solution(object):
    def rotateStringByK(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)

        if n == 0:
            return s

        k = k % n  #handling rotations greater than string length

        result = []

        for i in range(n):
            newPos = (i - k) % n  #finding original position after right rotation
            result.append(s[newPos])

        return ''.join(result)


print(Solution().rotateStringByK("abcdef", 2))  #"efabcd"
