/**
* 방 배정 정보를 저장하는 Map 객체: assigned
* 각 고객에게 배정된 방 배열: answer
* @param {number} k - 호텔 방 개수
* @param {number[]} room_number - 고객이 원하는 방 번호 배열
* @returns {number[]} 각 고객에게 배정된 방 번호 배열
*/
function solution(k, room_number) {
    const answer = [];
    const assigned = new Map(); 
    // 대용량 데이터 삽입/삭제에서 Map이 빠르다 함

    for (let num of room_number) {
        answer.push(findRoom(num, assigned));
    }

    return answer;
}

/**
* 새로운 방 번호 또는 다음 빈 방 번호를 찾아서 반환합니다.
* @param {number} node - 찾으려는 방 번호
* @param {Map} assigned - 각 방 번호에 대응하는 다음 빈 방 번호를 저장하는 Map 객체
* @returns {number} 새로운 방 번호 또는 다음 빈 방 번호
*/
function findRoom(node, assigned) {
    let target = assigned.get(node);

    // 새로운 방 번호인 경우
    if (target === undefined) {
        assigned.set(node, node + 1);
        return node;
    }   

    // 다음 빈 방 번호를 찾아서 반환
    let nextNode = findRoom(target, assigned);
    assigned.set(node, nextNode + 1);
    
    return nextNode;
}
