// 최선의 선택: 그리디 Greedy
// - routes: [진입, 진출][]
// - 모든 차량의 경로가 카메라를 지나가기
function solution(routes) {
    var count = 1; // 시작 지점의 도착을 비추는 카메라
    
    routes.sort((a, b) => a[1] - b[1]); // 도착 기준 정렬
    let camera = routes[0][1]; // 카메라 => 도착 위치
    
    for (let i = 1; i<routes.length; i++) {
        const [entry, exit] = routes[i];
        
        // console.log(routes, routes[i],camera, entry > camera)
        if(entry > camera) {
            count++;
            camera = exit; // 카메라 => 도착 위치
        }
    }

    return count;
}