function solution(hp) {
    let count = 0;
    
    // 수학적으로 풀이
    // 5로 나눈다. 5가 들어가는 횟수를 구한다.
    // 5로 나눈 나머지를, 3으로 나눈다. 나눠지거나(1) 나눠지지(0) 않는 경우가 있음.
    // 5로 나눈 나머지를, 3으로 나눈 나머지를 구한다. (2 ~ 0)
    count = parseInt(hp / 5) + parseInt(hp % 5 / 3) + parseInt((hp % 5) % 3)
    
    // 지문 그대로 반복문
    // while (hp) {
    //     if(hp < 3){
    //         hp --;
    //     } else if (hp < 5) {
    //         hp -= 3;
    //     } else {
    //         hp -= 5;
    //     }
    //     count++;
    // }
    
    return count;
}