/**
* 대칭 문자열인 경우 중, 가장 긴 길이 구하기
* a. 길이가 1일 때: 대칭 true
* b. 길이가 2일 때: 다음 문자와 같다면 대칭 true
* c. 길이가 3 이상일 때: 
*/
function solution (s) {
    const n = s.length;
    const dp = Array.from(Array(n).fill(), () => Array(n).fill(false)); // dp 배열 초기화

    var answer = 1;
    
    // a. 길이 1
    for (let i = 0; i < n; i++) {
        dp[i][i] = true;
    }

    // b. 길이 2
    for (let i = 0; i < n - 1; i++) {
        if (s[i] === s[i + 1]) {
            dp[i][i + 1] = true;
            answer = 2;
        }
    }

    // c. 길이 3 이상
    for (let i = 3; i <= n; i++) { // 길이
        for (let start = 0; start <= n - i; start++) { // 시작점 start
            const end = start + i - 1; // 끝점

            // 시작점과 끝점의 문자열이 같음 && 부분 문자열이 팰린드롬
            if (s[start] === s[end] && dp[start + 1][end - 1]) {
                dp[start][end] = true;
                answer = Math.max(answer, i); // 갱신
            }
        }
    };

    return answer;
}