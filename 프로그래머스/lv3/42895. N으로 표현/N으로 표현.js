/**
* N: 사칙 연산에 사용할 숫자
* number: 숫자
*/
function solution(N, number) {
    const MAX = 8;
    // 2차원 Set 배열 생성
    const dp = Array.from(Array(MAX), () => new Set());
    
    for (let i = 0; i < MAX; i++) { // 연산 횟수
        // i번째 set에 N을 여러개 사용하는 경우 추가
        dp[i].add(Number(N.toString().repeat(i + 1)));
         
        
        for (let j = 0; j < i; j++) { // 연산 횟수 i만큼 추가
            for (const arg1 of dp[j]) {
                for (const arg2 of dp[i - j - 1]) {
                    // 두 개의 숫자 arg1과 arg2를 조합하여 만들 수 있는 경우의 수를 추가
                    dp[i].add(arg1 + arg2);
                    dp[i].add(arg1 - arg2);
                    dp[i].add(arg1 * arg2);
                    dp[i].add(Math.floor(arg1 / arg2));
                }           
            }
        }
        
        // 현재 연산 횟수 번째의 set 확인하고, 있다면 +1을 반환
        if (dp[i].has(number)) return i + 1;
    }
    
    return -1;
}