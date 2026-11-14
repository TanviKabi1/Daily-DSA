class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        write = 0

        while i < len(chars):
            ch = chars[i]  #storing current character
            count = 0

            while i < len(chars) and chars[i] == ch:
                count += 1  #counting consecutive occurrences
                i += 1

            chars[write] = ch  #writing character
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit  #writing count digits
                    write += 1

        return write


chars = list("aabbccc")
print(Solution().compress(chars))
