class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators={'+' ,'-','/','*'}
        stack=[]
        for token in tokens:
            if token in operators:
                val2=stack.pop()
                val1=stack.pop()
                if token=="+":
                    stack.append(val1+val2)
                elif token=='*':
                    stack.append(val1*val2)
                elif token=='/':
                    stack.append(int(val1/val2))
                elif token=='-':
                    stack.append(val1-val2)
                continue

            stack.append(int(token))
        return stack[0]
        