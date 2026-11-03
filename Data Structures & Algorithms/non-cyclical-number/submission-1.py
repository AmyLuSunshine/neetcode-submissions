class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        Understand
        i: positive int with digits
        o: T if digit^2 sum == 1, otherwise False

        Match: 

        Plan
        create variable sum = 0
        loop through number, number.split()->list char
            sum += char * char
        if sum == 1:return Ture, otherwise return False
        
        '''
        #n = list(str(n)) # ['1','0','0']
        #s = ''.join(n) # '100'
        # print(type(s))

        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)

            total = 0
            for digit in str(n):
                total += int(digit) ** 2 #Power of 2

            n = total
        
        return n == 1
