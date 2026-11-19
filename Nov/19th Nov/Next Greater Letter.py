class Solution(object):
    def nextLetter(self, letters, target):
        l, r = 0, len(letters)
        while l < r:
            mid = (l + r) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid  #search left half
        return letters[l % len(letters)]
print(Solution().nextLetter(["c", "f", "j"], "a"))
