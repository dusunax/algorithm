/** 경수의 수 중, 귤 종류의 수가 최솟값인 경우 구하기 */
// 귤의 크기만큼 배열 생성 => 각 인덱스에 귤 갯수 세기 => 배열을 오름차순으로 정렬 => 필요한 귤 갯수만큼 인덱스 이동
// - k: 팔고 싶은 귤 수
// - tangerine: 귤의 크기 배열
function solution(k, tangerine) {
    // 가장 큰 귤
    const sizeCount = new Array(Math.max(...tangerine)+1).fill(0);
    
    // 귤 인덱스에 맞춰 갯수 세기
    for(let i = 0; i < tangerine.length; i++) {
        const current = tangerine[i];
        sizeCount[current] += 1;
    }
    sizeCount.sort((a, b) => b-a);
    
    // k만큼 고르기
    let index = 0;
    let answer = 0;
    while (k > 0) {
        k -= sizeCount[index];
        answer++; 
        index++;
    }
    
    // 계산이요
    return answer;
}