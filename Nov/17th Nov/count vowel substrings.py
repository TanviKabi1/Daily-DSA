class Solution(object):
    def countVowels(self, word):
        ans = 0
        vowels = "aeiou"

        for i in range(len(word)):
            seen = set()
            for j in range(i, len(word)):
                if word[j] not in vowels:
                    break  #stop at consonant
                seen.add(word[j])
                if len(seen) == 5:
                    ans += 1  #all vowels found

        return ans


print(Solution().countVowels("aeiouu"))
