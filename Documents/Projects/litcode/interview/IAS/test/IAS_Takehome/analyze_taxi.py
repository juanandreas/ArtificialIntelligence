import agg
from agg.most_least_profitable import most_least_profitable
import transform
from transform.extract_transform_taxi import extract_transform_taxi


def print_agg(most, least):
    print("Most profitable {} w/ Average profit:".format(most[0]))
    print("{} {} at ${}".format(most[0], most[1], most[2]))

    print("Least profitable {} w/ Average profit:".format(least[0]))
    print("{} {} at ${}".format(least[0], least[1], least[2]))

if __name__ == '__main__':

    taxi_df = extract_transform_taxi()

    # writing df to csv
    # taxi_df.to_csv("taxi_analysis.csv", sep=',')

    most, least = most_least_profitable(taxi_df, "Hour")
    print_agg(most, least)

    most, least = most_least_profitable(taxi_df, "Day")
    print_agg(most, least)

    most, least = most_least_profitable(taxi_df, "Origin location")
    print_agg(most, least)

