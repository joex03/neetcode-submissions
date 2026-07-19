class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        q=deque([("0000",0)])
        visit=set(deadends)
        while q:
            value,count=q.popleft()
            if value == target:
                return count
            for i in range(4):
                tmp1=str((int(value[i])+1)%10)
                tmp2=str((int(value[i])+9)%10)
                string1=(value[:i]+tmp1+value[i+1:])
                string2=(value[:i]+tmp2+value[i+1:])
                if string1 not in visit:
                    visit.add(string1)
                    q.append([string1,count+1])
                if string2 not in visit:
                    visit.add(string2)
                    q.append([string2,count+1])
        return -1
