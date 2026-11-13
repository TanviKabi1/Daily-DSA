class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        result = []
        i = 0

        while i < len(command):
            if command[i] == 'G':
                result.append('G')  #G remains unchanged
                i += 1

            elif command[i] == '(' and command[i + 1] == ')':
                result.append('o')  #converting () into o
                i += 2

            else:
                result.append('al')  #converting (al) into al
                i += 4

        return ''.join(result)


print(Solution().interpret("G()(al)"))  #"Goal"
