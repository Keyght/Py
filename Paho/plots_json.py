from datetime import datetime

import matplotlib.pyplot as plt
import csv
import json


# Наименование файла с дампом данных
JSON_FILENAME = 'test-dump.json'


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


def create_plots(plots_data_lists):
    # Создание графиков для отрисовки данных
    fig, axs = plt.subplots(1, 3, figsize=(15,6)) # Получим окно с 1 колонкой и 2 столбцами графиков

    # fig - окно, в котором будут отрисовываться графики
    # axs содержит в себе список графиков для отрисовки на них значений

    # Формирование гистограммы
    axs[0].hist(plots_data_lists['humidity'])
    axs[0].set_xlabel('Humidity level')
    axs[0].set_ylabel('Count')
    axs[0].set_title('Humidity')

    axs[1].plot(plots_data_lists['timestamp'], plots_data_lists['temperature'])
    # Задание лейблов для осей и графика
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('Temperature level')
    axs[1].set_title('Temperature')

    labels = ['6.32-6.70', '6.71-7.12', '7.12-7.53']
    c1 = 0
    c2 = 0
    c3 = 0
    for i in plots_data_lists['voltage']:
        if 6.32 <= i <= 6.70:
          c1 += 1
        if 6.71 <= i <= 7.12:
          c2 += 1
        if 7.12 <= i <= 7.53:
          c3 += 1
    sizes = [c1, c2, c3]

    axs[2].pie(sizes, labels=labels)
    axs[2].axis('equal')
    axs[2].legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))
    axs[2].set_title('Voltage')

    return fig, axs


def main():
    json_dict = get_data_from_json(JSON_FILENAME)
    data_list = json_dict['data']

    fieldnames = data_list[0].keys()
    myfieldnames = dict.fromkeys(['timestamp', 'humidity', 'temperature', 'voltage']).keys()


    # Создание списков для хранения данных для графиков
    plots_data_lists = {
        'humidity': [],
        'temperature': [],
        'voltage': [],
        'timestamp': [],
    }

    # Создание CSV-файла
    with open("data2.csv", "w") as csv_file:
        # Получение объекта для работы с CSV
        csv_writer = get_csv_writer(csv_file, fieldnames)

        # Запись заголовков в CSV файл, переданных в поле fieldnames
        csv_writer.writeheader()

        # Запись данных в CSV файл
        for info_dict in data_list:
            csv_writer.writerow(info_dict)


    with open('data.csv', 'r') as csv_file:
        # Создание объекта для чтения CSV (параметры соответствуют DictWriter)
        csv_reader = get_csv_reader(csv_file, fieldnames)

        line_count = 0
        for row in csv_reader:
            # В нулевой строке всегда читается заголовок
            if line_count == 0:
                line_count += 1
                continue

            # Заполнение списков с данными, с преобразованием типов
            plots_data_lists['timestamp'].append(datetime.fromisoformat(row['timestamp']))
            plots_data_lists['humidity'].append(float(row['humidity']))
            plots_data_lists['temperature'].append(float(row['temperature']))
            plots_data_lists['voltage'].append(float(row['voltage']))

            line_count += 1

    fig, axs = create_plots(plots_data_lists)

    # Отрисовка окна
    plt.show()


if __name__ == "__main__":
    main()
