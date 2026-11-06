class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        freq = {}  #storing frequencies from the first word

        for ch in words[0]:
            freq[ch] = freq.get(ch, 0) + 1

        for word in words[1:]:
            current = {}  #storing frequencies of the current word

            for ch in word:
                current[ch] = current.get(ch, 0) + 1

            for ch in freq:
                if ch in current:
                    freq[ch] = min(freq[ch], current[ch])  #keeping common frequency
                else:
                    freq[ch] = 0  #character is not common

        result = []

        for ch in freq:
            for i in range(freq[ch]):
                result.append(ch)  #adding repeated common characters

        return result


print(Solution().commonChars(["bella", "label", "roller"]))
