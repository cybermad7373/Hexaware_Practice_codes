// Basic Array
let indianNames = ["Aarav", "Priya", "Rohan", "Ananya"];
console.log("First name:", indianNames[0]);
console.log("Total names:", indianNames.length);

// 1. push() - Add to end
indianNames.push("Vikram");
console.log("After push:", indianNames);

// 2. pop() - Remove from end
let removedName = indianNames.pop();
console.log("Removed:", removedName);
console.log("After pop:", indianNames);

// 3. shift() - Remove from start
let firstName = indianNames.shift();
console.log("Removed first:", firstName);
console.log("After shift:", indianNames);

// 4. unshift() - Add to start
indianNames.unshift("Aditi");
console.log("After unshift:", indianNames);

// 5. splice() - Add/Remove at position
// Remove
let removedItems = indianNames.splice(1, 2);
console.log("Removed items:", removedItems);
console.log("After splice remove:", indianNames);

// Add
indianNames.splice(1, 0, "Karan", "Neha");
console.log("After splice add:", indianNames);

// 6. concat() - Merge arrays
let southNames = ["Arjun", "Divya"];
let northNames = ["Rahul", "Pooja"];
let allNames = southNames.concat(northNames);
console.log("Combined names:", allNames);

// 7. slice() - Subarray
let someNames = allNames.slice(1, 3);
console.log("Sliced names:", someNames);

// 8. indexOf()
let position = allNames.indexOf("Divya");
console.log("Position of Divya:", position);

// 9. forEach()
console.log("Printing all names:");
allNames.forEach(name => console.log(name));

// 10. map()
let nameLengths = allNames.map(name => name.length);
console.log("Name lengths:", nameLengths);

// 11. filter()
let longNames = allNames.filter(name => name.length > 4);
console.log("Names with more than 4 letters:", longNames);