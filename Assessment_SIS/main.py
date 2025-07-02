#!/usr/bin/env python3
import sys
from getpass import getpass
from datetime import date
from typing import Optional

from dao.sis_service_impl import SISServiceImpl
from entity.student import Student
from entity.course import Course
from entity.teacher import Teacher
from exception.student_not_found_exception import StudentNotFoundException
from exception.course_not_found_exception import CourseNotFoundException
from exception.teacher_not_found_exception import TeacherNotFoundException
from exception.duplicate_enrollment_exception import DuplicateEnrollmentException
from exception.payment_validation_exception import PaymentValidationException
from util.validation_util import ValidationUtil

class MainApp:
    """Main application class for the Student Information System"""
    
    def __init__(self):
        self.current_user = None
        self.is_admin = False
        self.sis_service = SISServiceImpl()
    
    def run(self):
        """Main entry point for the application"""
        try:
            while True:
                if not self.current_user:
                    self.show_login_menu()
                elif self.is_admin:
                    self.show_admin_menu()
                else:
                    self.show_student_menu()
        except KeyboardInterrupt:
            print("\nExiting the system...")
            sys.exit(0)
    
    def show_login_menu(self):
        """Display the login menu"""
        print("\n===== Student Information System =====")
        print("1. Student Login")
        print("2. Admin Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            self.student_login()
        elif choice == "2":
            self.admin_login()
        elif choice == "3":
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")
    
    def student_login(self):
        """Handle student login"""
        print("\n--- Student Login ---")
        email = input("Email: ").strip()
        password = getpass("Password: ").strip()
        
        try:
            with SISServiceImpl() as service:
                self.current_user = service.authenticate_student(email, password)
                self.is_admin = False
                print(f"\nWelcome, {self.current_user.first_name}!")
        except StudentNotFoundException:
            print("Error: Student not found with that email.")
        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    
    def admin_login(self):
        """Handle admin login"""
        print("\n--- Admin Login ---")
        email = input("Email: ").strip()
        password = getpass("Password: ").strip()
        
        # In a real system, you'd have a separate admin authentication
        # For this example, we'll use a hardcoded admin credential
        if email == "admin@sis.edu" and password == "Admin@123":
            self.current_user = Student(
                student_id=0,
                first_name="Admin",
                last_name="User",
                email="admin@sis.edu",
                date_of_birth="2000-01-01",
                phone_number="0000000000"
            )
            self.is_admin = True
            print("\nWelcome, Administrator!")
        else:
            print("Error: Invalid admin credentials.")
    
    def show_admin_menu(self):
        """Display the admin menu"""
        print("\n===== Admin Dashboard =====")
        print("1. Student Management")
        print("2. Course Management")
        print("3. Teacher Management")
        print("4. Reports")
        print("5. Logout")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            self.student_management_menu()
        elif choice == "2":
            self.course_management_menu()
        elif choice == "3":
            self.teacher_management_menu()
        elif choice == "4":
            self.reports_menu()
        elif choice == "5":
            self.current_user = None
            self.is_admin = False
            print("Logged out successfully.")
        else:
            print("Invalid choice. Please try again.")
    
    def show_student_menu(self):
        """Display the student menu"""
        print(f"\n===== Student Dashboard ({self.current_user.first_name}) =====")
        print("1. View My Profile")
        print("2. Update My Profile")
        print("3. View My Courses")
        print("4. Enroll in Course")
        print("5. View Payment History")
        print("6. Make Payment")
        print("7. Logout")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            self.view_student_profile()
        elif choice == "2":
            self.update_student_profile()
        elif choice == "3":
            self.view_student_courses()
        elif choice == "4":
            self.enroll_in_course()
        elif choice == "5":
            self.view_payment_history()
        elif choice == "6":
            self.make_payment()
        elif choice == "7":
            self.current_user = None
            print("Logged out successfully.")
        else:
            print("Invalid choice. Please try again.")
    
    # Admin menu handlers
    def student_management_menu(self):
        """Student management submenu"""
        print("\n--- Student Management ---")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Back to Main Menu")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            self.add_student()
        elif choice == "2":
            self.view_all_students()
        elif choice == "3":
            self.update_student()
        elif choice == "4":
            return
        else:
            print("Invalid choice. Please try again.")
    
    def course_management_menu(self):
        """Course management submenu"""
        print("\n--- Course Management ---")
        print("1. Add New Course")
        print("2. View All Courses")
        print("3. Assign Teacher to Course")
        print("4. Back to Main Menu")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            self.add_course()
        elif choice == "2":
            self.view_all_courses()
        elif choice == "3":
            self.assign_teacher_to_course()
        elif choice == "4":
            return
        else:
            print("Invalid choice. Please try again.")
    
    def teacher_management_menu(self):
        """Teacher management submenu"""
        print("\n--- Teacher Management ---")
        print("1. Add New Teacher")
        print("2. View All Teachers")
        print("3. Back to Main Menu")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            self.add_teacher()
        elif choice == "2":
            self.view_all_teachers()
        elif choice == "3":
            return
        else:
            print("Invalid choice. Please try again.")
    
    def reports_menu(self):
        """Reports submenu"""
        print("\n--- Reports ---")
        print("1. Course Enrollment Report")
        print("2. Student Payment Report")
        print("3. Back to Main Menu")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            self.generate_course_report()
        elif choice == "2":
            self.generate_payment_report()
        elif choice == "3":
            return
        else:
            print("Invalid choice. Please try again.")
    
    # Admin operations
    def add_student(self):
        """Add a new student to the system"""
        print("\n--- Add New Student ---")
        
        try:
            student = Student()
            student.first_name = input("First Name: ").strip()
            student.last_name = input("Last Name: ").strip()
            student.date_of_birth = input("Date of Birth (YYYY-MM-DD): ").strip()
            student.email = input("Email: ").strip()
            student.phone_number = input("Phone Number: ").strip()
            
            password = getpass("Password: ").strip()
            confirm_password = getpass("Confirm Password: ").strip()
            
            if password != confirm_password:
                print("Error: Passwords do not match.")
                return
            
            added_student = self.sis_service.add_student(student, password)
            print(f"\nStudent added successfully with ID: {added_student.student_id}")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    def view_all_students(self):
        """View all students in the system"""
        print("\n--- All Students ---")
        try:
            # In a complete implementation, you would have a method to get all students
            # For now, we'll simulate this with a search
            students = []
            search_term = input("Enter search term (leave empty for all): ").strip()
            
            # This would be replaced with actual database query
            print("\nStudent List:")
            print("ID\tName\t\tEmail")
            print("-" * 50)
            for student in students:
                print(f"{student.student_id}\t{student.first_name} {student.last_name}\t{student.email}")
            
            if not students:
                print("No students found.")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    def update_student(self):
        """Update student information"""
        print("\n--- Update Student ---")
        try:
            student_id = int(input("Enter Student ID to update: ").strip())
            student = self.sis_service.get_student(student_id)
            
            print(f"\nCurrent Information for {student.first_name} {student.last_name}:")
            print(f"1. First Name: {student.first_name}")
            print(f"2. Last Name: {student.last_name}")
            print(f"3. Date of Birth: {student.date_of_birth}")
            print(f"4. Email: {student.email}")
            print(f"5. Phone Number: {student.phone_number}")
            
            field = input("\nEnter field number to update (1-5) or 0 to cancel: ").strip()
            
            if field == "0":
                return
            
            if field == "1":
                student.first_name = input("Enter new First Name: ").strip()
            elif field == "2":
                student.last_name = input("Enter new Last Name: ").strip()
            elif field == "3":
                student.date_of_birth = input("Enter new Date of Birth (YYYY-MM-DD): ").strip()
            elif field == "4":
                student.email = input("Enter new Email: ").strip()
            elif field == "5":
                student.phone_number = input("Enter new Phone Number: ").strip()
            else:
                print("Invalid field number.")
                return
            
            if self.sis_service.update_student(student):
                print("Student information updated successfully.")
            else:
                print("Failed to update student information.")
        except StudentNotFoundException:
            print("Error: Student not found.")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    def add_course(self):
        """Add a new course to the system"""
        print("\n--- Add New Course ---")
        
        try:
            course = Course()
            course.course_name = input("Course Name: ").strip()
            course.course_code = input("Course Code: ").strip()
            course.credits = int(input("Credits (1-6): ").strip())
            
            added_course = self.sis_service.add_course(course)
            print(f"\nCourse added successfully with ID: {added_course.course_id}")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    def view_all_courses(self):
        """View all courses in the system"""
        print("\n--- All Courses ---")
        try:
            with SISServiceImpl() as service:
                courses = service.get_all_courses()
                
                if not courses:
                    print("No courses found.")
                    return
                
                print("\nCourse List:")
                print(f"{'ID':<5}{'Code':<10}{'Name':<25}{'Credits':<8}{'Teacher':<20}")
                print("-" * 70)
                for course in courses:
                    print(f"{course.course_id:<5}{course.course_code:<10}{course.course_name[:20]:<25}{course.credits:<8}{course.teacher_name or 'Not assigned':<20}")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    def assign_teacher_to_course(self):
        """Assign a teacher to a course"""
        print("\n--- Assign Teacher to Course ---")
        try:
            course_id = int(input("Enter Course ID: ").strip())
            teacher_id = int(input("Enter Teacher ID: ").strip())
            
            if self.sis_service.assign_teacher_to_course(teacher_id, course_id):
                print("Teacher assigned to course successfully.")
            else:
                print("Failed to assign teacher to course.")
        except (CourseNotFoundException, TeacherNotFoundException) as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    def add_teacher(self):
        """Add a new teacher to the system"""
        print("\n--- Add New Teacher ---")
        
        try:
            teacher = Teacher()
            teacher.first_name = input("First Name: ").strip()
            teacher.last_name = input("Last Name: ").strip()
            teacher.email = input("Email: ").strip()
            
            # In a complete implementation, you would have a method to add teachers
            print("\nTeacher added successfully (simulated)")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    def view_all_teachers(self):
        """View all teachers in the system"""
        print("\n--- All Teachers ---")
        try:
            # This would be replaced with actual database query
            teachers = []
            
            print("\nTeacher List:")
            print("ID\tName\t\tEmail")
            print("-" * 50)
            for teacher in teachers:
                print(f"{teacher.teacher_id}\t{teacher.first_name} {teacher.last_name}\t{teacher.email}")
            
            if not teachers:
                print("No teachers found.")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    def generate_course_report(self):
        """Generate a course enrollment report"""
        print("\n--- Course Enrollment Report ---")
        try:
            course_id = int(input("Enter Course ID: ").strip())
            
            # In a complete implementation, you would call the service method
            print(f"\nEnrollment Report for Course ID: {course_id}")
            print("This would display actual enrollment data in the full implementation")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    def generate_payment_report(self):
        """Generate a student payment report"""
        print("\n--- Student Payment Report ---")
        try:
            student_id = int(input("Enter Student ID: ").strip())
            
            # In a complete implementation, you would call the service method
            print(f"\nPayment Report for Student ID: {student_id}")
            print("This would display actual payment data in the full implementation")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    # Student operations
    def view_student_profile(self):
        """View current student's profile"""
        print("\n--- My Profile ---")
        try:
            student = self.sis_service.get_student(self.current_user.student_id)
            
            print(f"\nStudent ID: {student.student_id}")
            print(f"Name: {student.first_name} {student.last_name}")
            print(f"Date of Birth: {student.date_of_birth}")
            print(f"Email: {student.email}")
            print(f"Phone Number: {student.phone_number}")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    def update_student_profile(self):
        """Update current student's profile"""
        print("\n--- Update My Profile ---")
        try:
            student = self.sis_service.get_student(self.current_user.student_id)
            
            print("\nCurrent Information:")
            print(f"1. First Name: {student.first_name}")
            print(f"2. Last Name: {student.last_name}")
            print(f"3. Date of Birth: {student.date_of_birth}")
            print(f"4. Email: {student.email}")
            print(f"5. Phone Number: {student.phone_number}")
            
            field = input("\nEnter field number to update (1-5) or 0 to cancel: ").strip()
            
            if field == "0":
                return
            
            if field == "1":
                student.first_name = input("Enter new First Name: ").strip()
            elif field == "2":
                student.last_name = input("Enter new Last Name: ").strip()
            elif field == "3":
                student.date_of_birth = input("Enter new Date of Birth (YYYY-MM-DD): ").strip()
            elif field == "4":
                student.email = input("Enter new Email: ").strip()
            elif field == "5":
                student.phone_number = input("Enter new Phone Number: ").strip()
            else:
                print("Invalid field number.")
                return
            
            if self.sis_service.update_student(student):
                self.current_user = student  # Update current user data
                print("Profile updated successfully.")
            else:
                print("Failed to update profile.")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    def view_student_courses(self):
        """View courses enrolled by current student"""
        print("\n--- My Courses ---")
        try:
            with SISServiceImpl() as service:
                courses = service.get_courses_by_student(self.current_user.student_id)
                
                if not courses:
                    print("You are not enrolled in any courses.")
                    return
                
                print("\nEnrolled Courses:")
                print(f"{'ID':<5}{'Code':<10}{'Name':<25}{'Credits':<8}{'Teacher':<20}")
                print("-" * 70)
                for course in courses:
                    print(f"{course.course_id:<5}{course.course_code:<10}{course.course_name[:20]:<25}{course.credits:<8}{course.teacher_name or 'Not assigned':<20}")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    def enroll_in_course(self):
        """Enroll current student in a course"""
        print("\n--- Enroll in Course ---")
        try:
            course_id = int(input("Enter Course ID to enroll: ").strip())
            
            enrollment = self.sis_service.enroll_student(self.current_user.student_id, course_id)
            print(f"Enrollment successful. Enrollment ID: {enrollment.enrollment_id}")
        except CourseNotFoundException:
            print("Error: Course not found.")
        except DuplicateEnrollmentException:
            print("Error: You are already enrolled in this course.")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    def view_payment_history(self):
        """View payment history of current student"""
        print("\n--- My Payment History ---")
        try:
            payments = self.sis_service.get_payments_by_student(self.current_user.student_id)
            
            if not payments:
                print("No payment history found.")
                return
            
            print("\nPayment History:")
            print("Date\t\tAmount")
            print("-" * 30)
            total = 0
            for payment in payments:
                print(f"{payment.payment_date}\t₹{payment.amount:.2f}")
                total += payment.amount
            print("-" * 30)
            print(f"Total Paid:\t₹{total:.2f}")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    def make_payment(self):
        """Make a payment for current student"""
        print("\n--- Make Payment ---")
        try:
            amount = float(input("Enter payment amount: ").strip())
            
            payment = self.sis_service.record_payment(self.current_user.student_id, amount)
            print(f"Payment of ₹{amount:.2f} recorded successfully. Payment ID: {payment.payment_id}")
        except PaymentValidationException as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    app = MainApp()
    app.run()