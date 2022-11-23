function solution(my_string) {
    // map에서 해결
    // var answer = 0
    // my_string.split("").map(str => isNaN(str) ? "" : answer += +str)
    
    // filter와 reduce를 사용해서 코드에 대한 이해도가 높음(알아보기 쉬움)
    return my_string.split("").filter(str => !isNaN(str)).reduce((a, c) => +a + +c);
}