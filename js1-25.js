function solution(words) { // words는 가장 큰 덩어리
  let answer = [];
  words1 = words.split(" ");
  let i = 0;
  let words2 = words1[i]

for (let i = 0; i < words2.length; i++) {
  for (let j = 0; j < words2.length; i++) {
    if ( j === 0 || j % 2 === 0 ) { // 0과 짝수 이면
      answer.push(words2.slice(j, j+1).toUpperCase());
    } else {
      answer.push(words2.slice(j, j+1));
    }
  }}
  console.log(answer);
  
return answer.join("")
}

solution("trys hello world") 

// function solution(words) { // words는 가장 큰 덩어리
//   let answer = '';
//   let words1 = words.split(' ') // 외곽 배열만듬
//   let words2 = []
//   for (let i = 0; i < words1.length; i++) {
//   words2.push(words1[i].split('')); // 내부 이중배열 만듬
//   }

//   // 이중배열 안에 배열의 각 인덱스를 수정
//   for (let i = 0; i < words2.length; i++) { 
//       for (let j = 0; j < words2[i].length; j++) {
//          if ( j == 0 || j % 2 == 0 ) {
//       words2[i][j].toUpperCase();  // 단어 내 특정 글자
// console.log(words2);
//   }
// }
// } 
// for (let i = 0; i < words2.length; i++) { 
//  answer = words2.join("")          
// }                
// return answer
// }