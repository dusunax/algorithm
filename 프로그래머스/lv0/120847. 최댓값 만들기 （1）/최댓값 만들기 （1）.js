function solution(numbers) {
    const desc = numbers.sort((a,b)=>b-a);
    
    return desc[0] * desc[1];
}