import pandas as pd
from sodapy import Socrata


def extract_taxi():
    """
    Retrieves dataset using Socrata API
    :rtype taxi_df: Pandas dataframe produced by API request
    """
    
    # API authentications
    client = Socrata("data.cityofnewyork.us", None)

    results = client.get("t29m-gskq", limit=100)

    # Convert to pandas DataFrame
    taxi_df = pd.DataFrame.from_records(results)
    # print(taxi_df)

    return taxi_df
    