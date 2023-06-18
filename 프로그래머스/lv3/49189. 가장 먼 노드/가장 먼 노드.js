function solution (n, edges) {
    const graph = Array.from({ length: n + 1 }, () => []);

    // 그래프 생성
    edges.forEach(([a, b]) => {
        graph[a].push(b);
        graph[b].push(a);
    });
    
    const visited = Array(n + 1).fill(false); // 방문 여부 배열
    const distances = Array(n + 1).fill(0); // 1번 노드 로부터의 거리 배열

    // BFS 시작
    const queue = [1];
    visited[1] = true;

    while (queue.length > 0) {
        const node = queue.shift();

        graph[node].forEach((nextNode) => {
            if (!visited[nextNode]) {
                queue.push(nextNode);
                
                visited[nextNode] = true;
                distances[nextNode] = distances[node] + 1;
            }
        });
    }

    const longestNodes = distances.filter((distance) => distance === Math.max(...distances))
    return longestNodes.length;
}