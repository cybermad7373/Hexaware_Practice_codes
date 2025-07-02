import mysql.connector
from mysql.connector import Error
from typing import List, Optional
from datetime import date

from entity.student import Student
from entity.course import Course
from entity.enrollment import Enrollment
from entity.teacher import Teacher
from entity.payment import Payment

from exception.student_not_found_exception import StudentNotFoundException
from exception.course_not_found_exception import CourseNotFoundException
from exception.teacher_not_found_exception import TeacherNotFoundException
from exception.duplicate_enrollment_exception import DuplicateEnrollmentException
from exception.payment_validation_exception import PaymentValidationException

from util.db_conn_util import DBConnUtil
from util.security_util import SecurityUtil
from util.validation_util import ValidationUtil

from .sis_service import SISService


class SISServiceImpl(SISService):
    """Concrete implementation of SISService with MySQL backend"""
    
    def __init__(self):
        self.connection = None
            
    def __enter__(self):
        self.connection = DBConnUtil.get_connection()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            if exc_type is None:
                self.connection.commit()
            else:
                self.connection.rollback()
            self.connection.close()
            
    def authenticate_student(self, email: str, password: str) -> Student:
        """Authenticate a student with email and password"""
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM Students WHERE email = %s"
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            
            if not result:
                raise StudentNotFoundException(email)
            
            if not SecurityUtil.verify_password(result['password_hash'], password):
                raise ValueError("Invalid password")
                
            return Student(
                student_id=result['student_id'],
                first_name=result['first_name'],
                last_name=result['last_name'],
                date_of_birth=result['date_of_birth'],
                email=result['email'],
                phone_number=result['phone_number']
            )
        except Error as e:
            raise Exception(f"Database error: {e}")            
    
    # ========== Student Operations ==========
    def add_student(self, student: Student, password: str) -> Student:
        if not ValidationUtil.validate_email(student.email):
            raise ValueError("Invalid email format")
        if not ValidationUtil.validate_phone(student.phone_number):
            raise ValueError("Invalid phone number format")
        
        try:
            cursor = self.connection.cursor(dictionary=True)
            
            # Check for existing email
            cursor.execute("SELECT student_id FROM Students WHERE email = %s", (student.email,))
            if cursor.fetchone():
                raise ValueError("Email already registered")
            
            # Hash password
            password_hash = SecurityUtil.hash_password(password)
            
            # Insert student
            query = """
            INSERT INTO Students 
            (first_name, last_name, date_of_birth, email, phone_number, password_hash)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                student.first_name,
                student.last_name,
                student.date_of_birth,
                student.email,
                student.phone_number,
                password_hash
            ))
            
            student.student_id = cursor.lastrowid
            return student
            
        except Error as e:
            raise Exception(f"Database error: {e}")
    
    def get_student(self, student_id: int) -> Student:
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM Students WHERE student_id = %s"
            cursor.execute(query, (student_id,))
            result = cursor.fetchone()
            
            if not result:
                raise StudentNotFoundException(student_id)
                
            return Student(
                student_id=result['student_id'],
                first_name=result['first_name'],
                last_name=result['last_name'],
                date_of_birth=result['date_of_birth'],
                email=result['email'],
                phone_number=result['phone_number']
            )
        except Error as e:
            raise Exception(f"Database error: {e}")
    
    def authenticate_student(self, email: str, password: str) -> Student:
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM Students WHERE email = %s"
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            
            if not result:
                raise StudentNotFoundException(f"Email {email} not found")
            
            if not SecurityUtil.verify_password(result['password_hash'], password):
                raise ValueError("Invalid password")
                
            return Student(
                student_id=result['student_id'],
                first_name=result['first_name'],
                last_name=result['last_name'],
                date_of_birth=result['date_of_birth'],
                email=result['email'],
                phone_number=result['phone_number']
            )
        except Error as e:
            raise Exception(f"Database error: {e}")
    
    def update_student(self, student: Student) -> bool:
        try:
            cursor = self.connection.cursor()
            query = """
            UPDATE Students 
            SET first_name = %s, last_name = %s, date_of_birth = %s, 
                email = %s, phone_number = %s
            WHERE student_id = %s
            """
            cursor.execute(query, (
                student.first_name,
                student.last_name,
                student.date_of_birth,
                student.email,
                student.phone_number,
                student.student_id
            ))
            return cursor.rowcount > 0
        except Error as e:
            raise Exception(f"Database error: {e}")
    
    # ========== Course Operations ==========
    def add_course(self, course: Course) -> Course:
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = """
            INSERT INTO Courses 
            (course_name, course_code, credits, teacher_id)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (
                course.course_name,
                course.course_code,
                course.credits,
                course.teacher_id
            ))
            
            course.course_id = cursor.lastrowid
            return course
        except Error as e:
            raise Exception(f"Database error: {e}")
    
    def get_course(self, course_id: int) -> Course:
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = """
            SELECT c.*, t.first_name as teacher_first_name, t.last_name as teacher_last_name
            FROM Courses c
            LEFT JOIN Teachers t ON c.teacher_id = t.teacher_id
            WHERE c.course_id = %s
            """
            cursor.execute(query, (course_id,))
            result = cursor.fetchone()
            
            if not result:
                raise CourseNotFoundException(course_id)
                
            return Course(
                course_id=result['course_id'],
                course_name=result['course_name'],
                course_code=result['course_code'],
                credits=result['credits'],
                teacher_id=result['teacher_id'],
                teacher_name=f"{result['teacher_first_name']} {result['teacher_last_name']}" 
                    if result['teacher_first_name'] else None
            )
        except Error as e:
            raise Exception(f"Database error: {e}")

    def get_all_courses(self) -> List[Course]:
        """Get all courses with teacher information"""
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = """
            SELECT c.*, t.first_name as teacher_first_name, t.last_name as teacher_last_name
            FROM Courses c
            LEFT JOIN Teachers t ON c.teacher_id = t.teacher_id
            """
            cursor.execute(query)
            courses = []
            for row in cursor.fetchall():
                teacher_name = f"{row['teacher_first_name']} {row['teacher_last_name']}" if row['teacher_id'] else None
                courses.append(Course(
                    course_id=row['course_id'],
                    course_name=row['course_name'],
                    course_code=row['course_code'],
                    credits=row['credits'],
                    teacher_id=row['teacher_id'],
                    teacher_name=teacher_name
                ))
            return courses
        except Error as e:
            raise Exception(f"Database error: {e}")
        finally:
            if 'cursor' in locals():
                cursor.close()

    def get_courses_by_student(self, student_id: int) -> List[Course]:
        """Get courses a student is enrolled in"""
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = """
            SELECT c.*, t.first_name as teacher_first_name, t.last_name as teacher_last_name
            FROM Courses c
            JOIN Enrollments e ON c.course_id = e.course_id
            LEFT JOIN Teachers t ON c.teacher_id = t.teacher_id
            WHERE e.student_id = %s
            """
            cursor.execute(query, (student_id,))
            courses = []
            for row in cursor.fetchall():
                teacher_name = f"{row['teacher_first_name']} {row['teacher_last_name']}" if row['teacher_id'] else None
                courses.append(Course(
                    course_id=row['course_id'],
                    course_name=row['course_name'],
                    course_code=row['course_code'],
                    credits=row['credits'],
                    teacher_id=row['teacher_id'],
                    teacher_name=teacher_name
                ))
            return courses
        except Error as e:
            raise Exception(f"Database error: {e}")
        finally:
            if 'cursor' in locals():
                cursor.close()
    
    def assign_teacher_to_course(self, teacher_id: int, course_id: int) -> bool:
        try:
            # Verify teacher exists
            cursor = self.connection.cursor()
            cursor.execute("SELECT teacher_id FROM Teachers WHERE teacher_id = %s", (teacher_id,))
            if not cursor.fetchone():
                raise TeacherNotFoundException(teacher_id)
            
            # Verify course exists
            cursor.execute("SELECT course_id FROM Courses WHERE course_id = %s", (course_id,))
            if not cursor.fetchone():
                raise CourseNotFoundException(course_id)
            
            # Assign teacher
            query = "UPDATE Courses SET teacher_id = %s WHERE course_id = %s"
            cursor.execute(query, (teacher_id, course_id))
            return cursor.rowcount > 0
        except Error as e:
            raise Exception(f"Database error: {e}")
    
    # ========== Enrollment Operations ==========
    def enroll_student(self, student_id: int, course_id: int) -> Enrollment:
        try:
            cursor = self.connection.cursor(dictionary=True)
            
            # Verify student exists
            cursor.execute("SELECT student_id FROM Students WHERE student_id = %s", (student_id,))
            if not cursor.fetchone():
                raise StudentNotFoundException(student_id)
            
            # Verify course exists
            cursor.execute("SELECT course_id FROM Courses WHERE course_id = %s", (course_id,))
            if not cursor.fetchone():
                raise CourseNotFoundException(course_id)
            
            # Check for existing enrollment
            cursor.execute(
                "SELECT enrollment_id FROM Enrollments WHERE student_id = %s AND course_id = %s",
                (student_id, course_id)
            )
            if cursor.fetchone():
                raise DuplicateEnrollmentException(student_id, course_id)
            
            # Create enrollment
            query = """
            INSERT INTO Enrollments (student_id, course_id, enrollment_date)
            VALUES (%s, %s, CURDATE())
            """
            cursor.execute(query, (student_id, course_id))
            
            return Enrollment(
                enrollment_id=cursor.lastrowid,
                student_id=student_id,
                course_id=course_id,
                enrollment_date=date.today()
            )
        except Error as e:
            raise Exception(f"Database error: {e}")
    
    def get_enrollments_by_student(self, student_id: int) -> List[Enrollment]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = """
            SELECT e.*, c.course_name
            FROM Enrollments e
            JOIN Courses c ON e.course_id = c.course_id
            WHERE e.student_id = %s
            """
            cursor.execute(query, (student_id,))
            
            enrollments = []
            for row in cursor.fetchall():
                enrollments.append(Enrollment(
                    enrollment_id=row['enrollment_id'],
                    student_id=row['student_id'],
                    course_id=row['course_id'],
                    enrollment_date=row['enrollment_date'],
                    course_name=row['course_name']
                ))
            
            return enrollments
        except Error as e:
            raise Exception(f"Database error: {e}")
    
    # ========== Payment Operations ==========
    def record_payment(self, student_id: int, amount: float) -> Payment:
        if amount <= 0:
            raise PaymentValidationException("Payment amount must be positive")
        
        try:
            cursor = self.connection.cursor(dictionary=True)
            
            # Verify student exists
            cursor.execute("SELECT student_id FROM Students WHERE student_id = %s", (student_id,))
            if not cursor.fetchone():
                raise StudentNotFoundException(student_id)
            
            # Record payment
            query = """
            INSERT INTO Payments (student_id, amount, payment_date)
            VALUES (%s, %s, CURDATE())
            """
            cursor.execute(query, (student_id, amount))
            
            return Payment(
                payment_id=cursor.lastrowid,
                student_id=student_id,
                amount=amount,
                payment_date=date.today()
            )
        except Error as e:
            raise Exception(f"Database error: {e}")
    
    def get_payments_by_student(self, student_id: int) -> List[Payment]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = """
            SELECT * FROM Payments 
            WHERE student_id = %s
            ORDER BY payment_date DESC
            """
            cursor.execute(query, (student_id,))
            
            payments = []
            for row in cursor.fetchall():
                payments.append(Payment(
                    payment_id=row['payment_id'],
                    student_id=row['student_id'],
                    amount=float(row['amount']),
                    payment_date=row['payment_date']
                ))
            
            return payments
        except Error as e:
            raise Exception(f"Database error: {e}")
    
    # ========== Report Generation ==========
    def generate_enrollment_report(self, course_id: int) -> dict:
        try:
            cursor = self.connection.cursor(dictionary=True)
            
            # Get course info
            course = self.get_course(course_id)
            
            # Get enrollments
            query = """
            SELECT s.student_id, s.first_name, s.last_name, e.enrollment_date
            FROM Enrollments e
            JOIN Students s ON e.student_id = s.student_id
            WHERE e.course_id = %s
            ORDER BY e.enrollment_date
            """
            cursor.execute(query, (course_id,))
            
            enrollments = []
            for row in cursor.fetchall():
                enrollments.append({
                    'student_id': row['student_id'],
                    'student_name': f"{row['first_name']} {row['last_name']}",
                    'enrollment_date': row['enrollment_date']
                })
            
            return {
                'course_id': course.course_id,
                'course_name': course.course_name,
                'teacher': course.teacher_name,
                'enrollment_count': len(enrollments),
                'enrollments': enrollments
            }
        except Error as e:
            raise Exception(f"Database error: {e}")
    
    def generate_payment_report(self, student_id: int) -> dict:
        try:
            student = self.get_student(student_id)
            payments = self.get_payments_by_student(student_id)
            
            total_paid = sum(p.amount for p in payments)
            
            return {
                'student_id': student.student_id,
                'student_name': f"{student.first_name} {student.last_name}",
                'total_payments': len(payments),
                'total_amount': total_paid,
                'payments': [{
                    'payment_id': p.payment_id,
                    'amount': p.amount,
                    'date': p.payment_date
                } for p in payments]
            }
        except Error as e:
            raise Exception(f"Database error: {e}")