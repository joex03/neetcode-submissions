class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #[1:2 , 2:1,3:1] -> 12,13 so not consecutive
        size=len(hand)
        if size%groupSize!=0:
            return False
        mapper=Counter(hand) # we did the map
        hand.sort()
        for i in range (size): # for each num we need to make sure its consecutive existss
            if mapper[hand[i]]: # if this number exists
                for j in range (hand[i], hand[i]+groupSize):
                    if mapper[j]==0: #frequency is zero
                        return False
                    else :
                        mapper[j]-=1
        return True

