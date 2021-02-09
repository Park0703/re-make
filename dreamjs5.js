// 1. 클래스 in es6
// 변수들이 정리가 안되어서 규모있는 프로젝트를 하기 힘듬
// 클래스는 묶는 컨테이너와 같음 

// class person {
//     name; //속성 field
//     age;
//     speak() //행동 method
// } // fields 만 묶어 놓는 경우가 많음, class data
// 이걸 통해서 상속도 함

//class 붕어빵틀, 청사진, template
//declare once, data in// object를 집어넣음
//object 팥을 넣으면 팥붕어빵, 슈크림을 넣으면 슈크림 붕어빵


//1. Class declarations
class Person {
    // constructor
    constructor(name, age) {
            // fields
            this.name = name;
            this.age = age;
        }
        // methods

    speak() {
        console.log(`${this.name} : hello!`)
    }
}
const ellie = new Person('ellie', 20)
console.log(ellie.name);
console.log(ellie.age);
ellie.speak();


//2. getter setter 객체지향 언어에서 말이 되게 만들어주는 것
// setter 는 이상한 값이 input되어도 가동가능한 값으로 바꿔 주는 장치임
// 외부에서 영향을 밭지 않게 property 를 private 하게 만들어야 함.
class User {
    constructor(firstName, lastName, age) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        // this.age는 getter를, = age는 setter를 호출하게 됨
    }
    get age() {
            return this._age;
        }
        // 전달된 value는 set를 다시 호출하게 됨, 무한 반복Maximum call stack size exceeded
        // 다른 이름을 해줘야 한다.
    set age(value) {
            // if (value < 0) {
            //     throw Error('age can not be negative');
            // }
            this._age = value < 0 ? 0 : value;
        }
        // _age여도 age에 반응하는 것은 getter setter가 있기 때문임
}
const user1 = new User('Steve', 'Job', -1);
console.log(user1.age);

//3. public, private 최신
// constructor 없이 field를 정의할 수 있는데
class experiment {
    // publ = 2;
    // priv = 0; // undefined 로 표시되게 함.
}

//4. static
// object에 상관없이 class에 
// const article1 = new article(1);
// const article2 = new article(2);
// console.log(Article)

// 공통적으로 쓸쑤있는 것에

// 5. inheritance 상속과 다양성 다른 class로 확장
class shape {
    constructor(width, height, color) {
        this.width = width;
        this.height = height;
        this.color = color;
    }
    draw() { // method
        console.log(`drawing ${this.color} color of`); // 수정 부분
    }
    getArea() { // method
        return width * this.height;
    }
}
class Rectangle extends shape {} // 상속
const rectangle = new Rectangle(20, 20, 'blue');
rectangle.draw(); // 공통부분을 재사용가능, 수정할때도 한 곳만 하면 됨

// overwriting
// 6. class checking : instanceOf
console.log(rectangle instanceof Rectangle);
console.log(rectangle instanceof shape);

// javascript reference