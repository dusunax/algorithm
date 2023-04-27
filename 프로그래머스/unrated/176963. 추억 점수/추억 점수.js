/**
* 1. for of 문과 indexOf 사용하기
*/
// function solution(name, yearning, photo) {
//     const result = [];

//     for (const persons of photo) { // 이중 배열 photo를 순회
//         let score = 0;
        
//         for (const person of persons) { // 각 사람 확인
//             const nameIdx = name.indexOf(person); 
//             if(nameIdx < 0) continue;           
            
//             score += yearning[nameIdx];
//         }
//         result.push(score);
//     }

//     return result;
// }

/** 
* 2. for of 문과 map 사용하기
*/
function solution(name, yearning, photo) {
    const result = [];
    const yearningMap = new Map(name.map((key, idx) => [key, yearning[idx]]));

    for (const persons of photo) { // 이중 배열 photo를 순회
        let score = 0;
        
        for (const person of persons) { // 각 사람 확인
            const nameIdx = name.indexOf(person); 
            if(nameIdx < 0) continue;           
            
            // score += yearning[nameIdx];
            score += yearningMap.get(person)
        }
        result.push(score);
    }

    return result;
}
