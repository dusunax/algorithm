function solution(n) {
    return (""+n).split("").reduce((p, c) => +p + +c, 0);
}