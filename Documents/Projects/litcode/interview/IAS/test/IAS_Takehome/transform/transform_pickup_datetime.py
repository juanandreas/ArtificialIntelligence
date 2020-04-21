from datetime import datetime

import pandas as pd


def transform_pickup_datetime(df):
    """
    Transforms tpep_pickup_datetime column to date and time columns
    :param df: Original dataframe 
    :rtype: Dataframe with tpep_pickup_datetime column transformed 
    """

    pu_dates = []
    pu_times = []
    for entry in pd.to_datetime(df['tpep_pickup_datetime']):
        pu_dates.append(entry.date())
        pu_times.append(entry.time())
    df['pu_date'] = pu_dates
    df['pu_time'] = pu_times
    
    return df.drop(columns = ['tpep_pickup_datetime'])
    