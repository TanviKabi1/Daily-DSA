class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        map1 = {}  #mapping characters from s to t
        map2 = {}  #mapping characters from t to s

        for i in range(len(s)):
            ch1 = s[i]
            ch2 = t[i]

            if ch1 in map1:
                if map1[ch1] != ch2:
                    return False  #checking existing mapping

            if ch2 in map2:
                if map2[ch2] != ch1:
                    return False  #checking reverse mapping

            map1[ch1] = ch2
            map2[ch2] = ch1

        return True


print(Solution().isIsomorphic("egg", "add"))
