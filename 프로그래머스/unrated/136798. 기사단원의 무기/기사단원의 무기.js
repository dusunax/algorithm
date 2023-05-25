function solution(number, limit, power) {
    const div = [];
    
    for (let j = 1; j <= number; j++) {
        let cnt = 0;
        for (let i = 1; i <= Math.sqrt(j); i++) {
            if (j === i ** 2) {
                cnt += 1;
            } else if (j % i === 0) {
                cnt += 2;
            }
        }

        div.push(cnt);
    }
    
    const answer = div.reduce((sum, i) => sum + (i <= limit ? i : power), 0);
    return answer;
}
