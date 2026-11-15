class Solution(object):
    def Prefixword(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        words = sentence.split()  #splitting sentence into words

        for i in range(len(words)):
            word = words[i]

            if len(searchWord) <= len(word):
                match = True

                for j in range(len(searchWord)):
                    if word[j] != searchWord[j]:
                        match = False  #characters do not match
                        break

                if match:
                    return i + 1  #returning 1-based word position

        return -1  #prefix not found

print(Solution().Prefixword("i love eating burger", "burg"))
