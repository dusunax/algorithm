function solution(s) {
    const half = s.length / 2;
    
    return Number.isInteger(half) ? s[half-1]+s[half] : s[Math.floor(half)];
}