class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        U: find sum of two items that equals to target,
            return index of those two items

        P1: O(n^2)
        loop through nums from idx i   
            loop through nums from idx i+1
                check if nums[i] + nums[j] == 7
                    return [i,j]
            

        p2: o(n) 
            enumerate
            hashmap
        """

        # I1 - O(n^2)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                        