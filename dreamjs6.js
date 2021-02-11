// objects
// literals, property
const name = 'ellie';
const age = 4;

function print(person) {
    console.log(person.name);
    console.log(person.age);
}

const ellie = {
    name: 'ellie',
    age: 4
}; // object 생성
print(ellie);

//2. computed property 계산된 property
console.log(ellie.name); //코딩할때는 .
console.log(ellie['name']); // key 는ㄴ string type
ellie['hasJob'] = true; // 정확하게 어떤 값이 필요할지 모를 때, 실시간으로 runtime(구동할때) 
console.log(ellie.hasJob);

function printValue(obj, key) {
    console.log(obj, key);
} // key가 정상적이야? // [key]를 출력해줘
printValue(ellie, 'name');

//3. property value shorthand
const person1 = { name: 'bob', age: 2 };
const person2 = { name: 'steve', age: 3 };
const person3 = makePerson('ellie', 30);
// 또 추가하려하는데 일일이 다 치긴 힘들다면?
function makePerson(name, age) {
    return {
        /*name : */
        name, // 오차가 생기지 않는다면 생략해주어도 됨
        /*age : */
        age, // template같은 느낌, class 없을때 이렇게 만듬
    };
} // 함수를 이용해서 값만 전달해주면 되게 만듬
const person4 = new Person('ell', 30);

//4. constructor function
function Person(name, age) {
    this.name = name;
    this.age = age;
}
console.log(person3);
console.log(person4);

//5. in operator : property 를 체크
console.log('name' in ellie);
console.log('age' in ellie);
console.log('random' in ellie); // 정의하지 않은 값 false
console.log(ellie.random); // undefined

//6. for in vs for of
// for(key in obj)
console.clear();
for (key in ellie) {
    console.log(key);
}

// for (value of iterable)
const array = [1, 2, 4, 5]
for (let i = 0; i < array.length; i++) {
    console.log(array[i]);
} // 이렇게하면 출력은 되겠으나 더 쉽게 할 수 잇는 방법잉 ㅣㅇㅆ다ㅣ

for (value of array) {
    console.log(value);
}

// 7. fun cloning
// object.assign(dest, [obj1, obj2, obj3, obj4])
const user = {
    name: 'ellie',
    age: '20'
};
const user2 = user;
user2.name = 'coder';
console.log(user);