class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                ele=stack.pop()
                if i=='}' :
                    if ele!='{':
                        return False
                elif i==']':
                    if ele !='[':
                        return False
                elif i==')':
                    if ele!='(':
                        return False
        return True if len(stack)==0 else False