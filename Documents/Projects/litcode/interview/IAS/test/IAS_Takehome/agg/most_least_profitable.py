from collections import defaultdict

import numpy as np
import pandas as pd


def most_least_profitable(df, category):
    """
    Constructs history for number of rides that occured on each numerical day
    Constructs sum of fares gained on each numerical day
    Calculates max and min averages using sums and number of rides (sum/rides)
    """
    
    num_rides = defaultdict(int)
    agg_sum = defaultdict(float)

    for _, row in df.iterrows():
        if category == "Hour":
            cat = row['pu_time'].hour
        elif category == "Day":
            cat = row['pu_day']
        else:
            cat = row['pulocationid']
        num_rides[cat] += 1
        agg_sum[cat] += float(row['fare_amount'])

    max_avg = -1
    max_avg_cat = None

    min_avg = float("inf")
    min_avg_cat = None

    for cat in num_rides:
        avg_money = agg_sum[cat] / num_rides[cat]
        if avg_money > max_avg:
            max_avg = avg_money
            max_avg_cat = cat

        if avg_money < min_avg:
            min_avg = avg_money
            min_avg_cat = cat

    most = (category, max_avg_cat, max_avg)
    least = (category, min_avg_cat, min_avg)

    return most, least
    