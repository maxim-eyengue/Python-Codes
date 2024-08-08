"""This module extracts information from our `.env` file so that
we can use our MongoDB connection information in notebooks safely.
"""

# The os library allows us to communicate with a computer's
# operating system: https://docs.python.org/3/library/os.html
import os

# pydantic used for data validation: https://pydantic-docs.helpmanual.io/
from pydantic import BaseModel

class User(BaseModel):
    """Uses pydantic to define settings for project."""
    name: str
    password: str
    
# Info to connect to the corresponding database
external_data = {
    "name": "maxim-mongo",
    "password": "37MongoPass"
}

# Create instance of `Settings` class that will be imported
user = User(**external_data)
