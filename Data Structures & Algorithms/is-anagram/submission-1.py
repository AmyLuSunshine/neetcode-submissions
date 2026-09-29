class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            hashmap: key value pair 
            # dictionary = hashmap(o1-o(n)), python call dictionary 
                    
            # mp = {} 
            # mp = defaultdict(list),
                initiate value to 0

            #mp[car] = ford, toyota, nissan, mercedes
                    
            car.get():give you how many # in key, the value of key
                
            car = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
            }
            
            car.get("model")
            
            hashmap.get(key) returns the value
        """


    # isAnagram:        
    # res1 = {} -- Empty
    # res1 = {a:2, n:1,...}
    
    # for i in "anagram":
    #     res[i] = res.get(i, 0) + 1
    
    # sh = {}
    # th = {}
    
    # for si in s:
    #     sh[si] = sh.get(si,0) + 1
    # for ti in t:
    #     th[ti] = th.get(ti,0) + 1
    
        if len(s) != len(t):  return False
    
    # for i in range(len(s)):
    #     sh[s[i]] = sh.get(s[i],0) + 1
    #     th[t[i]] = th.get(t[i],0) + 1   
    # return sh == th
    
    # use sorted("string") for string
    # sorted: O(s*logs + t*logt)
    # sorting worstcase is nlogn
        return sorted(s) == sorted(t)
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