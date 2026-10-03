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
        diff_hash = {}
        diff = 0
        loop through idx, i in nums:
            diff = target - i
            if diff not in diff_hash:
                store in hash Pair(i:idx)
            else:
                return [idx, diff_hash[diff]]

        P3: time O() space O() 
        sorted, two pointers
        pointer i at start, pointer j at end  
        loop through the list
            if i + j == target, return index
            if i + j > target, j--
            if i+ j < target, i++

                
        """

        # I1 - time: O(n^2)  space: O(1)
        
        """for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
            return []"""

        # I2 - O(n)
        # hashmap visited/seen {}
        diff_hash = {}
        # loop with idx and num on nums array
        for idx, i in enumerate(nums):
            # get the target differences
            diff = target - i
            # check if in hashmap visited/seen {}
            if diff not in diff_hash:
                # !exists -> "key(num: value(idx)"
                diff_hash[i] = idx
            else:
                #  exitst -> return diff idx and curr idx
                return [diff_hash[diff],idx]
        
        # I3 - O(n log n) time, O(n) space
        # create a copy of array, store [value, index] pairs
        # [[3,0],[4,1]...]
        """A = []
        for idx,num in enumerate(nums):
            A.append([num,idx])
            
        A.sort() 
        # two pointers: i at start,  j at end 
        i = 0
        j = len(A) - 1
       
        # loop through the list
        while i < j:
            s = A[i][0] + A[j][0]
            if s == target:
                return sorted([A[i][1],A[j][1]])
            if s > target:
                j -= 1
            if s < target:
                i += 1
        return []"""
                