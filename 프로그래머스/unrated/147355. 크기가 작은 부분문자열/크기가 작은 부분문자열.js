function solution(t, p) {
    var answer = 0;
    
    let length = t.length - p.length;
    let countUp = 0;
    
    while (length >= countUp){
        let val = t.slice(countUp, countUp + p.length);
        p >= val && answer++;
        
        countUp++;
    }
    return answer;
}