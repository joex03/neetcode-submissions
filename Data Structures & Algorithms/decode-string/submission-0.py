class Solution:
    def decodeString(self, s: str) -> str:
        tmp=""
        num=0
        nums,chars=[],[]
        for c in s:
            if c.isdigit():
                num=num*10+int(c)
            elif c=='[':
                nums.append(num)
                num=0
                chars.append(tmp)
                tmp=""
            elif c==']':
                k=nums.pop()
                char=chars.pop()
                tmp=char+tmp*k
            else:
                tmp+=c
        return tmp