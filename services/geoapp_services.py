"""
Geoapp Services
"""

from database.database_tools import DatabaseTools


class GeoAppServices:
    """
    GeoApp Services
    """

    def __init__(self):
        self.db_tools = DatabaseTools()

    def get_paystats(self):
        """
        Get paystats
        """
        query = "select amount, p_age, p_gender from paystats where p_age = '<=24'"
        result = self.db_tools.execute_query(query=query)
        return result

