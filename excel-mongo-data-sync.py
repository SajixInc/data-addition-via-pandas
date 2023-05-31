
import pymongo

x = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'poltical_db',
        'CLIENT': {
            'host': 'IP',
            'port': 27017,
            'username': 'db_name',
            'password': 'password',
            'authsource': 'admin',
        }

    }

}



username = x['default']
try:
    y = x['default']['CLIENT']
    myclient = pymongo.MongoClient(
        f"mongodb://{username['CLIENT']['username']}:{username['CLIENT']['password']}@{username['CLIENT']['host']}:27017/")
except:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# client = MongoClient('mongodb://localhost:27017/')


db = myclient['poltical_db']
collection = db['mandal_master']

last_document = collection.find().sort("Mandal_id", -1).limit(1)


# Get the ID of the last document
last_id = last_document[0]['Mandal_id'] if last_document.count() > 0 else 0
# last_id = last_document[0]['id'] if last_document.count_documents({}) > 0 else 0



import pandas as pd
lists = []


district = db['District_Master'].find()
for i in district:
    print(i['District'])
    lists.append(i['District'])

print(lists)


df = pd.read_excel(r'C:\Users\LT-VFY-DL-012022-037\Downloads\Distict_Mandals.xlsx')

length = len(df)

for i in range(1, length):
    id_value = last_id + i
    filtered_data = df[df['SI.NO'] == id_value]
    mandal = filtered_data['Mandal'].iloc[0]
    district = filtered_data['District'].iloc[0]
    revenue_division = filtered_data['RevenueDivision'].iloc[0]
    if district in lists:
        # print(district, 'distttt')
        index = lists.index(district) + 1
        # print(index)

        document = {
            'Mandal_id': id_value,
            'District_id': index,
            'Mandal': mandal,
            'RevenueDivision': revenue_division,
            # Add more fields as needed
        }

        # Insert a single document
        collection.insert_one(document)


