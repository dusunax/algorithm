/** 
* Bottom up 방식의 솔루션 
* 
* - 빈 병의 용량, 새 병으로 교환 가능한 병의 수, 남은 빈 병의 수를 매개변수로 받습니다.
* - 받을 수 있는 총 병 수를 return합니다.
*/
const solution = (empty, receive, bottleLeft) => {
  let totalBottle = 0; // 최종적으로 리턴할 수를 저장할 변수
  let remainBottle = bottleLeft; // 아직 반환하지 않은 병의 수
  
  while (remainBottle >= empty) { // 더 이상 교환이 불가능할 때까지 반복
    // 남은 빈 병으로 교환 가능한 병의 수를 계산
    let newBottle = Math.floor(remainBottle / empty) * receive;
    totalBottle += newBottle; // 최종으로 리턴할 병 수에 더함
    remainBottle = (remainBottle % empty) + newBottle; 
    // 교환 후 남은 빈 병 수 
  }
  
  return totalBottle;
}

//-------------------------------------------------------
/** 
* 재귀함수의 경우
* (RangeError: Maximum call stack size exceeded)
*/
const recursiveSolution = (empty, receive, bottleLeft) =>{
    let newBottle = Math.floor(bottleLeft / empty) * receive;
    let remainBottle = bottleLeft % empty;
    
    return newBottle + solution(empty, receive, remainBottle);
}