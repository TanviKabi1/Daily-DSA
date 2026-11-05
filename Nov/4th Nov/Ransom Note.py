class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        freq = {}  #storing magazine character frequencies

        for ch in magazine:
            freq[ch] = freq.get(ch, 0) + 1  #counting characters

        for ch in ransomNote:
            if ch not in freq or freq[ch] == 0:
                return False  #character is unavailable

            freq[ch] -= 1  #using one occurrence

        return True  #all characters are available
print(Solution().canConstruct("a", "b"))       # False
