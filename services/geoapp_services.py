"""
Geoapp Services
"""

from collections import defaultdict
from database.database_tools import DatabaseTools


class GeoAppServices:
    """
    GeoApp Services
    """

    def __init__(self):
        """
        Initialize db tools
        """
        self.db_tools = DatabaseTools()

    def get_paystats_by_zipcode(self, zipcode: str):
        """
        Get paystats by age and gender given a zipcode

        :param str zipcode: Zip Code
        """
        where = f"WHERE POSTAL_CODES.CODE = '{zipcode}'"
        query = self.__get_query(where_clause=where)
        result = self.db_tools.execute_query(query=query)
        serialized = self.__serialize(key='age', data=result)
        return serialized

    def get_paystats_by_geometry(self, geometry: str):
        """
        Get paystats by age and gender given a WKB geometry

        :param str geometry: Geometry
        """
        where = f"WHERE POSTAL_CODES.THE_GEOM = '{geometry}'"
        query = self.__get_query(where_clause=where)
        result = self.db_tools.execute_query(query=query)
        serialized = self.__serialize(key='age', data=result)
        return serialized

    def get_all_paystats(self):
        """
        Get all paystats by age and gender
        """
        query = self.__get_query(where_clause='')
        result = self.db_tools.execute_query(query=query)
        serialized = self.__serialize(key='age', data=result)
        return serialized

    @staticmethod
    def __get_query(where_clause: str):
        """
        Generate query according to conditions to filter by

        :param str where_clause: Filter to apply (if any)
        """
        return "SELECT PAYSTATS.P_AGE AS AGE, PAYSTATS.P_GENDER AS GENDER, SUM(PAYSTATS.AMOUNT) AS TURNOVER " \
               "FROM POSTAL_CODES " \
               "JOIN PAYSTATS " \
               "ON POSTAL_CODES.ID = PAYSTATS.POSTAL_CODE_ID " \
               "{where_clause} " \
               "GROUP BY PAYSTATS.P_AGE, PAYSTATS.P_GENDER " \
               "ORDER BY PAYSTATS.P_AGE ASC".format(where_clause=where_clause)

    @staticmethod
    def __serialize(key, data):
        """
        Creates a dictionary from given list of dicts grouped by given key

        :param str key: Key to group by
        :param list data: List of dicts
        """
        grouped = defaultdict(list)
        for item in data:
            # exclude grouping key
            copy = {k: v for k, v in item.items() if k != key}
            # format money field TODO: casting on query would be faster
            copy['turnover'] = "{:,.2f}€".format(copy['turnover'])
            grouped[item[key]].append(copy)
        return grouped
