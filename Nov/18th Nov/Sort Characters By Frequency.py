class Solution(object):
    def sortFreq(self, s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1  #count frequency
        arr = self.mergeSort([[ch, n] for ch, n in freq.items()])
        return "".join(ch * n for ch, n in arr)
    def mergeSort(self, a):
        if len(a) <= 1:
            return a
        m = len(a) // 2
        l, r = self.mergeSort(a[:m]), self.mergeSort(a[m:])
        ans = []
        i = j = 0
        while i < len(l) and j < len(r):
            if l[i][1] >= r[j][1]:
                ans.append(l[i])
                i += 1
            else:
                ans.append(r[j])
                j += 1
        return ans + l[i:] + r[j:]
print(Solution().sortFreq("tree"))
