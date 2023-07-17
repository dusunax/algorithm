// 최고의 집합
// 1. 각 원소의 합이 S가 되는 수의 집합
// 2. 각 원소의 곱이 최대가 되는 집합
function solution(n, s) {
    if (s < n) return [-1]; // 1의 예외: 합이 s가 될 수 없음
    
    // 자바스크립트의 몫과 나머지
    const quotient = Math.floor(s / n); // 몫
    const remainder = s % n; // 나머지

    // n만큼 몫으로 채움
    const answer = new Array(n).fill(quotient); 
    
    // 동일 숫자의 집합 => 최고 집합
    // (3, 9)일 때 [3, 3, 3], 3^3 = 27
    if (remainder === 0) return answer;

    // n-1부터 n-remainder까지 역순으로
    // 나머지 값을 큰 원소에 우선적으로 분배
    for (let i = n - 1; i >= n - remainder; i--) {
        answer[i]++;
    }

    return answer;
}
