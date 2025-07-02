import hashlib
import os
import binascii
from typing import Tuple

class SecurityUtil:
    """
    Utility class for security-related operations like password hashing and verification
    """
    
    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hash a password with a randomly generated salt using PBKDF2-HMAC-SHA512
        
        Args:
            password: The plaintext password to hash
            
        Returns:
            str: The hashed password in format 'salt:hash'
        """
        if not password:
            raise ValueError("Password cannot be empty")
        
        # Generate a random salt
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        
        # Hash the password with the salt
        pwdhash = hashlib.pbkdf2_hmac(
            'sha512',
            password.encode('utf-8'),
            salt,
            100000  # Number of iterations
        )
        pwdhash = binascii.hexlify(pwdhash)
        
        # Return salt and hash concatenated
        return (salt + pwdhash).decode('ascii')
    
    @staticmethod
    def verify_password(stored_password: str, provided_password: str) -> bool:
        """
        Verify a stored password against one provided by user
        
        Args:
            stored_password: The stored hashed password
            provided_password: The password to verify
            
        Returns:
            bool: True if passwords match, False otherwise
            
        Raises:
            ValueError: If inputs are invalid
        """
        if not stored_password or not provided_password:
            raise ValueError("Both stored and provided passwords must be non-empty")
        
        # Extract salt and hash from stored password
        salt = stored_password[:64]  # SHA-256 produces 64 character hex
        stored_hash = stored_password[64:]
        
        # Hash the provided password with the same salt
        pwdhash = hashlib.pbkdf2_hmac(
            'sha512',
            provided_password.encode('utf-8'),
            salt.encode('ascii'),
            100000
        )
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        
        # Compare the hashes
        return pwdhash == stored_hash