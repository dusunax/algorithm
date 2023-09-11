/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[][]}
 */
var findDifference = function(nums1, nums2) {
    // array => set => array
    const nums1Set = new Set(nums1);
    const nums2Set = new Set(nums2);

    const result1 = [];
    const result2 = [];

    [...nums1, ...nums2].map((e) => {
        // if(nums2.includes(e)){
        //     nums1Set.delete(e)
        //     nums2Set.delete(e)
        // }

        if(!nums1Set.has(e) && !result1.includes(e)) result1.push(e);
        if(!nums2Set.has(e) && !result2.includes(e)) result2.push(e);
    })

    console.log()

    // return [Array.from(nums1Set), Array.from(nums2Set)]
    return [result2, result1]
};