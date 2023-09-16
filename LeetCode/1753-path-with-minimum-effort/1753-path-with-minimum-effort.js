const minimumEffortPath = function(heights) {    
    // 그래프 + 최소 비용 경로 => 최소 우선 순위 큐
    /* min priority queue, 최소 우선순위 큐
    * enqueue: 원소를 큐에 삽입하고 해당 원소의 우선순위에 따라 정렬됩니다.
    * dequeue: 가장 높은 우선순위(최소값)를 가진 원소를 큐에서 제거하고 반환합니다.
    * peek: 가장 높은 우선순위(최소값)를 가진 원소를 제거하지 않고 반환합니다.
    * size: 큐에 있는 원소의 개수를 반환합니다.
    * isEmpty: 큐가 비어 있는지 여부를 확인합니다.
    */
    const mlen = heights.length;
    const nlen = heights[0].length;

    const visited = new Array(mlen).fill([]).map(e => new Array(nlen).fill(false));

    // up, down, left, right
    const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    const pq = new MinPriorityQueue({ priority: input => input[2] });

    let result = 0;

    pq.enqueue([0, 0, 0]);

    while (pq.size() > 0) {
        const [m, n, cost] = pq.dequeue().element;

        if (visited[m][n]) {
            continue;
        }

        result = Math.max(result, cost);
        visited[m][n] = true;

        if (m === mlen - 1 && n === nlen - 1) {
            return result;
        }

        for (const [dx, dy] of directions) {
            const x = m + dx;
            const y = n + dy;

            if (x >= 0 && x < mlen && y >= 0 && y < nlen) {
                const newCost = Math.abs(heights[m][n] - heights[x][y]);
                pq.enqueue([x, y, newCost]);
            }
        }
    }

    return -1;
};
