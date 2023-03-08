function solution(A, B) {
  if (A.length !== B.length) return -1
  
  let count = 0;
  while (A !== B && count < A.length) {
    A = A[A.length - 1] + A.substring(0, A.length - 1);
    count++;
  }
  return A === B ? count : -1;
}