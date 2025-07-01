// Simple greeting function
function greetUser(name) {
    return `Namaste ${name}! Kaise ho?`;
}

console.log(greetUser("Neha Gupta"));

// Calculate GST for Indian products
function calculateTotal(price, quantity) {
    const GST_RATE = 0.18;
    let total = price * quantity;
    let gst = total * GST_RATE;
    return total + gst;
}

let mobilePrice = 15000;
let totalBill = calculateTotal(mobilePrice, 2);
console.log("Total bill with GST: ₹" + totalBill);

// Marriage eligibility checker
function checkMarriageEligibility(name, age, gender) {
    if ((gender === 'male' && age >= 21) || (gender === 'female' && age >= 18)) {
        return `${name} is eligible for marriage`;
    } else {
        return `${name} is not eligible for marriage yet`;
    }
}

console.log(checkMarriageEligibility("Ravi", 25, "male"));
console.log(checkMarriageEligibility("Pooja", 17, "female"));