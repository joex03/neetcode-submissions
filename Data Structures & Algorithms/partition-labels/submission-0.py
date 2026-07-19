class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mapper={} # to map each letter with last index it appeared at
        for i in range (len(s)):
            mapper[s[i]]=i
        result=[]
        size=0
        end=0
        for i in range(len(s)):
            size+=1
            if mapper[s[i]]>end:
                end=mapper[s[i]]
            if i==end:
                result.append(size)
                size=0
        return result