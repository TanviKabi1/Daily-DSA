class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()  #splitting sentence into words

        if len(pattern) != len(words):
            return False

        map1 = {}  #mapping pattern characters to words
        map2 = {}  #mapping words to pattern characters

        for i in range(len(pattern)):
            ch = pattern[i]
            word = words[i]

            if ch in map1 and map1[ch] != word:
                return False  #checking character mapping

            if word in map2 and map2[word] != ch:
                return False  #checking word mapping

            map1[ch] = word
            map2[word] = ch

        return True


print(Solution().wordPattern("abba", "dog cat cat dog"))
