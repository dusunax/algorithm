/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        let left = 1;
        let right = n;

        while (left < right){
            let mid = Math.floor((left + right) / 2);

            if (isBadVersion(mid)){
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left
    };
};

// call API "isBadVersion" to check version is bad
// - minimize calls 

// Binary search 
// check the mid version is bad
// - with isBadVersion's response, move pointers, check new mid of it.

// \U0001f914
// - left: 1, right: n
// - if mid is bad, right is mid
// - if mid is not bad, left is mid+1
// - if left is same as right? left is first bad version


