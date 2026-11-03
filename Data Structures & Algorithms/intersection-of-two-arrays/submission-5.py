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
        build in intersection between &
        return res

        Set enables O(1) lookup
        """
        #print(set1 & set2) #{2} <class'set'>
    
        return list(set(nums1) & set(nums2))  #[2]

        