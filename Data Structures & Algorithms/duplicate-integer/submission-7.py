class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        U:
        Return true if has duplicate, otherwise return false 

        P:
        SET: return false if set len < nums len
        Hash: return true if seen in hashmap
        
        """
        # SET O(n)
        """num_set = set(nums)
        if len(num_set) < len(nums):
            return True
        return False"""
        # return len(set(nums)) < len(nums)

        # Hashmap O(n)   #hashset O(n)
        """num_hash = {} # seen = set()
        for num in nums:
            if num in num_hash:
                return True
            num_hash[num] #seen.add(num)
        return False"""

        # sort Time complexity: O(n logn) Space Complexity: O(1) - O(n)
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False