// Objects
let employee = {
    name: "Rajesh Kumar",
    age: 32,
    department: "IT",
    salary: 75000,
    isMarried: true
};

console.log("Employee Name:", employee.name);
console.log("Department:", employee["department"]);

// Maps
let employeeSkills = new Map();
employeeSkills.set("Rajesh Kumar", ["Java", "JavaScript", "SQL"]);
employeeSkills.set("Priya Patel", ["Python", "React", "MongoDB"]);

console.log("Rajesh's skills:", employeeSkills.get("Rajesh Kumar"));
console.log("Map size:", employeeSkills.size);

// Sets
let uniqueDepartments = new Set();
uniqueDepartments.add("IT");
uniqueDepartments.add("HR");
uniqueDepartments.add("Finance");
uniqueDepartments.add("IT"); // Duplicate won't be added

console.log("Unique Departments:", uniqueDepartments);
console.log("Has HR department:", uniqueDepartments.has("HR"));