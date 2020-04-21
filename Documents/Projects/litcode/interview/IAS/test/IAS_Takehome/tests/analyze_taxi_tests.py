import sys
sys.path.append('../')
import datetime

import pandas as pd
from pandas.util.testing import assert_frame_equal

import agg
from agg.most_least_profitable import most_least_profitable
import transform
from transform.transform_pickup_datetime import transform_pickup_datetime
from transform.split_date import split_date


# test transform
def test_transform_pickup_datetime():
    """
    Test for successful transformation of datetime column to date and time columns
    """
    test_df = pd.DataFrame(
        [["11/04/2084 05:32:24 PM"]],
        columns=['tpep_pickup_datetime'])
    tested_df = transform_pickup_datetime(test_df)

    assert_df = pd.DataFrame(
        [[datetime.date(2084, 11, 4), datetime.time(17, 32, 24)]],
        columns=['pu_date', 'pu_time'])

    assert_frame_equal(assert_df, tested_df)


def test_split_date():
    """
    Test for successful transformation of date column to day, month, year columns
    """
    test_df = pd.DataFrame(
        [datetime.date(2084, 11, 4)],
        columns=['pu_date'])
    tested_df = split_date(test_df)

    assert_df = pd.DataFrame(
        [[4, 11, 2084]],
        columns=['pu_day', 'pu_month', 'pu_year'])

    assert_frame_equal(assert_df, tested_df)


# test agg
def test_most_profitable():
    """
    Test for successful aggregation of max average
    """
    test_df = pd.DataFrame(
        [[143, 20.0], 
        [143, 10.0], 
        [198, 12.0], 
        [198, 100.0]],
        columns=['pu_day', 'fare_amount'])
    test_most, _ = most_least_profitable(test_df, "Day")
    assert test_most == ("Day", 198, 56.0)


def test_least_profitable():
    """
    Test for successful aggregation of min average
    """
    test_df = pd.DataFrame(
        [[143, 20.0], 
        [143, 10.0], 
        [198, 12.0], 
        [198, 100]],
        columns=['pulocationid', 'fare_amount'])
    _, test_least = most_least_profitable(test_df, "Origin location")
    assert test_least == ("Origin location", 143, 15.0)
