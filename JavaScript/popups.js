// Alert box
alert("Welcome to Hexaware, Priya!");

// Confirm box - Indian language mix
let isConfirmed = confirm("Kya aap course continue karna chahte hain?\nDo you want to continue the course?");
if (isConfirmed) {
    console.log("User selected 'OK'");
} else {
    console.log("User selected 'Cancel'");
}

// Prompt box
let userName = prompt("Aapka naam kya hai?", "Amit Kumar");
if (userName) {
    alert(`Namaste ${userName}! Aapka swagat hai!`);
} else {
    alert("Naam nahi diya gaya");
}