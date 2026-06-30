class Solution:
    def search(self, nums: List[int], target: int) -> int:
        front = 0
        last = len(nums)-1

        while front<=last:
            mid = (front+last)//2
            print (mid)
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                front = mid+1
            else:
                last = mid -1
        return -1
