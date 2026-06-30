class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map={
            "[":"]",
            "(":")",
            "{":"}"
        }
        if len(s)%2!=0:
            return False

        for char in s:
            if char == "[" or char =="("or char == "{":
                stack.append(char)
            elif char == "]" or char =="}" or char ==")":
                if stack:
                    if hash_map[stack[-1]] == char:
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        
        if stack:
            return False
        else:
            return True
            
        