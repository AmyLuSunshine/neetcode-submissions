class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        '''
        Understand:
        input: a 2D list whith nums, a dot, a color num
        output: return the color modified version of 2D list

        eg:
        image = 
        [
        [1,1,1],
        [1,1,0],
        [1,0,1]], 
        
        dot(1,1):sr = 1, sc = 1, 
        color = 2

        [2,2,2],
        [2,2,0],
        [2,0,1]], 


        edge:
        with boundry of ROW, COL
        only go U D L R
        change color if the num == starting num

        Match: Graph, DFS, Matrix, 
            Recursion

        Plan:
        -Define ROW, COL = len(image)
        -Store oringin_num = image[sr][sc]

        if dot == color: return image itself instantly

        define a helper dfs function:(sr, sr)
            #Basecase
            -return None:
            --out of bound
            if min(sr,sc) < 0, or sr=ROW or sc=COL
            --not the right num
            or (sr,sc) == color or dot != origin-num
            -if image[sr][sc] ==  origin_num, 
            update to color num

            #Recursive case
            -move U D L R each call
            func( sr-1, sc)
            func( sr+1, sc)
            func( sr, sc-1)
            func( sr, sc+1)

        -return image
        '''
        ROW = len(image)
        COL = len(image[0])
        og_num = image[sr][sc]

        # dot num == color num,return image
        if image[sr][sc] == color:
                return image

        def helper_dfs(r,c):
            # base case
            # out of bounds
            if min(r,c) < 0 or r == ROW or c == COL: return
            
            # not origin num
            if image[r][c] !=  og_num or image[r][c] == color: return

            # find the target
            if image[r][c] ==  og_num:
                image[r][c] = color

            #Recursive case: call dfs on 4 neighbors
            up = helper_dfs( r-1, c)
            down = helper_dfs(r+1, c)
            left = helper_dfs(r, c-1)
            right = helper_dfs(r, c+1)

        helper_dfs(sr, sc)

        return image
