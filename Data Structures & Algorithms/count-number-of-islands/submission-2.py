class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Understane:
        input: 2D grid with 1 and 0
        output: return the count of islands(1s surround by 0s)

        eg:
        grid = [
        ["0","1","1","1","0"],
        ["0","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
        ]

        island:s  1

        Match: DFS Graph 
            
        Plan:
        # declare variables
        set boundary for R/C = len()
        r=c=0
        count variable = 0
        visited = set()
            
        # calling helper, loop through within bound
        for r in range R:
          for c in range C:
            # isIsland 1 and not visited: count++, the starter 1, end return 
            if cell == 1 and (r,c) not visited:
            count += 1
            helper_dfs(r,c)
            #helps check it's end recursively,by mark the visited

        helper_dfs(r,c)
        #base
        return:
        -r c, out of bound, not (0 <= r c < len)
        -(rc) == 0 is water
        -(r,c) in visited

        #recursive: check U D L R
        -return the count and adds up
        for nr,nc in [[-1,0],[1,0],[0,-1],[0,1]]:
            # if in bounds
            helper_dfs([r+nr,c+nc])
        
        
        '''

        # Each DFS call corresponds to one island. visited set
        """
        # declare variables
        ROW, COL = len(grid), len(grid[0])
        count = r = c = 0
        visited = set()

        # helper function
        def dfs_helper(r,c):
        # bounds
            if not (0 <= r < ROW and 0 <= c < COL): return

        # already visited OR is water -> return
            if grid[r][c] == '0' or (r,c) in visited: return

        # mark visited
            visited.add((r,c))

        # recurse into 4 neighbors
            for nr,nc in [(1,0),(-1,0),(0,1),(0,-1)]: 
                if 0 <= r+nr < ROW and 0 <= c+nc < COL:
                    dfs_helper(r+nr, c+nc)

        # calling helper, loop through within bound
        for r in range(ROW):
            for c in range(COL):
        # is 1 and not visited: count++
                if grid[r][c] == '1' and (r,c) not in visited:
                    count += 1
                    dfs_helper(r,c)

        return count
        """
        # Mark the current cell as '0' (visited).
        ROW, COL = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        islands = 0

        def dfs(r, c):
            #basecase: out bounds, is water
            if not (0 <= r < ROW and 0 <= c < COL): return
            if grid[r][c] == '0': return

            #do something, mark it water,so no repeat visit
            grid[r][c] = '0'

            #recursion
            for dr, dc in directions:
                if (0 <= r + dr < ROW and 0 <= c + dc < COL):
                    dfs(r + dr, c + dc)

        # call the helper func dfs
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        return islands