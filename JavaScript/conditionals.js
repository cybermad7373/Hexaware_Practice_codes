
// Voting eligibility check
let voterName = "Arjun Reddy";
let voterAge = 20;

if (voterAge >= 18) {
    console.log(`${voterName} is eligible to vote`);
} else {
    console.log(`${voterName} will be eligible in ${18 - voterAge} years`);
}

// Indian train ticket pricing
let passengerName = "Sunita Verma";
let travelClass = "AC";
let ticketPrice;

switch(travelClass) {
    case "AC":
        ticketPrice = 1500;
        break;
    case "Sleeper":
        ticketPrice = 800;
        break;
    case "General":
        ticketPrice = 400;
        break;
    default:
        ticketPrice = 0;
}

console.log(`${passengerName}'s ${travelClass} ticket costs ₹${ticketPrice}`);

// Ternary operator for Indian food order
let orderAmount = 650;
let deliveryCharge = orderAmount > 500 ? 0 : 50;
console.log(`Delivery charge: ₹${deliveryCharge}`);