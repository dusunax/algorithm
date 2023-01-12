function solution(num) {
    var answer = 0;
    var k = 0;

    while((k*(k-1)/2)<=num){
      if(Number.isInteger((num/k)-(k-1)/2) && ((num/k)-(k-1)/2 != 0)){
        answer++;
      }
      k++;
    }

    return answer;
}