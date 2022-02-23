console.time("label")
// 定義一個類別
class Car {
    constructor(color) {
        this.color = color;
    }
    run(){}
}
// 產生類別物件
let car = new Car("green");
//取得並將原型物件顯示出來
let carProto = Object.getPrototypeOf(car); // Car 原型物件
console.log(carProto);
let objProto = Object.getPrototypeOf(carProto); // Object 原型物件
console.log(objProto);
let lastOne = Object.getPrototypeOf(objProto); // 原型練終點 : null
console.log(lastOne);

console.timeEnd("label")