# Excel-mongo-data-sync

Importing data from Excel to MongoDB into one collection and making a relation with
Another collection using Pandas


# Prerequisites

Python 3.x

pymongo  (pip install pymongo).

pandas  (pip install pandas).

MongoDB server.

# Usage

Install the necessary Python libraries and ensure that a MongoDB server is running.

Save the Excel file ('xxxxx.xlsx') in the specified location ('FilePath').

Update the MongoDB connection details in the code if necessary. By default,e it connects to a MongoDB server running on 'localhost' at 'port 27017'.

Run the Python script.

The script will connect to the MongoDB database and insert the data from the Excel file into the 'mandal_master' collection.
