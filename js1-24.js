function solution(n) {
  var answer = 0;
  for (let i = 0; i < n.length + 1; i++) {
    if ( n%i === 0 ) {
      answer += i;
    }
  }
  console.log( answer );
  return answer;
}

solution(12) // 28 - 1 2 3 4 6 12
solution(5) // 6 - 1 2 3 6