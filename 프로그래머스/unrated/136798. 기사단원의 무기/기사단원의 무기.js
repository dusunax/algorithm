function solution(number, limit, power) {
    const div = []; // 약수 갯수를 저장하는 배열
    
    // 1부터 number까지, 각 *j*에 대한 약수 갯수 계산
    for (let j = 1; j <= number; j++) {
        let cnt = 0;
        
        // j의 제곱근까지의 약수를 확인
        let sqrt = Math.sqrt(j);
        for (let i = 1; i <= sqrt; i++) {
            if (j === i ** 2) { // 완전 제곱수인 경우, 약수 갯수 1 증가 ex) 1, 4, 9...
                cnt += 1;
            } else if (j % i === 0) { // i가 j의 약수인 경우, 약수 개수 2 증가
                cnt += 2;
            }
        }

        div.push(cnt);
    }
    
    // limit = 제한 수치인 경우, 제한 수치를 구매
    const answer = div.reduce((sum, i) => sum + (i <= limit ? i : power), 0);
    
    return answer;
}
