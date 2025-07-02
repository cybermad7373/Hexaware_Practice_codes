import re
from datetime import datetime
from typing import Optional

class ValidationUtil:
    """
    Utility class for validating various data formats
    """
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validate an email address format
        
        Args:
            email: The email address to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        if not email:
            return False
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validate_phone(phone: str) -> bool:
        """
        Validate a phone number format (Indian format)
        
        Args:
            phone: The phone number to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        if not phone:
            return False
        
        # Indian phone number regex (10 digits starting with 6-9)
        pattern = r'^[6-9]\d{9}$'
        return bool(re.match(pattern, phone))
    
    @staticmethod
    def validate_date(date_str: str, format: str = '%Y-%m-%d') -> bool:
        """
        Validate a date string format
        
        Args:
            date_str: The date string to validate
            format: The expected format (default: YYYY-MM-DD)
            
        Returns:
            bool: True if valid, False otherwise
        """
        if not date_str:
            return False
        
        try:
            datetime.strptime(date_str, format)
            return True
        except ValueError:
            return False
    
    @staticmethod
    def validate_name(name: str) -> bool:
        """
        Validate a person's name (letters, spaces, and certain special chars)
        
        Args:
            name: The name to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        if not name:
            return False
        
        pattern = r'^[a-zA-Z\s\.\'-]+$'
        return bool(re.match(pattern, name))
    
    @staticmethod
    def validate_amount(amount: Optional[float]) -> bool:
        """
        Validate a monetary amount
        
        Args:
            amount: The amount to validate
            
        Returns:
            bool: True if valid (positive number), False otherwise
        """
        return amount is not None and amount > 0