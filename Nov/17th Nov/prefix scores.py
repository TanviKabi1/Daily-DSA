class Solution(object):
    def prefixScores(self, words):
        pref = {}
        ans = []

        for word in words:
            for i in range(1, len(word) + 1):
                p = word[:i]
                pref[p] = pref.get(p, 0) + 1  #count each prefix

        for word in words:
            score = 0
            for i in range(1, len(word) + 1):
                score += pref[word[:i]]  #add prefix frequency
            ans.append(score)

        return ans


print(Solution().prefixScores(["abc", "ab", "bc", "b"]))
