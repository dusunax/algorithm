/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const filteredStr = s.toLowerCase().replace(/[^a-z0-9]/g, '');

    const reversedStr = filteredStr.split('').reverse().join('');

    return filteredStr === reversedStr
};