/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
    const n = s.length;
    let count = 0;

    const expand = (left, right) => {
        while (
            left >= 0 &&
            right < n &&
            s[left] === s[right]
        ) {
            count++;
            left--;
            right++;
        }
    }

    for (let i = 0; i < n; i++) {
        expand(i, i); // 홀수 길이의 팰린드롬
        expand(i, i + 1); // 짝수 길이의 팰린드롬
    }

    return count;
};
