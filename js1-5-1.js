function solution(answers) {
  var answer = [];
  //   var math = [
  //     [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
  //     [2, 1, 2, 3, 2, 4, 2, 5],
  //     [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
  //   ];
  var math1 = [1, 2, 3, 4, 5]; // 5
  var math2 = [2, 1, 2, 3, 2, 4, 2, 5]; // 8
  var math3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]; // 10
  var score = [0, 0, 0]; // 각 순번 인덱스에 점수 카운트 해서 배열화 // 가장 높은 카운트가
  // answers 갯수만큼 math생성
  for (var i = 0; i < answers.length; i++) {
    //math 0번배열의 i인덱스와 answers i인덱스가 같을 때
    if (math1[i % 5] == answers[i]) {
      // 일치 카운트 최종값을 스코어 배열 마지막에 넣어라
      score[0]++;
    }
    if (math2[i % 8] == answers[i]) {
      score[1]++;
    }
    if (math3[i % 10] == answers[i]) {
      score[2]++;
    } //score = [17, 23, 42];
  }
  console.log(score);
  // 스코어를 가장 높은 값을 탐색해서 // 가장 높은 값의 파라미터를 가져옴
  if (score[0] >= score[1] && score[0] >= score[2]) {
    answer.push(1);
  }

  if (score[1] >= score[0] && score[1] >= score[2]) {
    answer.push(2);
  }

  if (score[2] >= score[0] && score[2] >= score[1]) {
    answer.push(3);
  }

  //   score.max();
  //   answer.push(i);
  // 가장 높은 수의 파라미터를 가져옴
  // [i+1(수 맞춰주려고)] [1, 2, 3]
  // 순서에 맞게
  // 동점 이면 순차적으로 쌓아야함
  // 결과적으로 [1][2][3] [1,2,3] [1,2] [2,3] [1,3]이렇게 순서가 들어가야 함
  console.log(answer);
  return answer;
}
solution([1, 2, 3, 4, 5]);
solution([1, 3, 2, 4, 2]);
solution([1, 1, 1, 1, 1, 1, 1, 1, 1]);
solution([1, 3, 4, 5, 2, 3, 4, 2, 1, 4, 4, 5, 2, 3, 4]);
solution([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]);
solution([2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]);
solution([3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]);

function solution(answers) {
  var answer = [];
  var math1 = [1, 2, 3, 4, 5];
  var math2 = [2, 1, 2, 3, 2, 4, 2, 5];
  var math3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  var score = [0, 0, 0];
  for (var i = 0; i < answers.length; i++) {
    if (math1[i % 5] == answers[i]) {
      score[0]++;
    }
    if (math2[i % 8] == answers[i]) {
      score[1]++;
    }
    if (math3[i % 10] == answers[i]) {
      score[2]++;
    }
  }
  if (score[0] >= score[1] && score[0] >= score[2]) {
    answer.push(1);
  }
  if (score[1] >= score[0] && score[1] >= score[2]) {
    answer.push(2);
  }
  if (score[2] >= score[0] && score[2] >= score[1]) {
    answer.push(3);
  }
  return answer;
}
