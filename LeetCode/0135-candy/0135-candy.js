/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function(ratings) {
    // (각 상황에서)최선의 선택 => greedy
    // 순방향 순회: 점수가 높을 때, 사탕+1
    // 역방향 순회: 최대값 갱신(이미 나눠준 사탕 갱신)

    const n = ratings.length; // 점수
    const candies = new Array(n).fill(1);

    // 왼쪽 => 오른쪽으로 순회하면서 오른쪽 아이와 비교(사탕 수 조절)
    for (let i = 1; i < n; i++) {
        if (ratings[i] > ratings[i - 1]) {
            candies[i] = candies[i - 1] + 1;
        }
    }

    // 오른쪽 => 왼쪽으로 다시 순회하면서 왼쪽 아이와 비교(사탕 수 조절) + 결과 계산
    for (let i = n - 2; i >= 0; i--) {
        if (ratings[i] > ratings[i + 1]) {
            candies[i] = Math.max(candies[i], candies[i + 1] + 1);
        }
    }

    // 총 갯수=reduce
    return candies.reduce((a, b) => a + b, 0);
};