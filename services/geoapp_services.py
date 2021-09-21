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
        query = self.__get_query(column='code', value=zipcode)
        result = self.db_tools.execute_query(query=query)
        serialized = self.__serialize(key='age', data=result)
        return serialized

    def get_paystats_by_geometry(self, geometry: str):
        """
        Get paystats by age and gender given a WKB geometry

        :param str geometry: Geometry
        """
        query = self.__get_query(column='the_geom', value=geometry, compare_as_str=True)
        result = self.db_tools.execute_query(query=query)
        serialized = self.__serialize(key='age', data=result)
        return serialized

    def get_all_paystats(self):
        """
        Get all paystats by age and gender
        """
        query = self.__get_query(column='', value='', compare_as_str=False, apply_filter=False)
        result = self.db_tools.execute_query(query=query)
        serialized = self.__serialize(key='age', data=result)
        return serialized

    @staticmethod
    def __get_query(column: str, value: str, compare_as_str: bool = False, apply_filter: bool = True):
        """
        Generate query according to column / value to filter by

        :param str column: Column to filter by
        :param str value: Value to filter by
        :param bool compare_as_str: Compare between quotes if True
        :param bool apply_filter: Apply where clause if True
        """
        where_clause = ""
        if apply_filter:
            value_to_compare = f"'{value}'" if compare_as_str else f"{value}"
            where_clause = f"WHERE POSTAL_CODES.{column.upper()} = {value_to_compare}"
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
