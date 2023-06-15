/** 230615: DP 연습-2  */

// Dynamic Programming: Bottom-up
// 작은 부분 문제에서 큰 문제로 차례대로 해결
function solution(n) {
    if (n === 1) return 1;
    if (n === 2) return 2;

    let a = 1;
    let b = 2;

    for (let i = 3; i <= n; i++) {
        const temp = (a + b) % 1000000007;
        a = b;
        b = temp;
    }

    return b;
}

// Dynamic Programming: Top-down
// 재귀 (효율성 결과가 전부 실패)
// const topDownCache = [];
// function solutionTopDown(n) {
//     if (n === 1) return 1;
//     if (n === 2) return 2;

//     if (topDownCache[n] !== undefined) {
//         return topDownCache[n];
//     } else {
//         const num = solution(n - 1) + solution(n - 2);
//         topDownCache[n] = num;

//         return num % 1000000007;
//     }
// }