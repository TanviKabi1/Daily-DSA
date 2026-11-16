class Solution(object):
    def ana(self, s, p):
        ans = []
        m = len(p)
        n = len(s)

        if m == 0 or m > n:
            return ans

        need = {}
        window = {}

        for ch in p:
            need[ch] = need.get(ch, 0) + 1  #count pattern characters

        matched = 0
        required = len(need)

        for right in range(n):
            ch = s[right]

            if ch in need:
                old = window.get(ch, 0)

                if old == need[ch]:
                    matched -= 1  #remove old frequency match

                window[ch] = old + 1

                if window[ch] == need[ch]:
                    matched += 1  #add new frequency match

            if right >= m:
                leftChar = s[right - m]

                if leftChar in need:
                    old = window[leftChar]

                    if old == need[leftChar]: #remove old frequency match
                        matched -= 1  

                    window[leftChar] -= 1

                    if window[leftChar] == 0: #remove zero frequency
                        del window[leftChar]  

                    if window.get(leftChar, 0) == need[leftChar]:  #check updated frequency
                        matched += 1 

            if right >= m - 1 and matched == required:
                ans.append(right - m + 1)  #store anagram index

        return ans

print(Solution().ana("cbaebabacd", "abc"))
