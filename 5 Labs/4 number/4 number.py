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
















