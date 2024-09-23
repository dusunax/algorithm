/**
 * @param {string} s
 * @return {number}
 */
// Parsing
// Range Clamping
var myAtoi = function(s) {
    let result = "";
    let sign = 1
    let index = 0;
    const max = 2 ** 31 - 1;
    const min = -(2 ** 31)

    // Step 1: Whitespace, 공백 제거
    s = s.trim();

    // Step 2: Signedness, 부호 처리
    if (s[index] === '-') {
        sign = -1;
        index++;
    } else if (s[index] === '+') {
        index++;
    }

    // Step 3: Conversion, 숫자 변환
    while (index < s.length && s[index].match(/^\d$/)) {
        result = result * 10 + Number(s[index]);
        index++;

        // Step 4: Rounding, 범위 초과
        if (sign * result > max) {
            return max;
        }
        if (sign * result < min) {
            return min;
        }
    }
    return result * sign 
};