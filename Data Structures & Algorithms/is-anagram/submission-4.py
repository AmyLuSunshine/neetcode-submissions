class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #Plan 1: brute force - Sorting
        """
        sort first
        if length diff, return F
        loop within the range
        if s[i] != t[i]: return F
        return T finally
        """

        """if len(s) != len(t):
            return False
        for i in range(len(s)):
            if sorted(s)[i] != sorted(t)[i]: 
                return False
        return True"""

        # use sorted("string") for string
        # sorted: O(s*logs + t*logt)
        # sorting worstcase is nlogn
        """if len(s) != len(t):  return False
        return sorted(s) == sorted(t)"""

        #Plan 2: hashmap 101
        """
        hashmap: key value pair 
        # dictionary = hashmap(o1-o(n)), python call dictionary 
                
        # mp = {} 
        # mp = defaultdict(list),
            initiate value to 0

        #mp[car] = ford, toyota, nissan, mercedes
                
        car.get():give you how many # in key, the values of key
            
        car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
        }
        
        car.get("model")
        
        hashmap.get(key) returns the value
        """
        # eg: isAnagram:
        """ 
        res1 = {} -- Empty
        res1 = {a:2, n:1,...}

        for i in "anagram":
            res[i] = res.get(i, 0) + 1
        """
        
        # I2: Two hashmap O(s+t), space O(1) because 26 max char
        """
        if len(s) != len(t): return False

        sh, th = {}, {}
        
        # for si in s:
        #     sh[si] = sh.get(si,0) + 1
        # for ti in t:
        #     th[ti] = th.get(ti,0) + 1
       
        # alternative one for loop
        for i in range(len(s)):
            sh[s[i]] = sh.get(s[i],0) + 1
            th[t[i]] = th.get(t[i],0) + 1   

        return sh == th # compare two dicts {"a":2,...} == {"a":2,...}
        # Two dicts are equal if they have:
        # the same keys mapped to the same values. Also O(n), no sorting.
       """

        # Plan 3: Single hashmap,  O(n) time / O(n) space 
        """
        increment/decrement one dict
        """

        """if len(s) != len(t): return False

        sh = {}

        for si in s:
            sh[si] = sh.get(si,0) + 1

        # for i in t:
            # sh[i] = sh.get(i,0) - 1
        for i in range(len(t)):
            if t[i] in sh:
                sh[t[i]] -= 1
            else:
                return False  
        # return all(v == 0 for v in sh.values()) 
        for j in sh:
            if sh[j] != 0: return False
        return True"""


        # #cleaner One hash method
        # from collections import defaultdict
        # count = defaultdict(int)
        # for c in s:count[c] += 1
        # for c in t:count[c] -= 1
        # return all(v==0 for v in count.values())


        # Plan 4: HashTable Array - fixed size array of 26 counts
        # O(n) O(1)
        if len(s) != len(t): return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1 #hash 
            count[ord(t[i]) - ord('a')] -= 1
        for v in count:
            if v != 0: return False
        return True

        


"""        
        strs = ["act","pots","tops","cat","stop","hat"]
        
        strh=defaultdict(list) 
        #datatype in hash, build in, defaulte value is 0
        
        #for word in strs
        #sWord = sorted version word
        # python, append became array []
        strh[sWord].append(word) - act, cat
        
        strh = {act: [act, cat], opst: [pots, tops, stop] }   
        
        return list(strh.values())
        
        key:  val1, val2
        [act: cat, tac]


"""