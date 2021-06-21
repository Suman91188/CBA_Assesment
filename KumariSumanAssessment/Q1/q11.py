import csv
import json

a_dictionary = {}
a_file = open('./q1.test_data')
for line in a_file:
    key, value = line.split("\n")


    a_dictionary[key] = value

# print(a_dictionary)
keys = a_dictionary.keys()
# values = a_dictionary.values()

# printing keys and values separately
# print(str(keys))
print ("keys : ", str(keys))
# print("values : ", str(values))
# print(a_dictionary["smh_seg_id"])
# json_object = json.dumps(a_dictionary, indent = 2)
# print(json_object)
# now we will open a file for writing
# data_file = open('data_file.csv', 'w')
#
# # create the csv writer object
# csv_writer = csv.writer(data_file)

# smh_seg_id  smh_seg_version smh_msg_version smh_tran_type smh_cust_type smh_tran_num smh_corr_id smh_activity_detail sub_seg_id
# sub_seg_version sub_api_processing sub_rur_persistence rur_seg_id rur_seg_version smh_seg_id smh_seg_version smh_msg_version

# csv_columns = ['smh_seg_id','smh_seg_version','smh_msg_version']
# try:
#     with open("data_file.csv", 'w') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#         writer.writeheader()
#         for data in a_dictionary:
#             writer.writerow(data)
# except IOError:
#     print("I/O error")