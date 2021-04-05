class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        list1 = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] != ')':
                stack.append(s[i])
            else:
                pop = stack.pop()
                if pop != '(':
                    list1.append(pop)
                else:
                    stack += list1
                    list1 = []
                    i += 1
                continue

            i += 1
        return "".join(stack) 