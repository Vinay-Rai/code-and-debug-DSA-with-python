class Solution:
    def isValid(s):
        stack = []  # Initialize an empty stack
        
        for bracket in s:
            # If it's an opening bracket, push it onto the stack
            if bracket == "(" or bracket == "{" or bracket == "[":
                stack.append(bracket)
            # If it's a closing bracket
            else:
                # If stack is empty, there's no matching opening bracket
                if len(stack) == 0:
                    return False
                    
                # Pop the top of the stack
                ch = stack.pop()
                
                # Check if the current closing bracket matches the popped opening bracket
                if (
                    (bracket == ")" and ch == "(")
                    or (bracket == "]" and ch == "[")
                    or (bracket == "}" and ch == "{")
                ):
                    continue  # Valid pair, continue checking
                else:
                    return False  # Invalid pair
                    
        # After processing the string, the stack should be empty
        # if all brackets were properly closed
        return len(stack) == 0