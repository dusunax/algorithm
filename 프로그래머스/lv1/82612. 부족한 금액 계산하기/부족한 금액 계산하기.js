function solution(price, money, count) {
    while(count){
        money -= (price * count);
        count--;
    }
    
    return money = money < 0 ? Math.abs(money) : 0;
}