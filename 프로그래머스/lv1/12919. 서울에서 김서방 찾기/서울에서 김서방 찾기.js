function solution(seoul) {
    // "Kim"이 확실하다면 사용, indexOf로 문자열을 직접 찾기.
    // const findedIndex = seoul.indexOf('Kim');
    
    // 예외처리: toLowerCase로 대소문자 체크
    // findIndex()에 search 함수를 사용하여 찾기.
    const search = name => name.toLowerCase() === "kim";
    const findedIndex = seoul.findIndex(search);
    
    return `김서방은 ${findedIndex}에 있다`;
}