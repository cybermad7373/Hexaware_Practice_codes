// 8. Split String into Words
let sentence = "Hello My Name is Rohan Sharma";
let words = sentence.split(" ");
console.log("Split sentence:", words);

// 9. Limited Split
let fruits = "apple,banana,cherry,grape";
let firstTwoFruits = fruits.split(",", 2);
console.log("First two fruits:", firstTwoFruits);

// 10. Split with Regex
let data = "apple123banana456cherry789";
let splitData = data.split(/\d+/);
console.log("Split by numbers:", splitData);

// 11. Split into Characters
let name = "Aarav";
let letters = name.split("");
console.log(`Letters in ${name}:`, letters);

// 12. Complex Split
let mixedFruits = "apple,banana|cherry grape";
let fruitList = mixedFruits.split(/[,| ]/);
console.log("Mixed split result:", fruitList);