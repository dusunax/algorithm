function solution(M, N) {
    const Mcut = M - 1;
    const Ncut = (N - 1) * M;
    
    // 방법 A
    // 1. 한 쪽 변을 1까지 자름 => N - 1
    // 2-1. 다른 쪽 변을 1까지 자름 => M - 1
    // 2-2. 2-1을 1에서 잘린 갯수만큼 반복 => (M - 1) * 잘라진 한 쪽 갯수
    // Mcut + Ncut
    
    // 방법 B
    // 방법 A에서 알 수 있듯이, 
    // 한쪽 변은 -1만큼 자르고, 
    // 다른쪽 변은 "한쪽 변이 잘린 갯수"만큼 자릅니다.
    // 따라서 "M x N - 1" 은 (M - 1) + ((N - 1) * M)과 같은 결과를 가집니다. 
    
    return Mcut + Ncut;
}