class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        //dfs : depth first search
        const cache = new Array(n).fill(-1);//prefill -1 for n
        const dfs = (i) =>{
        //base case
       /*  if(i >= n){//reach top,or exceed
            if(i === n){
                //one valid path
                return 1;
             }
             //exceed, invalid path
            return 0;
        } */
        if(i >= n){
            return i == n ? 1: 0;//truthy, either 1 or 0 
        }
        //don't redo recursion if it's not -1
        if(cache[i] != -1) return cache[i]

        //recursive call
         return (cache[i] = dfs(i+1) + dfs(i+2));
        }
        return dfs(0);

    }
}
