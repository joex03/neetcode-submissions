class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for t in tokens:
            if t in '*/+-':
                x,y=stack.pop(),stack.pop()
                if t=='+':
                    stack.append(int(x)+int(y))
                elif t=='*':
                    stack.append(int(x)*int(y))
                elif t=='-':
                    stack.append(int(y)-int(x))
                elif t=='/':
                    res=int(y)/int(x)
                    if res<0:
                        stack.append(math.ceil(res))
                    else:
                        stack.append(math.floor(res))
            else:
                stack.append(t)
        return int(stack[0])