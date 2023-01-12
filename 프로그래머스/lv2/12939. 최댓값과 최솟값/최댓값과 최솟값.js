function solution(s) {
    let min = Math.min(...s.split(" "));
    let max = Math.max(...s.split(" "));
    return `${min} ${max}`;
}