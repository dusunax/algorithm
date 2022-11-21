function solution(array) {
    // 문자열로 바꿔서 7로 짜르고 자른 횟수(배열 길이) 체크
    return array.join('').split('7').length-1;
    
    // for문 2개
    // var answer = 0;
    // for(let x of array){
    //     for(let y of ""+x){
    //         y === '7' ? answer++ : '';
    //     }
    // }
    // return answer;
}