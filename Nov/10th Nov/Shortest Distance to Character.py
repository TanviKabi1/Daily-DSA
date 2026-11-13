class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        res = []
        prev = -len(s)  #initializing previous character position

        for i in range(len(s)):
            if s[i] == c:
                prev = i  #updating previous occurrence
            res.append(i - prev)  #storing distance from left occurrence

        prev = 2 * len(s)

        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                prev = i  #updating next occurrence
            res[i] = min(res[i], prev - i)  #keeping minimum distance

        return res


print(Solution().shortestToChar("loveleetcode", "e"))  #[3,2,1,0,1,0,0,1,2,2,1,0]
