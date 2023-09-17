/**
 * @param {number[][]} graph
 * @return {number}
 */
var shortestPathLength = function(graph) {
    const numNodes = graph.length; 

    // 방문 리스트 배열 (비트 마스크)
    const distance = initialize2DArray(1 << numNodes, numNodes); 
    const queue = []; // BFS 큐
    let shortestPath = Number.MAX_SAFE_INTEGER; // 결과 변수 초기화

    // 모든 노드에서 시작하여 큐에 추가
    for (let startNode = 0; startNode < numNodes; startNode++) {
        queue.push([1 << startNode, startNode]); // (비트 마스크,현재 노드 인덱스)
    }

    // BFS: 가장 짧은 경로 찾기
    while (queue.length) {
        const [mask, currentNode] = queue.shift(); // 큐에서 비트 마스크와 현재 노드를 추출

        for (const neighbor of graph[currentNode]) {
            const neighborMask = mask | (1 << neighbor); // 다음 노드로 이동한 상태를 업데이트

            // 만약 이전에 방문하지 않은 노드인 경우
            if (distance[neighborMask][neighbor] === 0) {
                queue.push([neighborMask, neighbor]); // 큐에 다음 상태 추가
                distance[neighborMask][neighbor] = distance[mask][currentNode] + 1; // 거리를 업데이트
            }
        }
    }

    // 모든 노드를 방문하는 가장 짧은 경로의 길이
    for (let i = 0; i < numNodes; i++) {
        shortestPath = Math.min(shortestPath, distance[(1 << numNodes) - 1][i]);
    }
    return shortestPath;
};

/** 2차원 배열 초기화 */ 
var initialize2DArray = (rows, cols) => {
    const array = [];
    for (let i = 0; i < rows; i++) {
        const row = Array(cols).fill(0); // 0으로 초기화된 row 생성
        array.push(row);
    }
    return array; // 2차원 배열 반환
};
