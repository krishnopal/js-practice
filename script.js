//ajke amra variable er kaj korbo....

let s = "shuvo pal";
console.log(s);

var age = 25;
console.log(age);

let city = "Dhaka";
console.log(city);

const country = "Bangladesh";
console.log(country);


let isLoggedIn = true;
console.log(isLoggedIn);

let colors = ["red", "blue", "green"];
console.log(colors);


let user = {
  name: "Shuvo",
  age: 25
};
console.log(user);

if (true) {
  var x = 10;
}
console.log(x);


let name = "Shuvo";
function test() {
  let name = "Rahim";
  console.log(name);
}
test();



function outer() {
  let counter = 0;

  return function inner() {
    counter++;
    console.log(counter);
  };
}
const count = outer();
count(); // 1
count(); // 2


let a = 10;
let b = a;
b = 20;
console.log(a); // 10
let obj1 = { name: "Shuvo" };
let obj2 = obj1;
obj2.name = "Rahim";
console.log(obj1.name); // Rahim
