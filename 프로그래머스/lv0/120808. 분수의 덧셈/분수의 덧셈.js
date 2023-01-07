function solution(denum1, num1, denum2, num2) {
    var answer = [0, 0]; // 기약분수의 분자, 분모
    
    // ## 기약 분수란? Irreducible Fraction
    // 분자와 분모의 공약수가 1 뿐이어서, 더 이상 약분되지 않는 분수입니다.
    
    // ## 약분이란? Reduction of a fraction
    // 분자와 분모를 1 이외의 공통된 약수로 나누는 행위를 약분이라고 합니다.
    
    // ## 즉-
    // 정수 a, b에 대해 분수 a/b가 기약분수라는 것과, 
    // a, b가 서로소 즉, 최대공약수가 1이라는 것은 같은 말입니다.
    // (약분이 1 이외에 더 이상 가능하지 않습니다.)
    
    // 공약수 Greatest Common Factor, 줄여서 GCF는 GCD라고도 합니다. Greatest Common Divisor
    
    // -----------------------------------------
    // 1 / 2 + 3 / 4 일 때,
    let first = num1 * denum2 + num2 * denum1; 
    // - 분자: (1 * 4) + (3 * 2) 
    let second = num1 * num2;
    // - 분모: 2 * 4
    
    let gcd = (a, b) => (a % b === 0 ? b : gcd(b, a % b));
    // ## 최대공약수 gcd를 구하는 함수
    // 상단에서 구한 분자와 분모를 사용합니다.
    // 분자를 분모로 나눴을 때, 나머지가 0이라면? 최대 공약수는 분모입니다.
    // 나머지가 0이 아니라면? 다시 gcd 함수를 재귀 실행합니다.
    // 나머지가 0이 될때까지 구합니다.
    
    // 10 / 8 분수를 확인했을 때, 10 % 8 === 2 이므로 재귀합니다.
    // => 다음 분수는 8 / 10 % 8
    
    // 8 / 2 분수를 확인했을 때, 8 % 2 === 0 이므로
    // => 최대 공약수는 분모입니다.
    // 즉, 2입니다.
    
    let min = gcd(first, second);
    // 최대공약수 구하기(분자, 분모)
    
    console.log(min)
    
    // 기약 분수의 분자
    // 분자를 최대 공약수로 나눕니다.
    answer[0] = first / min; 
    
    // 기약 분수의 분모
    // 분모를 최대 공약수로 나눕니다.
    answer[1] = second / min; 

    return answer;
}