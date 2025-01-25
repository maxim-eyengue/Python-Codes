# Necessary import
import sys
import pandas as pd

# print command line arguments
print(sys.argv)
# Get the first command line argument as day
day = sys.argv[1]

# Check pandas and pipeline arguments
print(f"job finished with success the {day}: pandas version {pd.__version__}.")