function solution(n) {
    // 런타임 에러로 인해 주석 처리
    // const fibFn = recursiveCachedFibonacci();
    // return fibFn(n) % 1234567;
    
    return fibonacci(n) % 1234567;
}

/** 
* 반복문을 사용하는 피보나치 함수입니다.
* - 작은 문제부터 해결하는 Bottom-up 방식
*/
function fibonacci(n) {
    // a = 이전 값, 0부터 시작
    // b = 현재 값, 1부터 시작
    // c = 피보나치 계산 값
    let a = 0, b = 1, c;
    
    // 항상 2 이상의 값이 입력됩니다.
    for (let i = 2; i <= n; i++) { // 2부터 n까지 for문을 돌립니다.
        c = (a + b) % 1234567; // 피보나치를 계산
        a = b; // 이전 값 갱신
        b = c; // 현재 값 갱신
    }
    return b; // 현재 값(n번째 피보나치 값) 을 반환합니다.
}

/** 
* 재귀를 사용하는 피보나치 함수입니다.
* - cache 객체 사용
* - 테스트 13, 14에서 런타임 에러 발생
*/
function recursiveCachedFibonacci(){
    let cache = {};
  
    return function a(n){
        if(n in cache){
            return cache[n] // 캐싱된 값이 있다면 return
        } else {
            // 항상 2 이상의 값이 입력됩니다.
            if(n <= 2) {
                cache[n] = 1; 
            } else {
                // 기본 피보나치 => cache[n] = a(n - 1) + a(n - 2); 
                cache[n] = (a(n - 1) % 1234567) + (a(n - 2) % 1234567);
            }

            return cache[n] %= 1234567; // 결과 리턴
        }
    } 
}
