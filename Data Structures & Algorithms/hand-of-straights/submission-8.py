class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize !=0:
            return False
        mapper={}
        for num in hand:
            if num in mapper:
                mapper[num]+=1
            else:
                mapper[num]=1
        hand.sort()
        for num in hand:
            if mapper[num]:
                for i in range (num,num+groupSize):
                    if i in mapper:
                        if  mapper[i]>0:
                            mapper[i]-=1

                        else:
                            return False

                    else:
                        return False
        return True            