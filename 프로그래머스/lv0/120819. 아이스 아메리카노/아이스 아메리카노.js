function solution(money) {
    if(!money || isNaN(money)) return;
    
    const price = 5500;
    const count = parseInt(money / price)
    const moneyLeft = money % price;
    
    return [count, moneyLeft];
}