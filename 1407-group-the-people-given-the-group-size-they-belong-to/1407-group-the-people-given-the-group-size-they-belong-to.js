/**
 * @param {number[]} groupSizes 
 * @return {number[][]}
 */
var groupThePeople = function(groupSizes) {
    const groups = {}; // 그룹 저장
    const result = [];

    for (let i = 0; i < groupSizes.length; i++) {
        const size = groupSizes[i]; // current group size
        if (!groups[size]) groups[size] = []; // 그룹이 없으면 초기화
        
        groups[size].push(i); // 현재 사람을 그룹에 추가
        
        // 그룹 완성 => 결과 배열에 추가하고 그룹 초기화
        if (groups[size].length === size) {
            result.push([...groups[size]]);
            groups[size] = [];
        }
    }
    
    return result;
};
