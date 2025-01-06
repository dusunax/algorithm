/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const result = {};

    for (const str of strs) {
        const sortedKey = str.split('').sort().join('');
        if (!result[sortedKey]) {
            result[sortedKey] = [];
        }
        result[sortedKey].push(str);
    }

    return Object.values(result);
};