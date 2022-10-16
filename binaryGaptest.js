function solution(N) {
  const binary = N.toString(2);

  let MaxGapInBinary = 0;
  let FlagCount = false;
  let LongBinary = binary.length;
  let MaxGapProspect = 0;
  for (var i = 0; i < LongBinary; i++) {
    if (binary[i] == 1) {
      if (FlagCount) {
        FlagCount = false;
        MaxGapInBinary = Math.max(MaxGapInBinary, MaxGapProspect);
      } else {
        FlagCount = true;
        MaxGapProspect=0;
      }
    } else {
      if (FlagCount) {
        MaxGapProspect++;
      }
    }
  }

  return MaxGapInBinary;
}

solution(9);

console.log(solution(9));
