class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        sizeOdd=0
        currentOdd=float('-inf')
        sizeEven=0
        currentEven=float('-inf')
        for i in range (len(arr)):
            if i%2==0 and (i+1)<len(arr) and arr[i]>arr[i+1]:
                sizeOdd+=1
                currentOdd=max(currentOdd,sizeOdd)
            elif i%2!=0 and (i+1)<len(arr) and arr[i]<arr[i+1]:
                sizeOdd+=1
                currentOdd=max(currentOdd,sizeOdd)
            else:
                sizeOdd=0
            if i%2==0 and (i+1)<len(arr) and arr[i]<arr[i+1]:
                sizeEven+=1
                currentEven=max(currentEven,sizeEven)
            elif i%2!=0 and (i+1)<len(arr) and arr[i]>arr[i+1]:
                sizeEven+=1
                currentEven=max(currentEven,sizeEven)
            else:
                sizeEven=0
                currentEven=max(currentEven,sizeEven)
                currentEven=max(currentEven,sizeEven)
        return max(currentEven,currentOdd)+1
        