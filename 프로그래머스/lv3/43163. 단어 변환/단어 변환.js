// 가장 짧은 경우 찾기: BFS
// BFS는 Quque
function solution(begin, target, words) {
    if (!words.includes(target)) return 0; // 없는 경우 얼리리턴
    // [[첫 단어, count 초기화]]
    const queue = [[begin, 0]]; 
    
    // queue 길이 만큼 돌리기
    // FIFO: enqueue, dequeue
    while (queue.length) {
        const [word, count] = queue.shift();
 
        // 이번 queue 처리(word === target 확인)
        if (word === target) return count;
        
        words.forEach((currentWord, i) => {
            // 이번 배열 요소의 알파벳 체크
            const differ = Array.from(currentWord).reduce((acc, cur, i) => acc + (cur !== word[i]), 0);
            
            // 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
            if (differ === 1) {
                queue.push([currentWord, count+1]);
                
                // swap해서 pop하는 이유
                // - slice(): O(n)
                // - 마지막 요소를 pop(): O(1)
                words[i] = words[words.length-1];
                words.pop();
            }
        });
    }
    return 0;
}
