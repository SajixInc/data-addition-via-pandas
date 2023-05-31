# Excel-mongo-data-sync

Importing data from excel to mongodb to one collection and making relation with
another colection using pandas


# Prerequisites

Python 3.x

pymongo  (pip install pymongo).

pandas  (pip install pandas).

MongoDB server.

# Usage

Install the necessary Python libraries and ensure that a MongoDB server is running.

Save the Excel file ('Distict_Mandals.xlsx') in the specified location ('C:\Users\LT-VFY-DL-012022-037\Downloads\').

Update the MongoDB connection details in the code if necessary. By default, it connects to a MongoDB server running on 'localhost' at 'port 27017'.

Run the Python script.

The script will connect to the MongoDB database and insert the data from the Excel file into the 'mandal_master' collection.
