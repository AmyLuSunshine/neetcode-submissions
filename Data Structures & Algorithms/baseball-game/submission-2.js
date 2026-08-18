class Solution {
    /**
     * @param {string[]} operations
     * @return {number}
     */

/* 
    have a new stack variable
    have a new result integer

    if Number.isInteger(), push to stack
    else, 
    if(it's + and stack has at least two integer)，add last two and  push stack
    if(it's D, and stack has at lease one integer), times last idx 2 and push stack
    if(it's C, and stack has at lease one integer), pop the last from stack

    for loop pop each element and add to the result.

 */

    calPoints(operations) {
        //stack of records
        let stack = [];
        let result = 0;

        let i = 0;
       
        while(i < operations.length){
             console.log("integer", Number(operations[i]))
            if(Number.isInteger(Number(operations[i]))){
                stack.push(Number(operations[i]));
            }
            else{
                if(operations[i] === "+" && stack.length >= 2){
                    stack.push(stack[stack.length-2] + stack[stack.length-1])
                     console.log("+", stack)
                }
                if(operations[i] === "D" && stack.length >= 1){
                    stack.push(stack[stack.length-1] * 2)
                     console.log("D", stack)
                }
                if(operations[i] === "C" && stack.length >= 1){
                    stack.pop();
                     console.log("C", stack)
                }
            }
            i++;
        };
        
        let j = stack.length-1;
        while(j >= 0){
            result += stack[j]
            j--;
             console.log("result", result)
        }
        //  console.log("result ok", result)
        return result;
    }
}
