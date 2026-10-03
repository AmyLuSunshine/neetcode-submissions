class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        U:
        Return true if has duplicate, otherwise return false 

        P:
        SET: return false if set len < nums len
        Hash: return true if one value >= 2
        
        """
        num_set = set(nums)
        if len(num_set) < len(nums):
            return True
        return False