// function
// fundamental building block in the program
// performs a task, calculates a value

// 1. function declaration
// let, const was nerb
// function verb && one thing
// 현업에서는 정확하게 interface를 명시를 해줘야 협업이 됨,

// 2. parameters
function changename(obj) {
  obj.name = 'coder';
}
const ellie = { name: 'ellie' }; //오호라 , const는 ref까지 고정값인데 함수를 넣으니 변경이 되는 구나
changename(ellie);
console.log(ellie); // { name: 'coder' }

//3. Default parameters (added in es6)
function showmessage(message, from) {
  if (from == undefined) {
    from = 'unknown';
  }
  console.log(`${message} by ${from}`);
}
showmessage('hi'); // 지정을 안하면 undefined
//4. rest parameter (added in es6) ... 배열
function printall(...args) {
  for (let i = 0; i < args.length; i++) {
    console.log(args[i]);
  }
  for (const arg of args) {
    // 이렇게 표현할 수도

    console.log(arg);
  }
}

printall('dream', 'coding', 'ellie'); //배열은 아니지만,...때문에 배열 형태로 보내짐

// 5. local scope 나중에 close, lexico에 정밀하게 들어감
let globalmessage = 'global'; // global variable
function printmessage() {
  let message = 'hello';
  console.log(message); // local variable
  console.log(globalmessage);
}
printmessage();

// 6. Return a value
function sum(a, b) {
  return a + b;
}
const result = sum(1, 2); //3
console.log(`sum:${sum(1, 2)}`);

// 7. Early return, early exit
//bad
function upgradeuser(user) {
  if (user.point > 10) {
    //long upgrade logic...
  } // 블럭안에서 계속 쓰면 가독성이 떨어짐
}

//good
function upgradeuser(user) {
  if (user.point <= 10) {
    return;
  }
}
// 1. first-class function
// 을 가능하게 하는 function expression
// 함수에 이름이 없으면 anonymous function
const print = function () {
  console.log(`print`);
};
print();
const printagain = print;
printagain();

const sumAgain = sum;
console.log(sumAgain(1, 3));

// 2. callback function using function expression
function randomQuiz(answer, printYes, printNo) {
  if (answer === 'love you') {
    printYes();
  } else {
    printNo();
  }
}
randomQuiz('love you');
randomQuiz('wrong');
// anonymous function
const printYes = function () {
  console.log('yes!');
};
// named function
// better debugging in debugger's stack traces
const printNo = function print() {
  console.log('no!'); // 피보나치 수열풀때
  print();
};
//Arrow function // always anonymous
const simplePrint = function () {
  console.log('simplePrint!'); // js특징상 선언된 모든 함수를 모아놓음, hoisting되어서 뒤에선언됬지만 끌어올려서 진행하는것
};

const simpleprint = () => console.log('simplePrint!');
const add = (a, b) => a + b;

// IIFE : Immediately Invoked Function Expression
(function hello() {
  console.log('IIFE');
})();
