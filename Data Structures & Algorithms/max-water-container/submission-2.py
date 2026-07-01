class Solution:
    def maxArea(self, heights: List[int]) -> int:
        front = 0
        last = len(heights)-1
        max_area=0

        while(front<=last):
            area = (last-front)* min(heights[front], heights[last])
            if area> max_area:
                max_area = area 
            if heights[front] < heights[last]:
                front = front + 1
            else:
                last = last - 1

        return max_area    




            

