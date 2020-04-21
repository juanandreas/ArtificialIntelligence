# A program that can parse the Taxi Rides data from NYC Open Data site and gives most/least profitable aspects.

### The program should determine the most/least profitable aspects of picking up a passenger by:

Categories              |
------------------------|
hour of day             |
day of month            |
origin location         |

## Setup

    pip install numpy
    pip install pandas
    pip install sodapy
    pip install pytest

This program requires the use of Python3.

## Filter used to download sample
This program downloads a subset of the dataset (first 100 rows) via the Socrata API.

This program also works with a locally provided dataset, as long as it is in the same format. However, the dataset provided by NYC Open Data may have some fields missing such as 'pulocation' (which is required for the 'origin location' category).

## Run

### Run program with Socrata API
    python3 analyze_taxi.py

### Run program with a local dataset
    python3 analyze_taxi.py <file_name>.csv

### Run unit tests
    Be in root directory
    cd tests

    pytest analyze_taxi_tests.py
                    OR
    python3 -m pytest analyze_taxi_tests.py

## Analysis
    
Average fare amounts are calculated based on every hour/day/pulocation available in the dataset.

Computation is done by aggregating the sum of every fare amount for each recorded hour/day/pulocation and that sum is divided by the number of occurences of rides in one specific hour/day/pulocation.

The maximum and minimum averages are taken as output for the most/least profitable aspects of picking up a passenger in the above mentioned Categories.

## Project Structure

### extract
    .
    ├── ...
    ├── extract                             # Data extraction files
    │   ├── extract_taxi.py                 # Retrieves dataset using Socrata API
    └── ...

### transform
    .
    ├── ...
    ├── transform                           # Transforms extracted data into a workable dataset
    │   ├── extract_transform_taxi.py       # Driver for extracting dataset, and transformations
    │   ├── split_date.py                   # Seprates pickup date column into year/month/day columns
    │   ├── transform_pickup_date.py        # Separates datetime column to date and time columns
    └── ...

### agg
    .
    ├── agg                                 # Library of aggregation functions
    │   ├── most_least_profitable.py        # Aggregates most/least profitable hours/days/pulocations
    └── ...

### tests
    .
    ├── ...
    ├── test                                # Test files
    │   └── analyze_taxi_tests.py           # Unit tests
    └── ...

### interface
    .
    ├── ...
    ├── analyze_taxi.py                     # Driver for extract, transform, and analyze
    └── README.md












The yellow and green taxi trip records include fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts. The data used in the attached datasets were collected and provided to the NYC Taxi and Limousine Commission (TLC) by technology providers authorized under the Taxicab & Livery Passenger Enhancement Programs (TPEP/LPEP). The trip data was not created by the TLC, and TLC makes no representations as to the accuracy of these data.