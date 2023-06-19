/** 
 * 네트워크의 수를 반환합니다. (간선으로 연결된 노드들의 경우)
 * @param {number} n - 컴퓨터 수
 * @param {number[][]} computers - 연결 여부 이중 배열
 * @return {number} - 네트워크 개수
 */
function solution(n, computers) {
    const visited = new Array(n).fill(false); // 방문 여부
    let count = 0; 

    // DFS
    const dfs = (node) => {
        visited[node] = true; // 방문 처리
        
        for (let i = 0; i < n; i++) {
            if (computers[node][i] === 1 && !visited[i]) { 
                // 연결되어 있고 방문하지 않았을 때
                dfs(i);             
            }
        }
    }
    
    for (let i = 0; i < n; i++) { // 컴퓨터 수만큼 진행
        if (!visited[i]) {
          dfs(i);
          count++;
        }
    }


    return count;
}
