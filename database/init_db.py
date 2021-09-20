#!/usr/local/bin/python3

import os
import pandas as pd
from database_tools import DatabaseTools

# instantiate db tools
db_tools = DatabaseTools()


def set_up_table(table_name: str, dataframe: pd.DataFrame):
    """
    Creates and populates Db table

    :param str table_name: Table / SQL file name
    :param pd.DataFrame dataframe: Dataframe
    """
    db_tools.create_table(table_name=table_name)
    db_tools.populate_table(table_name=table_name, dataframe=dataframe)


# get csv files as dataframes
current_path = os.path.dirname(os.path.abspath(__file__))
postal_codes = pd.read_csv(current_path + f"/../data/postal_codes.csv")
paystats = pd.read_csv(current_path + f"/../data/paystats.csv")
users = pd.read_csv(current_path + f"/../data/users.csv")

# clean data: some postal code ids from paystats are not in postal codes ids
valid_postal_code_ids = postal_codes['id'].tolist()
paystats = paystats[paystats['postal_code_id'].isin(valid_postal_code_ids)]

# set up tables
set_up_table(table_name="postal_codes", dataframe=postal_codes)
set_up_table(table_name="paystats", dataframe=paystats)
set_up_table(table_name="users", dataframe=users)
