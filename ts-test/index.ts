type Operation = (a: number, b: number) => number

function mathOp(x: number, y: number, op: Operation): number {
	return op(x, y)
}

const sum: Operation = (x, y) => x + y
const subtract: Operation = (x, y) => x - y
const multiply: Operation = (x, y) => x * y
const divide: Operation = (x, y) => x / y

console.log('Сложение:', mathOp(10, 20, sum))
console.log('Вычитание:', mathOp(10, 20, subtract))
console.log('Умножение:', mathOp(10, 20, multiply))
console.log('Деление:', mathOp(10, 20, divide))
