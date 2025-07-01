// 1. Add Two Numbers
let num1 = 5;
let num2 = 10;
let sum = num1 + num2;
console.log(`Sum of ${num1} and ${num2} is: ${sum}`);

// 2. Check Even or Odd
function checkEvenOdd(number) {
    return number % 2 === 0 ? "Even" : "Odd";
}
console.log(`7 is ${checkEvenOdd(7)}`); // Odd
console.log(`Rahul's age (24) is ${checkEvenOdd(24)}`); // Even

// 3. Print Numbers 1 to 5
console.log("Counting from 1 to 5:");
for (let i = 1; i <= 5; i++) {
    console.log(i);
}

// 4. Reverse a String
let name = "Priya";
let reversedName = name.split('').reverse().join('');
console.log(`${name} reversed is ${reversedName}`);

// 5. Check Even/Odd in Loop
console.log("Checking numbers 1 to 10:");
for (let i = 1; i <= 10; i++) {
    console.log(`${i} is ${checkEvenOdd(i)}`);
}

// 6. Prime Number Check
function isPrime(number) {
    if (number <= 1) return false;
    for (let i = 2; i < number; i++) {
        if (number % i === 0) return false;
    }
    return true;
}

console.log("Prime numbers between 2-20:");
for (let num = 2; num <= 20; num++) {
    console.log(`${num} is ${isPrime(num) ? 'prime' : 'not prime'}`);
}

// 7. Factorial Calculation
function factorial(n) {
    let result = 1;
    for (let i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

console.log(`Factorial of 5 (5!) is ${factorial(5)}`); // 120