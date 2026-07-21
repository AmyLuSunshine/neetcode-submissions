class Solution {
    /**
     * @param {number[]} arr
     * @return {number[]}
     * 
     * static array
     * 
     * loop through each element with dynamic start till the end
     * and compare, then overwritten the new value in array
     */
    /* replaceElements(arr) {    
        let big = arr[1];
        for(let i=0; i<arr.length; i++){
            while(i !== length){
                if(arr[i] < arr[i+1]){
               big = arr[i+1];
               arr[i-1] = big;
            }
            }
            if(i === length - 1){
                arr[i] = -1;
            }
            
        }
    } */
   replaceElements(arr) {    
        let max = arr[(arr.length)-1];
        let curr = 0;
        arr[(arr.length)-1] = -1;
        for(let i=(arr.length)-2; i>=0; i--){
            //curr  VS  max
            curr = arr[i];
            arr[i] = max;
            if(curr > max){
               max = curr;
            } 
        }
        return arr;
    }
}
