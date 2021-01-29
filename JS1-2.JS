// 정수배열 numbers[],
// 내용 인덱스에 두개 뽑아서
// numbers[i] + numbers[j] 서로 다 른합수의 조합 배열을 오름차순
//

function solution(numbers) {
  var answer = [];
  for (var i = 0; i < numbers.length; i++; j = 0; j < numbers.length; j++)  {
    //j는 i와 다른 수로 돌리고  j=i+1;
    if (numbers[i] != numbers[j]) {
      // [i], [j]가 서로 다른 인덱스이면
      answer.push(numbers[i] + numbers[j]); // 더해서 answer의 배열로 넣어라

    
    }
  }
  //이때 배열을 오름차순으로 만들어라
  for (var i = 0; i < answer.length; i++) {
    //서치하고
    if (answer[i] > answer[i + 1]);
    {
      // 배열i와 배열i+1을 비교하는데, 목표기대값 1<2(정상)->pass, 2>1(비정상) -> 처리
      answer.upshift(answer[i + 1]); //필터로 걸러진 더 작은값 arr[i+1]은 배열의 맨앞으로 가라
      answer.splice(answer[i + 2], 1); // 맨앞에 +arr[i+1]인덱스 value 추가된 상태에서 제거하기 위해 [i+2]해줌
      i = -1; // 처음부터 재실행
      console.log(answer);
      return answer;
    }
  }
}
solution([2, 1, 3, 4, 1]);
solution([5, 0, 2, 7]);
