/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let result = '';
    let minLength = Math.min(...strs.map(str => str.length));
    
    for (let i = 0; i < minLength; i++) {
        const char = strs[0][i]

        for (let j = 1; j < strs.length; j++) {
            if (strs[j][i] !== char) {
                return result;
            }
        }     
        result += char;
    }
    
    return result;
};