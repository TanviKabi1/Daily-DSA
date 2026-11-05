class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        freq = {}  #storing stone frequencies

        for ch in stones:
            freq[ch] = freq.get(ch, 0) + 1  #counting stones

        count = 0

        for ch in jewels:
            count += freq.get(ch, 0)  #adding the number of matching stones

        return count


print(Solution().numJewelsInStones("aA", "aAAbbbb"))  
