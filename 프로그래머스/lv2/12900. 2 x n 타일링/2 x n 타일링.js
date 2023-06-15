
// Dynamic Programming: Bottom-up
// 작은 부분 문제에서 큰 문제로 차례대로 해결
function solution(n) {
    if (n === 1) return a;
    if (n === 2) return b;

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
const cache = [];
function solutionTopDown(n) {
    if (n === 1) return 1;
    if (n === 2) return 2;

    if (cache[n] !== undefined) {
        return cache[n];
    } else {
        const num = solution(n - 1) % 1000000007 + solution(n - 2) % 1000000007;
        cache[n] = num;
        return num % 1000000007;
    }
}