/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var decodeAtIndex = function(s, k) {
    let count = 0;
    
    // 첫 번째 루프: 반복 횟수를 계산하고 K에 도달할 때까지 반복 수를 누적합니다.
    for (let i = 0; i < s.length; i++) {
        if (!isNaN(s[i])) {
            count *= Number(s[i]);
        } else {
            count++;
        }
    }

    // 두 번째 루프: K를 계속해서 줄여나가면서 결과 charactor 찾기
    for (let i = s.length - 1; i >= 0; i--) {
        k %= count;
        
        // K가 0이고 현재 문자가 숫자가 아니면 리턴
        if (k === 0 && isNaN(s[i])) return s[i];
        
        if (!isNaN(s[i])) {
            count = Math.ceil(count / Number(s[i]));
        } else {
            count--;
        }
    }
};