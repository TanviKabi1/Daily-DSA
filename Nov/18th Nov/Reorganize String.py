class Solution(object):
    def reorganize(self, s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1  #count frequency
        arr = self.mergeSort([[ch, n] for ch, n in freq.items()])
        n = len(s)
        if arr[0][1] > (n + 1) // 2:
            return ""  #check possibility
        ans = [""] * n
        i = 0
        for ch, count in arr:
            for _ in range(count):
                if i >= n:
                    i = 1  #switch to odd positions
                ans[i] = ch
                i += 2
        return "".join(ans)
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
print(Solution().reorganize("aab"))
