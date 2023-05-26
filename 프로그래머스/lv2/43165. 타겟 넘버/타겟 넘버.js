function solution(numbers, target) {
    let count = 0;
    dfs(0, 0); // DFS 호출 시작
    
    // DFS 깊이 우선 탐색, 완전 탐색
    function dfs(index, sum) {
        // 모든 숫자를 탐색 = index
        
        if (index === numbers.length) {
            // 타겟 넘버를 만든 경우 count를 증가하고 return
            if (sum === target) count++;
            return;
        }

        // 현재 숫자를 더하거나 빼는 경우를 *각각* 재귀적으로 호출
        dfs(index + 1, sum + numbers[index]);
        dfs(index + 1, sum - numbers[index]);
    }

    return count;
}
