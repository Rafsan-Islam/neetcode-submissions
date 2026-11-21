class Solution:
    def isValid(self, s: str) -> bool:
        '''
        This is a stack problem, which means last in, first out.

I need two things. The first is a hashmap that stores the three bracket pairs, with each closing bracket mapped to its matching opening bracket. I write it myself before the loop and it never changes, so it works like a cheat sheet. The second is a stack, which is just an empty list, and it holds the opening brackets I am still waiting to close.

I go through the string once, from left to right. When I see an opening bracket, I push it onto the stack. When I see a closing bracket, I look up its matching opening bracket in the hashmap and check whether that bracket is on top of the stack. If it matches, I pop it off the stack. If it does not match, or the stack is empty, I return false.

At the end, if the stack is empty, every bracket was matched and I return true. If the stack still has brackets in it, I return false.
'''


        valid = {")": "(",  "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in valid:
                if len(stack) != 0 and stack[-1] == valid[char]:
                    
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
            
        return len(stack) == 0

