function solution(n, k) {
    const paidK = k - parseInt(n / 10);
    const menu = {
        lamb: 12000,
        drink: 2000
    };
    
    // ## javaScript의 Ti
    
    // 32비트 변환 후 NOT 연산 : 즉, n이라면 -(n+1)이다.
    // 소숫점을 제거한다.
    
    // ~~를 사용하면 parseInt와 같은 결과지만,
    // 음수에서 다른 값이 나올 수 있다.
    // ex) Math.floor(-5.9) === -5
    //     ~~(5.9) === -6
    
    // ES7(2016)에서 includes가 나오기 전,
    // js의 배열에서 str.indexOf()값이 참인지 확인할 때 사용했었다.
    
    // k -= ~~(n / 10);
    
    return (n * menu.lamb + paidK * menu.drink);
}
