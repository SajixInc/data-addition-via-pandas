import pymongo
# from database import x
x = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'IVINPRO',
        # Abhishek Commented port setting for database configuration, to be used only if database is on another instance
        'CLIENT': {
            'host': 'IP',
            'port': 27017,
            'username': 'UserName',
            'password': 'Password',
            'authsource': 'admin',
        }
    }}

username = x['default']
a = x['default']['NAME']


try:
    y = x['default']['CLIENT']
    myclient = pymongo.MongoClient(
        f"mongodb://{username['CLIENT']['username']}:{username['CLIENT']['password']}@{username['CLIENT']['host']}:27017/")
except:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")


# # client = MongoClient('mongodb://localhost:27017/')

mydb = myclient[a]


serialnum_table = mydb['serial_num_madugula']  ## data having with serial numbers 
voter_master_ivin_dummy = mydb['Voter_Master_List']  ## voter details collection table
madugula_not_import = mydb['madugula_not_import']  ## to store data which is not updated with serial number
serial_number_updated_ivinid = mydb['serial_number_updated_ivinid']  ## here storing ivinids which is updated serial number in to voter master
maduguladata = voter_master_ivin_dummy.find()
count = 1
maduguladata_list = list(maduguladata)
not_updated_data = []
import re
for i in range(0,len(maduguladata_list):
    # print(maduguladata_list[i],"kkk")
    if maduguladata_list[i]['Voter_Slip'] == "Null":
        pass
    else:
        slipname_madugula = 'slip' + maduguladata_list[i]['Voter_Slip'].split('slip')[1]
        print(slipname_madugula,"slipname_madugula")
        start_index = slipname_madugula.find(".pdf")
        # print(start_index,"kkk")
    #
        modified_string = slipname_madugula[:start_index]
        slipname_madugula = modified_string
        new_string = slipname_madugula.replace(".pdf", "")
        new_string = new_string.replace(".png", "")
        print(new_string)
        search_query = {'votere_slip': {'$regex': re.escape(new_string), '$options': 'i'}}
        print(search_query,"search_query")
        voter_slip = serialnum_table.find_one(search_query)
        if voter_slip:
            serial_number = voter_slip['SerialNumber']
            Main_TownORVillage = voter_slip['Main_TownORVillage']
            Police_Station = voter_slip['Police_Station']
            Revenue_Division = voter_slip['Revenue_Division']
            Pin_Code = voter_slip['Pin_Code']
            maduguladata_list[i]['SerialNumber'] = serial_number
            maduguladata_list[i]['Main_TownORVillage'] = Main_TownORVillage
            maduguladata_list[i]['Police_Station'] = Police_Station
            maduguladata_list[i]['Revenue_Division'] = Revenue_Division
            maduguladata_list[i]['Pin_Code'] = Pin_Code
            maduguladata_list[i]['SerialNumber'] = serial_number
            IvivnId = maduguladata_list[i]['ivin_id']
            document = {'Ivin_id': IvivnId}
            # Insert the document into the collection
            serial_number_updated_ivinid.insert_one(document)
            voter_master_ivin_dummy.update_one(
                {'_id': maduguladata_list[i]['_id']},
                {'$set': {
                    'Voter_SerialNumber': serial_number,
                    'Main_Town_OR_Village': Main_TownORVillage,
                    'Police_Station': Police_Station,
                    'Revenue_Division': Revenue_Division,
                    'Pin_Code': Pin_Code
                }},
            )
            count += 1
            print(count)
        else:
            count += 1
            print(count)
            print("No matching document found.")
            not_updated_data.append(maduguladata_list[i])
            madugula_not_import.insert_one(maduguladata_list[i])
print(len(not_updated_data), "length of not_updated_data")
print("Completed")
