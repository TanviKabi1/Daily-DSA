class Codec(object):

    def encode(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = []

        for word in strs:
            result.append(str(len(word)) + "#" + word)  #storing length followed by word

        return ''.join(result)

    def decode(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1  #finding the separator

            length = int(s[i:j])  #reading word length
            word = s[j + 1:j + 1 + length]  #extracting the word

            result.append(word)
            i = j + 1 + length  #moving to next encoded word

        return result


codec = Codec()
print(codec.decode(codec.encode(["hello", "world"])))
