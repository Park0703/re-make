function solution(new_id) {
  var answer = '';

  var array = [];

  new_id = new_id.toLowerCase();

  new_id = new_id.replace(
    /[\~\!\@\#\$\%\^\&\*\(\)\=\+\[\{\]\}\:\?\,\<\>\/]/gi,
    ''
  );
  array = new_id.split('');
  for (var i = 0; i < array.length; i++) {
    if (array[i] == array[i + 1]) {
      if (array[i] == '.') {
        array.splice(i, 1);
        i = i - 1;
      }
    }
  }

  if (array[0] == '.') {
    array.splice(0, 1);
  }
  if (array[array.length - 1] == '.') {
    array.splice(array.length - 1, array.length);
  }
  if (array.length == 0) {
    array.push('a');
  }
  if (array.length >= 16) {
    array.splice(15);
  }
  if (array[array.length - 1] == '.') {
    array.splice(array.length - 1, array.length);
  }
  for (var i = 0; i < array.length; i++) {
    if (array.length <= 2) {
      array.push(array[array.length - 1]);
    }
  }
  answer = array.join('');

  return answer;
}

// function solution(new_id) {
//   var answer = '';
//   // 1)lower 대문자를 소문자로 치환
//   answer = new_id.toLowerCase();
//   // 2) 허용문자(lowerint-_.)이외 모두제거
//   answer = answer.replace(
//     /[\~\!\@\#\$\%\^\&\*\(\)\=\+\[\{\]\}\:\?\,\<\>\/]/gi,
//     ''
//   );
//   // 3)  ..연속이면 .로 치환
//   for (var i = 0; i < answer.length; i++) {
//     answer = answer.replace('..', '.');
//   }
//   // 4). 처음 끝이면 제거
//   if (answer.substring(0, 1) == '.') {
//     answer = answer.substring(1, answer.length);
//   }
//   if (answer.substring(answer.length - 1) == '.') {
//     answer = answer.substring(0, answer.length - 1);
//   }
//   // 5) replace 빈문자열이면 a 대입
//   if (answer.length == 0) {
//     answer = answer + 'a';
//   }
//   // 6) 길이 >= 16이면, 이후 문자전부 제거
//   if (answer.length >= 16) {
//     answer = answer.substring(0, 15);
//   }
//   // 7) 제거후 끝에 .이 있으면 제거
//   if (answer.substring(answer.length - 1) == '.') {
//     answer = answer.substring(0, answer.length - 1);
//   }
//   // 8) 길이가 2자 이하면, 마지막 문자를 아이디길이가 3이 될때까지 반복해서 끝에 붙임
//   for (var i = 0; i < answer.length; i++) {
//     if (answer.length <= 2) {
//       answer = answer + answer.substring(answer.length - 1, answer.length);
//     }
//   }
//   console.log(answer);
//   return answer;
// }
solution('...!@BaT#*..y.abcdefghijklm');
solution('z-+.^.');
solution('=.=');
solution('123_.def');
solution('abcdefghijklmn.p');
solution('@@@@@@@@');
solution('@23');
solution('................');
