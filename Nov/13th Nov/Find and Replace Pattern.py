class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        result = []

        for word in words:
            if len(word) != len(pattern):
                continue

            map1 = {}  #mapping pattern characters to word characters
            map2 = {}  #mapping word characters to pattern characters
            match = True

            for i in range(len(pattern)):
                ch1 = pattern[i]
                ch2 = word[i]

                if ch1 in map1 and map1[ch1] != ch2:
                    match = False
                    break  #pattern mapping does not match

                if ch2 in map2 and map2[ch2] != ch1:
                    match = False
                    break  #reverse mapping does not match

                map1[ch1] = ch2
                map2[ch2] = ch1

            if match:
                result.append(word)  #adding matching word

        return result


print(Solution().findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))
