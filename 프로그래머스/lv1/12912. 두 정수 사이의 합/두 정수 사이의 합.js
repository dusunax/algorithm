function solution(a, b) {
    let answer = 0;
    const numArr = a < b ? [a, b] : [b, a];
    
    for(let i = numArr[0]; i <= numArr[1]; i++) answer += i;
    return answer;
}