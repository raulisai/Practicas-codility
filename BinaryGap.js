//Binary Gap

function solution(N) {
    let binary = N.toString(2);
  
    let escapesProspect = 0;
    let escapes = 0;
    let banderaConteo = true;
  
    for (let i = 0; i <= binary.length; i++) {
      if (binary[i] == 0 && banderaConteo) {
        if (banderaConteo) {
          escapesProspect++;
        }
      }
  
      if (binary[i] == 1) {
        if (banderaConteo && binary[i - 1] == 0) {
          binary[i + 1] == 0 ? banderaConteo: banderaConteo = false;
          escapesProspect > escapes
            ? (escapes = escapesProspect)
            : escapes == 0
            ? (escapes = escapesProspect):
  
          escapesProspect = 0;
        } else {
          banderaConteo = true;
        }
      }
    }
    return escapes;
  }
  console.log(solution(66561));
  test();
  
  function test() {
    let test = [9, 20, 15];
    let resulTest = [2, 1, 0];
  
    const Resultados = [solution(test[0]),solution(test[1]),solution(test[2])];
  
  
    for (let i = 0; i <= test.length; i++) {
      if (resulTest[i] == Resultados[i]) {
        console.log("Test " + i + " - Aproved");
      } else {
        console.log("Test " + i + " - Failed");
      }
    }
  }
  