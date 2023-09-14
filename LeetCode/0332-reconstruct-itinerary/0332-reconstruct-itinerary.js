/**
 * @param {string[][]} tickets
 * @return {string[]}
 */
var findItinerary = function(tickets) {
    // 항공권
    // 모든 경로 탐색: DFS
    const graph = {};
    
    // 항공권 목록 => 그래프
    for (const [from, to] of tickets) {
        if (!graph[from]) graph[from] = [];
        graph[from].push(to);
    }
    
    // lexical order, reverse
    for (const key in graph) {
        graph[key].sort().reverse(); 
    }
    
    // 여행 경로 배열
    const itinerary = [];
    
    // DFS
    function dfs(airport) {
        while (graph[airport] && graph[airport].length > 0) {
            // 도착지를 스택에서 꺼내 재귀탐색
            dfs(graph[airport].pop());
        }
        itinerary.push(airport); // 현재 공항 추가
    }
    
    dfs("JFK");
    
    return itinerary.reverse(); // 왜 뒤집냐 => 스택에서 역순으로 쌓이기 때문
};