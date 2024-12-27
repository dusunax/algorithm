/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    const result = []; // int[][]
    
    function backtrack (start, remain, combination) {
        if (remain === 0){
            result.push([...combination])
            return;
        }
        if (remain < 0) return;

        for (let i = start; i < candidates.length; i++ ){
            combination.push(candidates[i]);
            backtrack(i, remain-candidates[i], combination);
            combination.pop()
        }
    }
        
    backtrack(0, target, []);
    return result;
};