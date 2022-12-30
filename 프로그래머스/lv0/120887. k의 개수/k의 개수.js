function solution(start, end, number) {
    const strNum = ""+number
    let answer = 0;
    
    for (let i = start; i <= end; i++) {
        const arr = (""+i).split('');
        
        if(arr.includes(strNum)){
            arr.forEach( e => e === strNum ? answer += 1 : '' );
        }
    }
    
    return answer;
}