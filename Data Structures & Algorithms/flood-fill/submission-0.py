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
        -Define a visited = set()
        -Store oringin_num = image[sr][sc]
        #Basecase
        -return None:
        if min(sr,sc) < 0, or sr=ROW or sc=COL
        or (sr,sc) in visited
        -if image[sr][sc] ==  origin_num, update to color num

        visited.add(sr,sc)

        #Recursive case
        -move U D L R each call
        floodFill(image, sr-1, sc, color)
        floodFill(image, sr+1, sc, color)
        floodFill(image, sr, sc-1, color)
        floodFill(image, sr, sc+1, color)

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
            # out of bound
            if min(r,c) < 0 or r == ROW or c == COL: return
            
            # not origin num
            if image[r][c] !=  og_num or image[r][c] == color: return

            if image[r][c] ==  og_num:
                image[r][c] = color

            #Recursive case: call dfs on 4 neighbors
            up = helper_dfs( r-1, c)
            down = helper_dfs(r+1, c)
            left = helper_dfs(r, c-1)
            right = helper_dfs(r, c+1)

        helper_dfs(sr, sc)

        return image
