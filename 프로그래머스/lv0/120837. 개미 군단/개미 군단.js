function solution(hp) {
    var count = 0;
    
    while (hp) {
        if(hp < 3){
            hp --;
        } else if (hp < 5) {
            hp -= 3;
        } else {
            hp -= 5;
        }
        count++;
    }
    
    return count;
}