class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        for char in tokens:
            if char == "+":
                a = int(stack.pop())
                print(f"a:{a}")
                b = int(stack.pop())
                print(f"b:{b}")
                stack.append(a+b)
            elif char == "*":
                a = int(stack.pop())
                print(f"a:{a}")
                b = int(stack.pop())
                print(f"b:{b}")
                stack.append(a*b)
            elif char == "/":
                a = int(stack.pop())
                print(f"a:{a}")
                b = int(stack.pop())
                print(f"b:{b}")
                stack.append(b/a)
            elif char == "-":
                a = int(stack.pop())
                print(f"a:{a}")
                b = int(stack.pop())
                print(f"b:{b}")
                stack.append(b-a)
            else:
                stack.append(int(char))
                print("appending number:")
                print(char)
                
            

        return int(stack.pop())

                
        