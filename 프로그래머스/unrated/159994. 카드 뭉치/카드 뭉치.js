function solution(cards1, cards2, goal) {
    for (const word of goal) {
        if (cards1.length + cards2.length === 0) return "No";
        
        const c1 = cards1[0];
        const c2 = cards2[0];
        
        if(c1 === word || goal.indexOf(c1) < 0) cards1.shift();
        if(c2 === word || goal.indexOf(c2) < 0) cards2.shift();
        
        if (c1 !== word && c2 !== word) return "No";
    }
    return "Yes";
}

// 오늘의 기억할 점

// 1. 오탈자와 불리언(boolean)
// `cards1.lenth`와 같이, 프로토타입에 없는 속성을 사용하면, 해당 메소드는 undefined가 됩니다..
// 따라서 `cards1.lenth === 0`와 같이 불리언 조건문을 확인할 때, 메소드명에 오탈자가 있다면 항상 `false`가 반환됩니다.

// 2. 빈 배열 확인하기
// - 빈 배열 `[]`은 true인 값입니다.
//   따라서 다음과 같이 확인할 수 없습니다.
//   ```
//   if (!cards1 && !cards2) return "Yes";
//   ```
// - 빈 배열 `[]`의 length는 숫자입니다.
//   따라서 다음과 같이 확인할 수 있습니다.
//   ```
//   if (cards1.length + cards2.length === 0) return "Yes";
//   ```