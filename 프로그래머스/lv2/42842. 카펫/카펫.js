function solution(brown, yellow) {
    // 1번 방법이 효율적
    
    // 1. yellow로 구할 때
    for (let h = 1; h <= Math.sqrt(yellow); h++) {
        // 1부터 yellow 약수까지 확인
        // yellow를 h로 나눈 값이 정수일 때
        const w = yellow / h;
        
        if (Number.isInteger(w)) {
            console.log(brown, w, h, (w + h) )
            
            // 카펫 둘레
            // (w + h) * 2 + 4가 brown과 일치하면 [가로, 세로] 반환
            if (brown === (w + h) * 2 + 4) {
                return [w + 2, h + 2];
            }
        }
    }
    
    // 2. brown과 yellow
    // 가로+세로/2 모든 크기의 경우를 구하고, 일치하는 경우 확인
//     for (let w = 3; w <= (brown + yellow) / 2; w++) {
//         const h = (brown + yellow) / w;

//         // h가 정수 integer이며, yellow와 같을 때 [가로, 세로] 반환
//         if (Number.isInteger(h) && (w - 2) * (h - 2) === yellow) {
//             return [h, w];      
//         }
//     }
}
