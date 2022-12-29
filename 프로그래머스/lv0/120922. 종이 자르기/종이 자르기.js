function solution(M, N) {
    const Mcut = M - 1;
    const Ncut = (N - 1) * M;
    
    // 1. 한 쪽 변을 1까지 자름 => N - 1
    // 2-1. 다른 쪽 변을 1까지 자름 => M - 1
    // 2-2. 2-1을 1에서 잘린 갯수만큼 반복 => (M - 1) * 잘라진 한 쪽 갯수
    
    return Mcut + Ncut;
}