/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    if(!n) return;

    let p1 = m-1;
    let p2 = n-1;
    let index = m+n -1; // index

    while(p1 >= 0 && p2 >= 0){ // 조건 확인
        if(nums1[p1] > nums2[p2]){
            nums1[index] = nums1[p1];
            p1--;
        } else {
            nums1[index] = nums2[p2];
            p2--;
        }

        index--;
    }

    while (p2 >= 0){
        nums1[index] = nums2[p2];
        p2--;
        index--;
    }
};

// should merge arrays into nums1
// non-decreasing order
// m: denote the index of marge start
// n: last numbes, that set to 0's, should be ignored.
// hint: problem give us m & n for two-pointers

// prototype
// nums1.filter(e=>e).concat(nums2).sort((a, b)=>a-b) // [ 1, 2, 2, 3, 5, 6 ]

// \U0001f914
// - nums1 is already sorted by non-decresing order.
// - should modify the num1 array directly
// - should solve with O(m+n) time complexity

// Use two-pointer for minimal operations (to optimize the time complexity)
// - Avoid Unnecessary Shifts: starting from end
