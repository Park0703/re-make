// array 자료구조
// object와 차이점 : 동물 - 귀, 눈, 뛴다, 먹는다 // 연관성으로 묶어놓음
'use strict';
// 비슷한 타입으로 묶어 놓음
// 검색, 정렬, 삽입, 삭제 // 자료구조와 알고리즘

// 배열 인덱스  0  1  2  3  4 데이터를 넣을 땐 동일한 타입을 넣어라
// 1. declaration
// const arr1 = array();
const arr2 = [1, 2];

// 2. index position
const fruits = ['❤', '🎁']
console.log(fruits);
console.log(fruits.length);
console.log(fruits[3])
console.log(fruits[fruits.length - 1])

// 3. looping
// for
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i])
}
// for of

for (let fruit of fruits) {
    console.log(fruit);
}
//for each
fruits.forEach(function(fruit, index, array) {
    console.log(fruit);
});
//for each
fruits.forEach((fruit, index) => console.log(fruit, index));
// Adaption, deletion, copy
// push add and item to the end
// pop remove an item to the end
// shift remove an item from the beginning
// unshift add an item from the beginning

// un/shift are slower than pop, push // in making black space
// 차라리 중간에 있는 데이터를 움지이게 하는게 나아
// splice(1start, 2deletecount, 3)

// combine two arrays - concat
const fruits2 = ['z', 'x']
const fruits3 = fruits.concat(fruits2)
console.log(fruits3)
    // indexOf 처음으로 맞나는 데이터의 인덱스 번호 찾기
console.log(fruits3.indexOf('z'));
// 있는지 없는지 찾기

console.log(fruits3.includes('x'));
//lastIndexOf() 똑같은 데이터가 있는경우 가장 마지막에 있는 인덱스 번호 찾기