import configparser
from pathlib import Path
from typing import Dict

def get_connection_string(config_file: str = 'config/db_config.ini') -> Dict[str, str]:
    """
    Read database configuration from file and return connection parameters
    
    Args:
        config_file: Path to configuration file (default: 'config/db_config.ini')
    
    Returns:
        Dictionary with connection parameters: host, database, user, password
    
    Raises:
        ValueError: If configuration file or MySQL section is missing
        FileNotFoundError: If config file doesn't exist
    """
    config_path = Path(__file__).parent.parent / config_file
    
    if not config_path.exists():
        raise FileNotFoundError(f"Database configuration file not found: {config_path}")
    
    config = configparser.ConfigParser()
    config.read(config_path)
    
    if not config.has_section('mysql'):
        raise ValueError("MySQL configuration not found in config file")
    
    required_keys = ['host', 'database', 'user', 'password']
    if not all(key in config['mysql'] for key in required_keys):
        missing = [key for key in required_keys if key not in config['mysql']]
        raise ValueError(f"Missing required MySQL configuration: {', '.join(missing)}")
    
    return {
        'host': config['mysql']['host'],
        'database': config['mysql']['database'],
        'user': config['mysql']['user'],
        'password': config['mysql']['password']
    }