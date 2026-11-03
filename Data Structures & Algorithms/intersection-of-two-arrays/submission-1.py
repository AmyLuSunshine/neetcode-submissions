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
        """
        seen_nums1 = set(nums1)
        seen_nums2 = set(nums2)

        res = []

        for num in seen_nums2:
            if num in seen_nums1:
                res.append(num)
        
        return res

        