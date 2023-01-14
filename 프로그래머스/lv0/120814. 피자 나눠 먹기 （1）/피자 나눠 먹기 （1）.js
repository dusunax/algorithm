function solution(n) {
    const pizza = 7;
    let count = 0;
    
    while(n > 0){
        n -= 7;
        count++;
    }
    
    return count;
}