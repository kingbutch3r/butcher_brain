import csv
import json
import sys

# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json():
    csvFilePath= sys.argv[0]
    jsonFilePath= sys.argv[1]
    # create a dictionary
    data = {}
    
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
             
            # Assuming a column named 'No' to
            # be the primary key
            key = rows['Subdomain']
            data[key] = rows
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
if __name__ == '__main__':
    make_json()        