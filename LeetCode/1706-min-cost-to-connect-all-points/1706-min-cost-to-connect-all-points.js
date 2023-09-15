/**
 * @param {number[][]} points
 * @return {number}
 */
var minCostConnectPoints = function(points) {
    // 두 점을 연결, 최소 비용
    let cost = 0;
    const len = points.length;
    const distance = Array(len).fill(Infinity); // 초기화 as Infinity
    distance[0] = 0;
    let next = 0;

    for (let step = 1; step < len; step++) {
        let min = Infinity;
        let point = -1; // index reset

        for (let i = 1; i < len; i++) {
            if (distance[i] > 0) {
                distance[i] = Math.min(distance[i], Math.abs(points[i][0] - points[next][0]) + Math.abs(points[i][1] - points[next][1]));

                // 더 작은 거리를 찾는 경우
                if (distance[i] < min) {
                    min = distance[i]; 
                    point = i;
                }
            }
        }

        cost += min; // 비용을 누적 = 반환값
        distance[point] = 0; // 방문 표시
        next = point; // 다음 vertex 업데이트
    }
    
    return cost;
};