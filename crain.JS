function solution(board, moves) {
  var answer = 0;
  var storage = [];
  for (var i = 0; i < moves.length; i++) {
    for (var j = 0; j < board.length; j++) {
      if (board[j][moves[i] - 1] !== 0) {
        storage.push(board[j][moves[i] - 1]);
        board[j].splice(moves[i] - 1, 1, 0);
        break;
      }
    }
  }
  for (var i = 0; i < storage.length; i++) {
    if (storage[i] == storage[i + 1]) {
      storage.splice(i, 2);
      answer += 2;
      i = -1;
    }
  }
}
