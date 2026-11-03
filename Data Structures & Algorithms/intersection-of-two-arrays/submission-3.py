class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Understand:
        i: list of nums 1 and 2
        o: interval list between 1 and 2

        Match: set

        Plan:
        turn list nums1 to a hashset - seen
        turn list nums2 to a set
        create a variable res as list []
        loop through the set nums2:
            if seen in nums1's hashset
                append to res []
        return res

        Set enables O(1) lookup
        """
        seen = set(nums1) #set1 = 

        res = []
        for num in nums2:
            if num in seen:
                res.append(num)
                seen.remove(num)# make sure append once

        return res

        