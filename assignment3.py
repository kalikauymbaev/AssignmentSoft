import json
import os
import sqlite3
import threading
from typing import Any, Dict

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()
    
    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def _initialize_instance(cls, config: Dict[str, str]):
        cls._hostname = config['hostname']
        cls._username = config['username']
        cls._password = config['password']
        cls._database_name = config['database_name']
        cls._connect_to_database()

    @classmethod
    def _connect_to_database(cls):
        # This example uses sqlite3; adjust as needed for your specific database.
        cls._connection = sqlite3.connect(cls._database_name)
        cls._cursor = cls._connection.cursor()

    @classmethod
    def instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls.__new__(cls)
                    config = cls._load_config()
                    cls._initialize_instance(config)
        return cls._instance

    @staticmethod
    def _load_config():
        # Construct the path to the configuration file assuming it's in the current directory
        dir_path = os.path.dirname(os.path.realpath(__file__))  # Gets the directory where this script is located
        config_path = os.path.join(dir_path, 'db_config.json')  # Path to the config file in the same directory
        
        # Load and return the configuration
        with open(config_path, 'r') as file:
            return json.load(file)

    def execute_query(self, query: str) -> Any:
        self._cursor.execute(query)
        return self._cursor.fetchall()

    def commit(self):
        self._connection.commit()

    def get_connection_info(self) -> Dict[str, str]:
        return {
            'hostname': self._hostname,
            'username': self._username,
            'password': self._password,
            'database_name': self._database_name
        }

    def close_connection(self):
        self._connection.close()

# Test program
def test_program():
    # Assuming db_config.json exists in the user's home directory with proper database connection information
    db_connection = DatabaseConnection.instance()
    
    # Print the connection info to verify the correct loading of configuration and instantiation
    print(db_connection.get_connection_info())

    # Here you can add queries to test the database interaction, for example:
    # results = db_connection.execute_query('SELECT * FROM your_table')
    # print(results)

    # Close the connection when done.
    db_connection.close_connection()

if __name__ == "__main__":
    test_program()
