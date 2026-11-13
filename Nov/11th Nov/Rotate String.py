class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):  #different lengths cannot be rotations
            return False

        n = len(s)

        for i in range(n):
            match = True

            for j in range(n):
                if s[(i + j) % n] != goal[j]:  #checking characters using modular indexing
                    match = False
                    break

            if match:
                return True

        return True if n == 0 else False


print(Solution().rotateString("abcde", "cdeab"))  #True
