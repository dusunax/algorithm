/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
// Calculate Frequency
// - time: O(N+M)
// - space: O(Min(N,M))
var intersect = function(nums1, nums2) { 
    const map = new Map();
    const result = [];
    const [shorter, longer] = nums1.length < nums2.length ? [nums1, nums2] : [nums2, nums1];
    
    for (const num of shorter) {
        map.set(num, (map.get(num) || 0) + 1);
    }

    for (const num of longer) {
        if (map.has(num) && map.get(num) > 0) {
            map.set(num, map.get(num) - 1);
            result.push(num);
        }
    }
    
    return result;
};