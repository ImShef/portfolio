function mathOp(x, y, op) {
    return op(x, y);
}
var sum = function (x, y) { return x + y; };
var subtract = function (x, y) { return x - y; };
var multiply = function (x, y) { return x * y; };
var divide = function (x, y) { return x / y; };
console.log('Сложение:', mathOp(10, 20, sum));
console.log('Вычитание:', mathOp(10, 20, subtract));
console.log('Умножение:', mathOp(10, 20, multiply));
console.log('Деление:', mathOp(10, 20, divide));
