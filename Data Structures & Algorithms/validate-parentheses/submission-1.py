class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brac_map = {"(":")","[":"]","{":"}"}
        for char in s:
            if char in brac_map:
                stack.append(brac_map[char])
            else:
                if stack and stack[-1] == char:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

        '''We have to take care of three things:
        1) For every opening bracket, add its equivalent closing bracket to stack
        2) For every closing bracket, just look at the top of stack . If same -> pop
        3) Else return False'''