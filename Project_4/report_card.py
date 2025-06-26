import datetime
from collections import defaultdict

class ReportCardSystem:
    def __init__(self):
        self.students = {}
        self.grade_scale = [
            (90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'), (0, 'F')
        ]

    def add_student(self, name, marks):
        """Add student with name and marks list"""
        self.students[name] = {
            'marks': marks,
            'date_added': datetime.date.today()
        }
        print(f"Student {name} added successfully!")

    def calculate_percentage(self, marks):
        return sum(marks) / len(marks)

    def get_grade(self, percentage):
        for min_score, grade in self.grade_scale:
            if percentage >= min_score:
                return grade

    def generate_report(self, name):
        if name not in self.students:
            return None
        
        data = self.students[name]
        percentage = self.calculate_percentage(data['marks'])
        grade = self.get_grade(percentage)
        
        return {
            'name': name,
            'percentage': percentage,
            'grade': grade,
            'added_on': data['date_added']
        }

    def get_highest_scorer(self):
        if not self.students:
            return None
        return max(self.students.items(), 
                    key=lambda x: self.calculate_percentage(x[1]['marks']))

    def run(self):
        while True:
            print("\n" + "="*50)
            print("STUDENT REPORT CARD SYSTEM".center(50))
            print("="*50)
            print("1. Add Student")
            print("2. View Student Report") 
            print("3. View Highest Scorer")
            print("4. Back to Main Menu")
            print("="*50)
            
            choice = input("Enter your choice (1-4): ")
            
            if choice == '1':
                name = input("Enter student name: ")
                marks = list(map(float, input("Enter marks separated by space: ").split()))
                self.add_student(name, marks)
            elif choice == '2':
                name = input("Enter student name: ")
                report = self.generate_report(name)
                if report:
                    print("\n" + "="*30)
                    print(f"Name: {report['name']}")
                    print(f"Percentage: {report['percentage']:.2f}%")
                    print(f"Grade: {report['grade']}")
                    print(f"Added on: {report['added_on']}")
                    print("="*30)
                else:
                    print("Student not found!")
            elif choice == '3':
                student = self.get_highest_scorer()
                if student:
                    name, data = student
                    percentage = self.calculate_percentage(data['marks'])
                    print(f"\nHighest Scorer: {name} with {percentage:.2f}%")
                else:
                    print("No students found!")
            elif choice == '4':
                break
            else:
                print("Invalid choice!")
            
            input("\nPress Enter to continue...")