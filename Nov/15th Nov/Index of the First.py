class Solution(object):
    def Statement(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)

        if m == 0:
            return 0  #empty needle

        for i in range(n - m + 1):
            match = True

            for j in range(m):
                if haystack[i + j] != needle[j]:
                    match = False  #mismatch found
                    break

            if match:
                return i  #first matching index

        return -1  #needle not found

print(Solution().Statement("sadbutsad", "sad"))
