import json
import sys


def read_file(values_path, tests_path):
    with open(values_path, 'r') as file:
        values_file = json.load(file)

    with open(tests_path, 'r') as file:
        tests_file = json.load(file)

    def add_values(data, values_dict):
        if isinstance(data, dict):
            for key in data:
                if key == 'id':
                    value_id = data[key]
                    if value_id in values_dict:
                        data['value'] = values_dict[value_id]
                else:
                    add_values(data[key], values_dict)
        elif isinstance(data, list):
            for item in data:
                add_values(item, values_dict)

    add_values(tests_file, values_file)
    return tests_file


values_path = sys.argv[1]
tests_path = sys.argv[2]
output_path = 'report.json'

new_data = read_file(values_path, tests_path)

with open(output_path, 'w') as file:
    json.dump(new_data, file, indent=4)
