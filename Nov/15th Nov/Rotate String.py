class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        n = len(s)

        if n != len(goal):
            return False  #different lengths cannot match

        if n == 0:
            return True  #both strings are empty

        for start in range(n):
            match = True

            for j in range(n):
                rotatedIndex = (start + j) % n  #wrapping around string

                if s[rotatedIndex] != goal[j]:
                    match = False  #rotation does not match
                    break

            if match:
                return True  #valid rotation found

        return False

print(Solution().rotateString("abcde", "cdeab"))
