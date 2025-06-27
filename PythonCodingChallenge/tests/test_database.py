import sys
import os
import pytest

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util.db_conn_util import DBConnUtil
from util.db_property_util import DBPropertyUtil
from dao.loan_repository_impl import LoanRepositoryImpl
from entity.customer import Customer
from exception.invalid_loan_exception import InvalidLoanException
from entity.home_loan import HomeLoan
from entity.car_loan import CarLoan

@pytest.fixture(scope="module")
def db_connection():
    """Fixture that provides a database connection"""
    connection_string = DBPropertyUtil.get_connection_string("db.properties")
    conn = DBConnUtil.get_connection(connection_string)
    yield conn
    conn.close()

@pytest.fixture
def loan_repo(db_connection):
    """Fixture that provides a LoanRepository instance"""
    return LoanRepositoryImpl()

def test_db_connection(db_connection):
    """Test database connection is established"""
    assert db_connection.is_connected()
    
    cursor = db_connection.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    cursor.close()
    
    assert result[0] == 1

def test_property_file_loading():
    """Test that db.properties file is loaded correctly"""
    connection_string = DBPropertyUtil.get_connection_string("db.properties")
    assert "host=" in connection_string
    assert "dbname=" in connection_string
    assert "user=" in connection_string
    assert "password=" in connection_string

def test_loan_repository_initialization(loan_repo):
    """Test that LoanRepositoryImpl initializes properly"""
    assert hasattr(loan_repo, 'connection')
    assert loan_repo.connection.is_connected()

@pytest.mark.xfail
def test_calculate_interest(loan_repo):
    """Test interest calculation"""
    # First create a test loan
    test_customer = Customer(customer_id=1)
    test_loan = HomeLoan(
        customer=test_customer,
        principal_amount=100000,
        interest_rate=7.5,
        loan_term=24,
        property_address="123 Test St",
        property_value=200000
    )
    
    # Apply loan and get its ID
    loan_repo.apply_loan(test_loan)
    cursor = loan_repo.connection.cursor()
    cursor.execute("SELECT LAST_INSERT_ID()")
    loan_id = cursor.fetchone()[0]
    cursor.close()
    
    try:
        # Test interest calculation
        interest = loan_repo.calculate_interest(loan_id)
        expected_interest = (100000 * 7.5 * 24) / (12 * 100)
        assert interest == pytest.approx(expected_interest)
        
        # Test with invalid loan ID
        with pytest.raises(InvalidLoanException):
            loan_repo.calculate_interest(99999)
            
    finally:
        # Clean up
        cursor = loan_repo.connection.cursor()
        cursor.execute(f"DELETE FROM Loan WHERE loan_id = {loan_id}")
        loan_repo.connection.commit()
        cursor.close()

def test_loan_status_update(loan_repo):
    """Test loan status update based on credit score"""
    # Create test customer with known credit score
    cursor = loan_repo.connection.cursor()
    cursor.execute("""
        INSERT INTO Customer 
        (name, email_address, phone_number, address, credit_score)
        VALUES ('Test User', 'test@example.com', '1234567890', 'Test Address', 700)
    """)
    customer_id = cursor.lastrowid
    
    # Create test loan
    cursor.execute(f"""
        INSERT INTO Loan 
        (customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status)
        VALUES ({customer_id}, 100000, 7.5, 24, 'HomeLoan', 'Pending')
    """)
    loan_id = cursor.lastrowid
    cursor.close()
    
    try:
        # Test status update (should approve since credit score > 650)
        status = loan_repo.loan_status(loan_id)
        assert status == "Approved"
        
        # Verify in database
        cursor = loan_repo.connection.cursor(dictionary=True)
        cursor.execute(f"SELECT loan_status FROM Loan WHERE loan_id = {loan_id}")
        db_status = cursor.fetchone()['loan_status']
        cursor.close()
        assert db_status == "Approved"
        
    finally:
        # Clean up
        cursor = loan_repo.connection.cursor()
        cursor.execute(f"DELETE FROM Loan WHERE loan_id = {loan_id}")
        cursor.execute(f"DELETE FROM Customer WHERE customer_id = {customer_id}")
        loan_repo.connection.commit()
        cursor.close()

@pytest.mark.xfail
def test_emi_calculation(loan_repo):
    """Test EMI calculation"""
    # First create a test loan
    test_customer = Customer(customer_id=1)
    test_loan = HomeLoan(
        customer=test_customer,
        principal_amount=100000,
        interest_rate=7.5,
        loan_term=24,
        property_address="123 Test St",
        property_value=200000
    )
    
    # Apply loan and get its ID
    loan_repo.apply_loan(test_loan)
    cursor = loan_repo.connection.cursor()
    cursor.execute("SELECT LAST_INSERT_ID()")
    loan_id = cursor.fetchone()[0]
    cursor.close()
    
    try:
        # Test EMI calculation with loan ID
        emi = loan_repo.calculate_emi(loan_id)
        
        # Manual calculation for verification
        principal = test_loan.get_principal_amount()
        rate = test_loan.get_interest_rate()
        term = test_loan.get_loan_term()
        
        monthly_rate = rate / 12 / 100
        expected_emi = (principal * monthly_rate * (1 + monthly_rate)**term) / ((1 + monthly_rate)**term - 1)
        
        assert emi == pytest.approx(expected_emi, rel=1e-3)
        
    finally:
        # Clean up
        cursor = loan_repo.connection.cursor()
        cursor.execute(f"DELETE FROM Loan WHERE loan_id = {loan_id}")
        loan_repo.connection.commit()
        cursor.close()