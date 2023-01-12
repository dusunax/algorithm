function solution(array) {
    const map = new Map();
    
    // map.set()
    for(let i = 0; i <= Math.max(...array); i++){
        map.set(i, 0);    
    }
    
    // array를 확인하며 키의 갯수를 구함
    for(let i = 0; i < array.length; i++){
        // map.set()
        // array의 i번째 요소 => 키
        // map의 해당 키의 해당하는 값 => +1
        map.set(array[i], map.get(array[i]) + 1);
    }
    
    // value를 배열로 놓고, max를 구함
    const arr = Array.from(map.values());
    const max = Math.max(...arr);
    
    // 최대 갯수 "max"의 인덱스 확인
    // 첫번째 index와 마지막 index가 같지 않다 === max와 같은 숫자가 존재 
    if(arr.indexOf(max) !== arr.lastIndexOf(max)){
        return -1;
    } else {
        // arr의 index === 0부터 시작하는 전체 길이만큼의 숫자
        return arr.indexOf(max);
    }
}