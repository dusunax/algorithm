/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    const frequencyMap = new Map();

    for (let char of s) {
        frequencyMap.set(char, (frequencyMap.get(char) || 0) + 1)
    }

    for (let i = 0; i < s.length; i++) {
        if (frequencyMap.get(s[i]) === 1){
            return i;
        }
    }

    return -1
};