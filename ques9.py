class ParenthesesValidator:
    def is_valid(self, s):
        stack = []
        brackets = {"(": ")", "{": "}", "[": "]"}
        
        for char in s:
            if char in brackets:
                stack.append(char)
            elif char in brackets.values():
                if not stack or brackets[stack.pop()] != char:
                    return False
        
        return len(stack) == 0


validator = ParenthesesValidator()
print(validator.is_valid("()"))  
print(validator.is_valid("()[]{}"))  
print(validator.is_valid("[)"))  
print(validator.is_valid("({[)]"))  
print(validator.is_valid("{{{"))  

