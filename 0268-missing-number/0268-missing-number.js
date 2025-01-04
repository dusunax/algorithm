/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) { 
    let distinctNums = new Set(nums);
    

    // for (any of nums) {
    //     if (distinctNums.has(any)) {
    //         return
    //     } else {
    //         distinctNums.add(any)
    //     }
    // }

    const n = distinctNums.size;

    for (let i = 0; i <= n; i++) {
        if (!nums.includes(i)) {
            return i;
        }
    }
};