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
        # # loop with idx and num on nums array
        for idx, i in enumerate(nums):
        #     # get the target differences
            diff = target - i
        #     # check if in hashmap visited/seen {}
            if diff not in diff_hash:
        #         # !exists -> "key(num: value(idx)"
                diff_hash[i] = idx
            else:
        #         #  exitst -> return diff idx and curr idx
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


        # return value, optimize the space to O(1)
        # 3,4
        '''
            [3,4,4,5,6,8]
        sum: 9
            l
                        r
            
        val:
        target:9

        ask q before do: if there's multiple pairs, can this that
        '''

        #2 0(n^2)
        """ 
        nums.sort()
        diff = 0

        for idx,n in enumerate(nums):
            diff = target - n

            for idx2 in range(idx+1,len(nums)):
                if nums[idx2] == diff:
                    return  [n,nums[idx2]]
                    """

        #3 O(n) two pointers
        """
        l = 0 
        r = len(nums) -1
        nums.sort()
        while l < r:
            if nums[l] + nums[r] == target: 
                return [nums[l], nums[r]]
            elif nums[l] + nums[r] < target: 
                l += 1
            else:
                r -= 1
        return [-1,-1]
        """
            
        # 4: if multiple pairs, use one num once
        '''
            [3,4,4,5,6,8]
        sum: 9
                l
                    r
            
        res[[3,6],[4,5],[4,5]]:
        target:9

    
        #find all the pairs
        #have two pointer l and r
        if l + r val = target, 
        if res[-1][0] != l and res[-1][1] != r:
            store to res 
        move l++
        if < t: move l ++
        if > t: move r --
        #remove duplicate (set() crate new space, so no)
        '''
        """
        def twoSum(nums,target):
        
            l = 0 
            r = len(nums) -1
            res = []

            nums.sort()

            while l < r:
                # print(l,r)
                if nums[l] + nums[r] == target:
                res.append((nums[l], nums[r])) 
                l += 1
                r -= 1
                #check both left and right
                while l < len(nums) and r > l and nums[l] == nums[l+1]:
                    l += 1

                while r >=0 and r > l and nums[r] == nums[r-1]:
                    r -= 1

                elif nums[l] + nums[r] < target:
                l += 1
                else:
                r -= 1
                    
            return res

        nums = [3,4,4,5,6,8]
        target = 9

        print(twoSum(nums, target))"""

        
                