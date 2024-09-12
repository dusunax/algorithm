/**
 * @param {number} x
 * @return {number}
 */
// 1. Convert to string
// var reverse = function(x) {
//     const reversedStr = Math.abs(x).toString().split('').reverse().join("");
//     const result = Number(reversedStr) * Math.sign(x);

//      if (result < Math.pow(-2, 31) || result > Math.pow(2, 31) - 1) {
//         return 0;
//     }

//     return result;
// };

// 2. Using remainder
var reverse = function(x) {
    let num = Math.abs(x)
    let res = 0

    while (num > 0) {
        let digit = num % 10;
        num = Math.floor(num / 10);
        if (res > Math.floor((2 ** 31 - 1) / 10) || (res === Math.floor((2 ** 31 - 1) / 10) && digit > 7)) {
            return 0;
        }
        res = (res * 10) + digit;
    }

    return res * Math.sign(x)
}