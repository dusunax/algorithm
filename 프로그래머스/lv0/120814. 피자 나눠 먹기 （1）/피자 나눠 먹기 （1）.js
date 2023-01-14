function solution(n) {
    // 1. 풀이
    // 사람(n)을 피자(7)로 나눔
    // 나눈 수를 올림
    // return Math.ceil(n / 7)
    
    // 2. 피자 먹기
    const pizza = 7;
    let count = 0;
    
    while(n > 0){
        n -= 7;
        count++;
    }
    
    return count;
}