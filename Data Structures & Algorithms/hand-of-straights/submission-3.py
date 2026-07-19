class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        mapper=Counter(hand)
        size=len(hand)
        if size%groupSize!=0:
            return False
        hand.sort()
        for num in hand:
            if mapper[num]:
                for i in range (num,num+groupSize):
                    if  mapper[i]==0:
                        return False
                    else:
                        mapper[i]-=1
        return True