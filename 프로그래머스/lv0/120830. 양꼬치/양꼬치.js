function solution(n, k) {
    const paidK = k - parseInt(n / 10);
    const menu = {
        lamb: 12000,
        drink: 2000
    };
    
    return (n * menu.lamb + paidK * menu.drink);
}