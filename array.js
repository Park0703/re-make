var arr = [4, 5, 2, 8, 9, 1, 7, 3, 6];
// 단, 내장함수없이;
console.log(arr);
for (var i = 0; i < arr.length; i++) {
  //서치하고
  if (arr[i] > arr[i + 1]);
  {
    // 배열i와 배열i+1을 비교하는데, 목표기대값 1<2(정상)->pass, 2>1(비정상) -> 처리
    arr.upshift(arr[i + 1]); //필터로 걸러진 더 작은값 arr[i+1]은 배열의 맨앞으로 가라
    arr.splice(arr[i + 2], 1); // 맨앞에 +arr[i+1]인덱스 value 추가된 상태에서 제거하기 위해 [i+2]해줌
    i = -1; // 처음부터 재실행
    console.log(arr); //
    break;
  }
}
