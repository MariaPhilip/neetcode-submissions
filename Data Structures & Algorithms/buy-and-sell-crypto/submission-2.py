class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxP = 0
        while(right<len(prices)):
            if prices[right]<prices[left]:
                left=right
                right+=1
            else:
                maxP = max(maxP, (prices[right]-prices[left]))
                right+=1
            
        return maxP 


            


        