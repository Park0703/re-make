// 1. string concatenation
console.log('my' + 'cat'); // 합쳐짐
console.log('1' + 2); // 문자열이 됨
console.log(`string literals : 1 + 2 = ${1 + 2}`); // 문자열로 됨

// 새로 줄바꿈을 할땐 \\
//2. Numeric operators
console.log(1 + 1); // add
console.log(1 - 1); // substract
console.log(1 / 1); // divide
console.log(1 * 1); // multiply
console.log(5 % 2); // remainder
console.log(2 ** 4); // exponentiation

//3. Increment and decrement operators
let counter = 2;
const preIncrement = ++counter;
// counter = counter + 1;
// preincrement = counter;
console.log(counter);
const postincrement = counter++;
// postincrement = counter;
// counter = counter + 1;
console.log(counter);

//4. assignment operators
let x = 3;
let y = 6;
x += y; // x=x+y;
x -= y;
x *= y;
x /= y;

//5. comparison operators
console.log(10 < 6); // less than
console.log(10 <= 6); // less than or equal
console.log(10 > 6); // greater than
console.log(10 >= 6); // greater than or equal

//6. logical operators; || or. %% and, !not
// ||로 불러낼 땐 연산량을 줄이기 위해서 value1 값을 앞에 function을 뒤에 해서 앞에서 true 걸리면 끝나게 해주는게 좋음

//7. equality
const stringFive = '5';
const numberFive = 5;

// == loose equality, with type conversion
console.log(stringFive == numberFive);
console.log(stringFive != numberFive);
// === strict equality, no type conversion // 이게 더 자주쓰임
console.log(stringFive === numberFive);
console.log(stringFive !== numberFive);

// object equlity by reference
const ellie1 = { name: 'ellie' };
const ellie2 = { name: 'ellie' };
const ellie3 = ellie1;
console.log(ellie1 == ellie2); // false, 왜냐하면 서로다른ref에 잠귀어 버림
console.log(ellie1 === ellie2); // let 이었다면 true, const라서 false
console.log(ellie1 === ellie3); // true, 왜냐하면 e1의 ref1을 가져왔기 때문에

// 8. conditional operator : if
const name = 'df';
if (name === 'ellie') {
  console.log('welcome, Ellie!');
} else if (name === 'coder') {
  console.log('you are amazing coder');
} else {
  console.log('unknown');
}

// 9. Ternary operator; ? // condition? value1:value2;
console.log(name === 'ellie' ? 'yes' : 'no');

// 10. switch statement
// use for multiple if checks, enum-like balue check, muliple type checks in ts
const browser = 'IE';
switch (browser) {
  case 'IE':
    console.log('go away!');
    break;
  case 'chrome':
    console.log('love you!');
    break;
  case 'Firefox':
    console.log('love you!');
    break;
  default:
    console.log('same all!');
    break;
}

// 11. loops
// while,
let i = 3;
while (i > 0) {
  console.log(`while:${i}`);
  i--;
}
do {
  console.log(`do while : ${i}`);
  i--;
} while (i > 0);
//for
for (i = 3; i > 0; i--) {
  // 기존에 존재하는 변수를 할당하는 경우
  console.log(`for: ${i}`);
}
for (let i = 3; i > 0; i = i - 2) {
  // inline variable declaration
  console.log(`inline variable for : ${i}`);
}

// nested loops
for (let i = 0; i < 10; i++) {
  // n**2연산함 cpu 에 좋지 않다.
  for (let j = 0; j < 10; j++) {
    console.log(`i:${i}, j:${j}`);
  }
}
