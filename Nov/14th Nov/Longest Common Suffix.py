class Solution(object):
    def longestCommonSuffix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""  #empty input

        suffix = strs[0]  #first word as reference

        for i in range(1, len(strs)):
            word = strs[i]
            j = 1  #starting from the last character

            while j <= len(suffix) and j <= len(word) and suffix[-j] == word[-j]:
                j += 1  #checking matching characters backwards

            suffix = suffix[len(suffix) - j + 1:]  #updating common suffix

            if suffix == "":
                return ""  #no common suffix

        return suffix

print(Solution().longestCommonSuffix(["running", "jogging", "walking"]))
