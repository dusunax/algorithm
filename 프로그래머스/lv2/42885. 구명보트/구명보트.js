// 그리디
// - 가장 무거운 사람과 가벼운 사람 더한 후, 무게<=100 확인하기
function solution(people, limit) {
    let answer = 0;
    let left = 0;
    let right = people.length - 1;

    people.sort((a, b) => a - b);

    // 양쪽에서 중앙으로 이동
    // (가장 가벼운 사람 + 가장 무거운 사람)
    // - 탈 수 없으면 보트 1대 추가
    // - 탈 수 있으면 left 한 번 이동(탔으니까)
    while (left <= right) {
        if (people[left] + people[right] <= limit) {
            left++;
        }
        right--;
        
        answer++; // 보트 추가요
    }

    return answer;
}
