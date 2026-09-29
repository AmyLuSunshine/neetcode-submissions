# from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        # print(hashmap)
        max_val = [0,0]  #[count,val]
        for h in hashmap:
            if hashmap[h] > max_val[0]:
                max_val = [hashmap[h], h]  
        return max_val[1]

    """
    voting algorithsm - hashmap

    """