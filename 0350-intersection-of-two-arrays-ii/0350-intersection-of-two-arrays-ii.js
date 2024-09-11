/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
// calculate Frequency
var intersect = function(nums1, nums2) { 
    const map = new Map();
    const result = [];
    
    for (const num of nums1) {
        map.set(num, (map.get(num) || 0) + 1);
    }

    for (const num of nums2) {
        if (map.has(num) && map.get(num) > 0) {
            map.set(num, map.get(num) - 1);
            result.push(num);
        }
    }
    
    return result;
};