/**
* 1. for of 문과 indexOf 사용하기
* - 소요시간 평균: 1.07ms
* - 메모리 사용량 33.82MB
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
* - 소요시간 평균: 1.01ms
* - 메모리 사용량 평균: 33.8MB
*/
// function solution(name, yearning, photo) {
//     const result = [];
//     const yearningMap = new Map(name.map((key, idx) => [key, yearning[idx]]));

//     for (const persons of photo) { // 이중 배열 photo를 순회
//         let score = 0;
        
//         for (const person of persons) { // 각 사람 확인
//             const nameIdx = name.indexOf(person); 
//             if(nameIdx < 0) continue;           
            
//             score += yearningMap.get(person)
//         }
//         result.push(score);
//     }

//     return result;
// }

/**
* 3. 객체와 reduce를 사용하기
* - 소요시간 평균: 0.43ms
* - 메모리 사용량 평균: 33.7MB
*/
function solution(name, yearning, photo) {
    const yearningObj = {};

    name.forEach((key, idx) => { // obj에 key과 value 설정
        yearningObj[key] = yearning[idx];
    });

    return photo.map((persons) => {
        return persons.reduce((score, person) => { 
            // person이 yearningObj에 없다면 return
            if (yearningObj[person] === undefined) return score;

            return score += yearningObj[person];
        }, 0); // score를 0으로 초기화
    });
}