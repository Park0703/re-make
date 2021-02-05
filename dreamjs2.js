'use strict'; // 모던하게 하자구~
// 2. variable (read/write)

// application 마다 비어있는 메모리가 있는데 let으로 지정
// blockscope(안에) globalscope(밖에) - 최소한의 메모리에 지정
// var는 선언하기도 전에(undefined)도 출력할 수 있음. 그래서 안됨
// var hoisting - 어디에서 선언했든 제일 위로 끌어올림(globalscope)
// blockscope을 무시함, 그래서 규모가 커지면 정밀성이 떨어짐
// es6는 호환성이 좋아 쓸수있음
let name; // es6의 var

// 3. constants const (read)
// 지정한 메모리를 변경불가능하게 잠궈버림, 강한 let
// mutable로 변경이 가능하면 바이러스에 취약함.
// immutable : security, thread safety(변수요소), reduce human mistakes

// 4. variable type
// primitive, 더이상나뉠 수 없는 single item(number, string, boolean 등)
// object : item을 묶어서 만든 것
// function 데이터 타입중 하나임, first-class function

// number type이면 끝 심지어 선언하지 않아도 됨. vs c, java
//
// const infinity = 1 / 0;
// const negativeinfinity = -1 / 0;
// const nAn = 'not a number' / 2;
// console.log(infinity);
// concole.log(negativeinfinity);
// console.log(nAn);
// 원래는 2**52<int<2**52까지만 표시할 수 있는데, 넘으면 마지막에 n만 붙이면 bigint 설정을 함
// 123123124214325235522152315231532152153215321500n 최신이라, 아직 쓰이는 곳은 많지 않음

// string
//template literals
const grendan = 'bitch';
const hellobob = `hi ${grendan}!`; //hi brendan! 값이 나옴
//null vs undefined
let nothing = null;
let x; // = undefined;
console.log(`value : ${nothing}, type: ${typeof nothing}`);
console.log(`value : ${x}, type: ${typeof x}`);

//symbol, create unique identifiers for objects
// symbol : map이나 자료구조에서 고유 식별이 필요하거나, conquer한 걸 쓸때, 우선순위 부여할때
// const symbol1 = symbol('id');
// const symbol2 = symbol('id');
// console.log(symbol1 === symbol2); // true

//  ★ 5. dynamic typing : 좋은 아이디어를 프로토타입을 만들때 좋음, 협업할땐 좋지 않음
let text = 'hello';
console.log(text.charAt(0));
console.log(`value:${text}, type:${typeof text}`);
text = 1;
console.log(`value:${text}, type:${typeof text}`);
text = '7' + 5;
console.log(`value:${text}, type:${typeof text}`);
text = '8' / '2'; //원래는 되면 안되는데 되니깐 연산을 해버림
console.log(`value:${text}, type:${typeof text}`);
// dynamic typing의 불분명한 type을 해결한 typescript의 배경,
// 결국 TS도 transformation을 하고 js로 만들어야함.
