import json


def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def pull_values(tests, values_dict):
    if isinstance(tests, list):
        for item in tests:
            pull_values(item, values_dict)
    elif isinstance(tests, dict):
        if 'id' in tests and tests['id'] in values_dict:
            tests['value'] = values_dict[tests['id']]
        for key, value in tests.items():
            if isinstance(value, (dict, list)):
                pull_values(value, values_dict)


def main(values_path, tests_path, report_path):
    values_data = load_json(values_path)
    tests_data = load_json(tests_path)

    values_dict = {item['id']: item['value'] for item in values_data['values']}

    pull_values(tests_data, values_dict)

    save_json(tests_data, report_path)


values_path = 'values.json'
tests_path = 'tests.json'
report_path = 'report.json'
main(values_path, tests_path, report_path)
