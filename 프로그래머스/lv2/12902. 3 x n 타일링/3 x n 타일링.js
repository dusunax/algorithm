/** 230615: DP 연습-4 */
function solution(n) {
    const cache = [1, 0, 3];

    for (let i = 4; i <= n; i += 2) {
        let temp = 0;

        // 짝수에 2가지 추가
        for (let j = i - 4; j >= 0; j -= 2) {
            temp += 2 * cache[j];
            temp %= 1000000007;
        }
        
        cache[i] = (3 * cache[i - 2] + temp) % 1000000007;
    }

    return cache[n];
}
