class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        U:
        Return true if has duplicate, otherwise return false 

        P:
        SET: return false if set len < nums len
        Hash: return true if seen in hashmap
        
        """
        # SET
        """num_set = set(nums)
        if len(num_set) < len(nums):
            return True
        return False"""

        # Hashmap
        num_hash = {}
        for num in nums:
            if num in num_hash:
                num_hash[num] += 1
                return True
            num_hash[num] = 1
        return False

