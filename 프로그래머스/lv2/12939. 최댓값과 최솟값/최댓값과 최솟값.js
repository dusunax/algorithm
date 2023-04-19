function solution(s) {
    const min = Math.min(...s.split(" "));
    const max = Math.max(...s.split(" "));
    return `${min} ${max}`;
}