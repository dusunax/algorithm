// JS

// A. modulo
/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function(num) {
    let step = 0;

    while (num) {
        num % 2 ? num -= 1 : num /= 2;
        step++;
    }

    return step;
};

// B. bitwise operations
/**
 * @param {number} num
 * @return {number}
 */
// var numberOfSteps = function(num) {
//     let step = 0;

//     while (num) {
//         num & 1 ? num -= 1 : num >>= 1;
//         step++;
//     }

//     return step;
// };