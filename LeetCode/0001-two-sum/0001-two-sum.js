/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        console.log('leethub v2 testing 10')
        const otherNumber = target - nums[i];
        const idx = nums.indexOf(otherNumber);

        if (idx !== -1 && idx !== i) return [i, idx];
    }
};