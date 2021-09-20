"""
Registration Services
"""

from database.database_tools import DatabaseTools
from passlib.apps import custom_app_context as pwd_context


class AuthorizationServices:
    """
    GeoApp Services
    """

    def __init__(self):
        """
        Initialize db tools
        """
        self.db_tools = DatabaseTools()

    @staticmethod
    def __hash_password(password):
        """
        Hash password

        :param str password: Password to be hashed
        """
        return pwd_context.encrypt(password)

    @staticmethod
    def __verify_password(password, hashed_password):
        """
        Verify password against has

        :param str password: Password to check
        :param str hashed_password: Hashed password
        """
        return pwd_context.verify(password, hashed_password)

    def check_user_exists(self, username: str):
        """
        Checks if given username already exits on the database

        :param str username: Username to check
        """
        result = self.__get_user(username=username)
        return len(result) > 0

    def get_db_password(self, username: str):
        """
        Retrieves user's db password

        :param str username: Username to search
        """
        result = self.__get_user(username=username)
        return result[0].get('password') if result else None

    def save_user(self, username: str, password: str):
        """
        Saves user to DB

        :param str username: Username to save
        :param str password: Password to save
        """
        pw_hash = self.__hash_password(password=password)
        sql = f"INSERT INTO USERS(USERNAME, PASSWORD) VALUES ('{username}', '{pw_hash}')"
        connection = self.db_tools.get_db_connection()
        cursor = connection.cursor()
        connection.commit()
        cursor.execute(sql)
        cursor.close()
        connection.close()

    def verify_user(self, username: str, password: str):
        """
        Checks user exists and password is correct

        :param str username: Username to save
        :param str password: Password to password
        """
        result = self.__get_user(username=username)
        db_password = result[0].get('password') if result else ''
        return self.__verify_password(password=password, hashed_password=db_password)

    def __get_user(self, username: str):
        """
        Retrieves user by username

        :param str username: Username to search
        """
        query = f"SELECT USERNAME, PASSWORD FROM USERS WHERE USERNAME = '{username}'"
        return self.db_tools.execute_query(query=query)
