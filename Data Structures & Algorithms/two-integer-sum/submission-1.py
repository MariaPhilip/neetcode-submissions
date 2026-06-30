class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range (len(nums)):
            hash_map[nums[i]] = i
            """
            3 4 5 6

            1 : 0
            3 : 1
            4 : 2
            2 : 3
            ###
        
        """
        for i in range (len(nums)):
            diff = target - nums[i]
            if diff in nums and i != hash_map[diff]:
                return [i,hash_map[diff]]
            
        

        