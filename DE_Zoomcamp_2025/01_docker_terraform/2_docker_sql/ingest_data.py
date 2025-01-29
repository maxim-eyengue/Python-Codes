#!/usr/bin/env python
# coding: utf-8
#### Data Ingestion

# Necessary import
import os
import argparse # to parse command-line arguments and get named arguments
import pandas as pd
from time import time
from sqlalchemy import create_engine

# Main function for ingesting data
def main(params):
    # Unpack parameters
    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    table_name = params.table_name
    url = params.url

    # Create a connection to postgres
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # Get the correct data file extension for pandas to be able to open the file
    if url.endswith('.csv.gz'): # if it is a backup file as they are gzipped
        csv_name = 'output.csv.gz'
    else: # if it is a csv file
        csv_name = 'output.csv'
    # Download the file containing the data
    os.system(f"wget {url} -O {csv_name}")

    # Create an iterator to chunk the original data set into chunk of 100,000 rows
    df_iter = pd.read_csv(csv_name, iterator = True, chunksize = 100000)
    # Get an iteration
    df = next(df_iter)
    # Convert dates from text format to time
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    # Add data (0 row all columns) to the database - just to create a table
    df.head(n = 0).to_sql(name = table_name, con = engine, if_exists = 'replace')
    df.to_sql(name = table_name, con = engine, if_exists = 'append') # adding some rows   
    # Attempt for adding the data
    try:
        print("Starting Data Upload...") # starting message
        for i, df in enumerate(df_iter): # Get the data set iteration and its type
            # Initialize starting time
            t_start = time()
        
            # Convert date from text to date-time format
            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        
            # Add the data to the database int the table `yellow_taxi_data`
            df.to_sql(name = table_name, con = engine, if_exists = 'append')
        
            # Ending time
            t_end = time()
        
            # Completion message for one operation
            print(f"Data Chunk Insertion - {i + 1} took {round(t_end - t_start, 3)} seconds.")
    # Catch error if any
    except Exception as e:
        print(f"Error: {e}.") # print error
    # after completion
    else:
        print("Operation Terminated.") # Completion message

# If the script is executed
if __name__ == '__main__':
    # Set the description that will be printed in help
    parser = argparse.ArgumentParser(description = 'Ingest CSV data to Postgres')
    # Get the user, password, host, port, database name, table name and zip data url parameters
    parser.add_argument('--user', required = True, help = 'user name for postgres')
    parser.add_argument('--password', required = True, help = 'password for postgres')
    parser.add_argument('--host', required = True, help = 'host for postgres')
    parser.add_argument('--port', required = True, help = 'port for postgres')
    parser.add_argument('--db', required = True, help = 'database name for postgres')
    parser.add_argument('--table_name', required = True,
                        help = 'name of the table where we will write the results to')
    parser.add_argument('--url', required = True, help = 'url of the data file')
    # Parse the parameters
    args = parser.parse_args()

    # Ingest data with corresponding function
    main(args)


# ---