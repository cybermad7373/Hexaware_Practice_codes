// Function to show employee details
function showEmployeeDetails() {
    let empName = "Vikram Singh";
    let empId = "HXW456";
    let department = "IT";
    
    document.getElementById("empName").innerText = empName;
    document.getElementById("empId").innerText = empId;
    document.getElementById("department").innerText = department;
}

// Function to calculate PF (Indian Provident Fund)
function calculatePF() {
    let basicSalary = parseFloat(document.getElementById("salary").value);
    let pfAmount = basicSalary * 0.12;
    document.getElementById("pfResult").innerHTML = 
        `<strong>PF Contribution:</strong> ₹${pfAmount.toFixed(2)} per month`;
}

// Event handler for button click
document.getElementById("greetBtn").onclick = function() {
    let userName = document.getElementById("userName").value || "Guest";
    alert(`Atithi Devo Bhava! Welcome ${userName} to our website!`);
};