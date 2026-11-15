class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""  #empty input

        prefix = strs[0]  #first word as reference

        for i in range(1, len(strs)):
            word = strs[i]
            j = 0  #starting index

            while j < len(prefix) and j < len(word) and prefix[j] == word[j]:
                j += 1  #checking matching characters

            prefix = prefix[:j]  #updating common prefix

            if prefix == "":
                return ""  #no common prefix

        return prefix

print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
