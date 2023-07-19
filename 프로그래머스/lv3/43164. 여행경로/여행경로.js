// DFS
// - 모든 경로: DFS
// - [a, b]: 공항 a -> 공항 b
// - 경로가 2 이상일 때: 알파벳 오름차순
function solution(tickets) {
    const answer = [];
    
    // 그래프 생성
    const graph = {};
    for (let [from, to] of tickets) {
        if (!(from in graph)) graph[from] = [];
        graph[from].push(to);
    }
    
    // to[]를 오름차순 정렬
    for (let airport in graph) {
        graph[airport].sort()
    }
    
    /**
     * 그래프 from: to[]
     * graph: { ICN: [ 'ATL', 'SFO' ], SFO: [ 'ATL' ], ATL: [ 'ICN', 'SFO' ] }
     */
    
    /** DFS */
    function dfs(node) {
        const nextNodes = graph[node];

        // 다음 노드들을 모두 탐색하며 to[]를 확인
        while (nextNodes && nextNodes.length > 0) {
            const nextNode = nextNodes.shift(); // 배열 shift: 알파벳 오름차순 다음 노드
                 
            dfs(nextNode);
        } 

        // 현재 노드 추가
        answer.push(node);
    }

    // 시작노드
    dfs("ICN");

    // 오름차순으로 shift 했기 때문에 마지막 경로가 가장 크므로 reverse();
    return answer.reverse();
}
