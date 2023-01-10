function solution(array) {
    const middleIdx = (array.length + 1) / 2 - 1;
    
    return array.sort((a, b)=>a-b)[middleIdx];
}