import sys

import pandas as pd
from sodapy import Socrata

import extract
from extract.extract_taxi import extract_taxi
from transform.transform_pickup_datetime import transform_pickup_datetime
from transform.split_date import split_date


def extract_transform_taxi():
    """
    Extracts taxi df with API or file if provided
    Transforms dataframe and filters through the necessary columns
    :rtype filtered_taxi_df: extracted df filtered and transformed
    """

    # extracts dataframe via API
    if len(sys.argv) == 1:
        taxi_df = extract_taxi()

    # extracts dataframe via provided file
    else:
        taxi_df = pd.read_csv(sys.argv[1])

    # filter necessary columns
    feature_cols = ["tpep_pickup_datetime",
                    "pulocationid",
                    "fare_amount",
                    ]
    filtered_taxi_df = taxi_df.filter(feature_cols)

    # transforms datetime columns into year, month, day, and time columns
    filtered_taxi_df = transform_pickup_datetime(filtered_taxi_df)
    filtered_taxi_df = split_date(filtered_taxi_df)

    return filtered_taxi_df
