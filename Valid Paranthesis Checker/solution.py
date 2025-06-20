class Solution:
    def checkValidString(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i==")":
                top=-1
                while stack and stack[top]!="(":
                    top-=1
                    if -top>len(stack):
                        stack.append(")")
                        break
                else:
                    if stack:
                        stack.pop(top)
                    else:
                        stack.append(")")
            else:
                stack.append(i)
        while stack:
            if stack[-1]=="*":
                i=1
                while stack[-i]!="(":
                    i+=1
                    if i==len(stack)+1:
                        stack.pop()
                        break 
                else:
                    stack.pop(-i)
                    stack.pop()
            elif stack[-1]==")":
                i=1
                while stack[-i]!="*":
                    i+=1
                    if i==len(stack)+1:
                        return False
                        break 
                else:
                    stack.pop(-i)
                    stack.pop()
            else:
                return False
        return True

        
