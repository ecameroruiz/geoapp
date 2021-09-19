"""
Database Tools
"""

import json
import os
import psycopg2
import pandas as pd
from psycopg2 import extras


class DatabaseTools:
    """
    DB connection
    """

    def __init__(self):
        self.db_credentials = self.get_db_credentials()

    @staticmethod
    def get_db_credentials():
        """
        Reads DB credentials
        """
        current_path = os.path.dirname(os.path.abspath(__file__))
        with open(current_path + '/credentials.json') as credentials_file:
            return json.load(credentials_file)

    def get_db_connection(self):
        """
        Creates DB connection
        """
        return psycopg2.connect(user=self.db_credentials['user'],
                                password=self.db_credentials['password'],
                                host=self.db_credentials['host'],
                                port=self.db_credentials['port'],
                                database=self.db_credentials['database'])

    def execute_sql(self, sql: str):
        """
        Execute SQL code and return cursor

        :param str sql: SQL to execute
        """
        cursor = self.get_db_connection().cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(sql)
        return cursor

    def execute_query(self, query: str):
        """
        Get SQL query results as list of dicts

        :param str query: Query to execute
        """
        cursor = self.execute_sql(query)
        rows = cursor.fetchall()
        cursor.close()
        return [dict(row) for row in rows]

    def create_table(self, table_name: str):
        """
        Creates table from sql file

        :param str table_name: Table / SQL file name
        """
        table_script = open(f"tables/{table_name}.sql")
        connection = self.get_db_connection()
        cursor = connection.cursor()
        cursor.execute(table_script.read())
        connection.commit()
        cursor.close()
        connection.close()
        table_script.close()

    def populate_table(self, table_name: str, dataframe: pd.DataFrame):
        """
        Populate a table in the database from a dataframe

        :param str table_name: The name of the table in the DB
        :param pd.DataFrame dataframe: The dataframe to populate the table
        """
        cursor = self.execute_sql(sql=f"SELECT * FROM {table_name} LIMIT 0")

        # get col names in right order for insertion
        col_names = [i[0] for i in cursor.description]
        dataframe = dataframe[col_names]

        connection = self.get_db_connection()
        cursor = connection.cursor()

        # insert each row of dataframe into table
        for index, row in dataframe.iterrows():
            cursor.execute(f"INSERT INTO {table_name} VALUES{tuple(row.values)}")
            connection.commit()

        cursor.close()
        connection.close()