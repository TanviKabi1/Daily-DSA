class Solution(object):
    def customSort(self, order, s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1  #count frequency
        ans = []
        for ch in order:
            ans.append(ch * freq.get(ch, 0))  #follow custom order
            freq.pop(ch, None)
        for ch, count in freq.items():
            ans.append(ch * count)  #add remaining chars
        return "".join(ans)
print(Solution().customSort("cba", "abcd"))
