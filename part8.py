import csv
import json

# Наименование файла с дампом данных
JSON_FILENAME = 'data.json'


# Функция получения экземпляра класса для записи CSV
def get_csv_writer(filestream, fieldnames):
    return csv.DictWriter(
                filestream, # Файловый поток
                fieldnames=fieldnames, # Наименования полей словаря и заголовков CSV файла
                delimiter=',', # Разделитель CSV файла
                quotechar='"', # Кавычки для обрамления текстовых значений, содержащих символ-разделитель
                quoting=csv.QUOTE_MINIMAL # Политика расстановки кавычек
            )


# Функция получения экземпляра класса для чтения CSV
def get_csv_reader(filestream, fieldnames):
    return csv.DictReader(
                filestream,
                fieldnames=fieldnames,
                delimiter=',',
                quotechar='"',
                quoting=csv.QUOTE_MINIMAL
            )

# Функция получения данных из json-файла
def get_data_from_json(filename):
    with open(filename, 'r') as file:
        data = file.read()

    return json.loads(data)

def main():
    json_dict = get_data_from_json(JSON_FILENAME)
    data_list = json_dict['data']

    #fieldnames = data_list[0].keys()
    myfieldnames = dict.fromkeys(['Lux', 'Pulsation', 'Proximity', 'analogRead(A0)']).keys()


    # Создание CSV-файла
    with open("data.csv", "w") as csv_file:
        # Получение объекта для работы с CSV
        csv_writer = get_csv_writer(csv_file, myfieldnames)

        # Запись заголовков в CSV файл, переданных в поле fieldnames
        csv_writer.writeheader()

        # Запись данных в CSV файл
        for info_dict in data_list:
            csv_writer.writerow(info_dict)

if __name__ == "__main__":
    main()
