
// Form validation for Indian phone number
function validateForm() {
    let phone = document.getElementById("phone").value;
    if (phone.length !== 10 || isNaN(phone)) {
        alert("Please enter a valid 10-digit Indian phone number");
        return false;
    }
    alert("Dhanyavaad! Form submitted successfully");
    return true;
}

// On mouseover event for Indian festival greeting
document.getElementById("diwaliBtn").onmouseover = function() {
    this.innerText = "Diwali ki Shubhkamnayein!";
};

document.getElementById("diwaliBtn").onmouseout = function() {
    this.innerText = "Festival Greetings";
};

// On change event for Indian states dropdown
document.getElementById("stateSelect").onchange = function() {
    let selectedState = this.options[this.selectedIndex].text;
    console.log(`Selected state: ${selectedState}`);
    document.getElementById("stateDisplay").innerText = 
        `You selected: ${selectedState}`;
};