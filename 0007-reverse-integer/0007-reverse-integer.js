/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    const reversedStr = Math.abs(x).toString().split('').reverse().join("");
    const result = Number(reversedStr) * Math.sign(x);

     if (result < Math.pow(-2, 31) || result > Math.pow(2, 31) - 1) {
        return 0;
    }

    return result;
};