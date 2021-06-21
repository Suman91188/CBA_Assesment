import json
from pprint import pprint

"""First of all we will read-in the JSON file using JSON module.
Then we will create a list of the data which we want to extract from each JSON file.
Then we will write the data from these multiple nested JSON file to a CSV file using the CSV Module."""

# with open("D://Projects_hands_on_suman//CBA//tests//q1Testdata.json") as f:
# import json
# import csv

"""  raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)"""

import csv
exampleFile = open('./q1.test_data')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

