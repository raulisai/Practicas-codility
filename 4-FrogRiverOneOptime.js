function solution(X, A) {
  const occupiedPositions = new Map();
  let totalSum = (X * (X + 1)) / 2;
 console.log(occupiedPositions.has(A[0]))
  for (let i = 0; i < A.length; i++) {
    if (!occupiedPositions.has(A[i]) && A[i] <= X) {
      occupiedPositions.set(A[i], true);
      totalSum -= A[i];
      console.log(totalSum)
      if (totalSum === 0) {
        return i;
      }
    }
  }
  return -1;
}



console.log(solution(5,[1,3,6,1,4,2,3,5,4,6,7,8]))
