/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[][]}
 */
var findDifference = function(nums1, nums2) {
    // array => set => array
    const nums1Set = new Set(nums1);
    const nums2Set = new Set(nums2);

    nums1.map((e) => {
        if(nums2.includes(e)){
            nums1Set.delete(e)
            nums2Set.delete(e)
        }
    })

    return [Array.from(nums1Set), Array.from(nums2Set)]
};