class Solution(object):
    def minWindow(self, s, t):
        if not s or not t or len(t) > len(s):
            return ""
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1  #count required chars
        window = {}
        left = 0
        matched = 0
        start = 0
        minLen = float("inf")
        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1  #expand window
            if ch in need and window[ch] <= need[ch]:
                matched += 1  #match one required char
            while matched == len(t):
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    start = left  #save smallest window
                old = s[left]
                window[old] -= 1  #shrink window
                if old in need and window[old] < need[old]:
                    matched -= 1  #window is no longer complete
                left += 1
        if minLen == float("inf"): return ""
        return s[start:start + minLen]

print(Solution().minWindow("ADOBECODEBANC", "ABC"))
