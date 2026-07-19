class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        mapper={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        result=[]
        tmp=[]
        n=len(digits)
        def helper(i):
            if i==n:
                result.append("".join(tmp))
                return
            for l in mapper[digits[i]]:
                tmp.append(l)
                helper(i+1)
                tmp.pop()
        helper(0)
        return result

