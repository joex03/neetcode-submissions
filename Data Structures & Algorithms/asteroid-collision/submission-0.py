class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res=[]
        pos=[]
        for a in asteroids:
            if a>0:
                pos.append(a)
            else:
                flag=True
                #negative
                while pos:
                    right=pos.pop()
                    left=abs(a)
                    if right>left:
                        pos.append(right)
                        break
                    elif right<left:
                        # we need to loop on other right elements
                        continue # we will go for other pos
                    else:
                        flag=False
                        break
                if not pos and flag:
                    res.append(a)
        for p in pos:
            res.append(p)
        return res