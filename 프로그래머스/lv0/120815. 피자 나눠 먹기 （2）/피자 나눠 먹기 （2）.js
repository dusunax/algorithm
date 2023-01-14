function solution (n) {
    if(n % 6 === 0) return n / 6;
    console.log(n)
    
    for(let i = 1; i <= n; i++){
        if((i * 6) % n === 0) return i;
    }
}