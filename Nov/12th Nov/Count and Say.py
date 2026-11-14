class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"  #first term

        for i in range(n - 1):
            newResult = []
            j = 0

            while j < len(result):
                ch = result[j]
                count = 0

                while j < len(result) and result[j] == ch:
                    count += 1  #counting consecutive digits
                    j += 1

                newResult.append(str(count))  #adding frequency
                newResult.append(ch)  #adding digit

            result = ''.join(newResult)  #creating next term

        return result


print(Solution().countAndSay(5))
