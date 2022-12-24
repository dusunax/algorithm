// 간단 풀이
// time이 0(false)이 될 때까지 -1
function solution(n, time) {
    const multifly = 2;
    
    while(time) {
        n = n * multifly;
        time--;
    }
    return n;
}

// 복잡한 풀이
// 초기값이 있는 reduce를 사용한 풀이(불필요)
// const solution = (n, time) => new Array(time).fill(2).reduce((acc, multiply) => { return acc * multiply }, n)