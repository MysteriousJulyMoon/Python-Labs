'''
import json
import csv
import os
import sys

def json_to_csv(json_filename):
    with open(json_filename, 'r') as json_file:
        data = json.load(json_file)

    csv_filename = os.path.splitext(json_filename)[0] + ".csv"
    root_name = list(data.keys())[0]

    with open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(data[root_name][0].keys())

        for item in data[root_name]:
            writer.writerow(item.values())

    return csv_filename

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python json2csv.py example.json")
    else:
        json_filename = sys.argv[1]
        csv_filename = json_to_csv(json_filename)
        print(f"CSV файл создан: {csv_filename}")
'''


import json
import csv
import sys
import os

try:
    with open('example.json', 'r') as f:
        data = json.loads(f.read())

    output = ', '.join([*data[0]])
    print(output)
    for obj in data:
        output += f'\n{obj["ID"]},{obj["Age"]},{obj["Skills"]},{obj["First_name"]},{obj["Last_name"]}'
    print(output)
    with open('output.csv", "w') as f:
        f.write(output)

except Exception as ex:
    print(f'Error: {str(ex)}')
















