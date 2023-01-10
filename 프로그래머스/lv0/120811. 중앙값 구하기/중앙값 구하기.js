function solution(array) {
    const middleIdx = (array.length + 1) / 2 - 1;

    // index 확인법 A.
    // return array.sort((a, b)=>a-b)[middleIdx];
    
    // index 확인법 B.
    // 체이닝이 가독성이 더 높은 것 같습니다.
    return array.sort((a, b)=>a-b).at(middleIdx);
}