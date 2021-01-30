// function solution(participant, completion) {
//   var answer = '';
//   participant.sort();
//   completion.sort();
//   // participant[i] = 'i+1'; completion[i] = 'i+1'
//   for (var i = 0; i < participant.length; i++) {
//     for (j = 'i+1'; (participant[i] = j); completion[i] = j) {
//       if (participant[i] != completion[i]) {
//         j = participant[i];
//         answer = participant[i];
//       }
//     }
//   }
//   console.log(answer);
//   return answer;
// }
// //1명 외 모두 완주
// // 전체명단 participant, 완주명단 completion
// // 그중에 완주하지 못한 선수 명단 answer return answer
// // p - c = a // a + c = p // p - a = c // 근데 결과값은 a가 되어야함
// // sort 해서 순서맞추고 - 같은 값 제거, // 두개를 비교? c[] = p[]
// // 순서대로 하기엔 뭐가 answer인지 모른다.

// solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']); // leo
// solution(
//   ['marina', 'josipa', 'nikola', 'vinko', 'filipa'],
//   ['josipa', 'filipa', 'marina', 'nikola']
// ); // vinko
// solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']); // mislav
// // 문자상, 순위상 우열이 없다. 인덱스로 번호를 지정해버려서

function solution(participant, completion) {
  var answer = '';
  participant.sort();
  completion.sort();
  console.log(participant);
  console.log(completion);
  for (var i = 0; i < participant.length; i++) {
    if (participant[i] !== completion[i]) {
      answer = participant[i];
      break;
    }
  }
  return answer;
}
solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']); // leo
solution(
  ['marina', 'josipa', 'nikola', 'vinko', 'filipa'],
  ['josipa', 'filipa', 'marina', 'nikola']
); // vinko
solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']); // mislav
// 문자상, 순위상 우열이 없다. 인덱스로 번호를 지정해버려서
