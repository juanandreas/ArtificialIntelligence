import pandas as pd


def split_date(df):
    """
    Transforms date column from yyyy-mm-dd into separate year, month, day columns
    :param df: Original dataframe 
    :rtype: Dataframe with date column dropped and transformed 
    """
    
    # Create new columns
    df['pu_day'] = pd.DatetimeIndex(df['pu_date']).day
    df['pu_month'] = pd.DatetimeIndex(df['pu_date']).month
    df['pu_year'] = pd.DatetimeIndex(df['pu_date']).year

    return df.drop(columns = ['pu_date'])
    