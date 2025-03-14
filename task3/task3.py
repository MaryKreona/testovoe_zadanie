import json

def load_json(file_path):
    """Загружает JSON из файла."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(data, file_path):
    """Сохраняет данные в JSON файл."""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def fill_values(tests, values_dict):
    """Рекурсивно заполняет поля 'value' в структуре tests."""
    if isinstance(tests, list):
        for item in tests:
            fill_values(item, values_dict)
    elif isinstance(tests, dict):
        if 'id' in tests and tests['id'] in values_dict:
            tests['value'] = values_dict[tests['id']]
        for key, value in tests.items():
            if isinstance(value, (dict, list)):
                fill_values(value, values_dict)

def main(values_path, tests_path, report_path):
    # Загружаем данные из файлов
    values_data = load_json(values_path)
    tests_data = load_json(tests_path)

    # Создаем словарь для быстрого поиска значений по id
    values_dict = {item['id']: item['value'] for item in values_data['values']}

    # Заполняем значения в структуре tests
    fill_values(tests_data, values_dict)

    # Сохраняем результат в report.json
    save_json(tests_data, report_path)

if __name__ == "__main__":
    # Пути к файлам
    values_path = 'values.json'
    tests_path = 'tests.json'
    report_path = 'report.json'

    # Запуск программы
    main(values_path, tests_path, report_path)