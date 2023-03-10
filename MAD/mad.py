import csv

# Функция получения экземпляра класса для записи CSV
def get_csv_writer(filestream, fieldnames):
    return csv.DictWriter(
                filestream, # Файловый поток
                fieldnames=fieldnames, # Наименования полей словаря и заголовков CSV файла
                delimiter=';', # Разделитель CSV файла
                quotechar='"', # Кавычки для обрамления текстовых значений, содержащих символ-разделитель
                quoting=csv.QUOTE_MINIMAL # Политика расстановки кавычек
            )

# Функция получения экземпляра класса для чтения CSV
def get_csv_reader(filestream, fieldnames):
    return csv.DictReader(
                filestream,
                fieldnames=fieldnames,
                delimiter=';',
                quotechar='"',
                quoting=csv.QUOTE_MINIMAL
            )

def main():
    dic = {'dt=50' : 1, 'dt=150' : 2, 'dt=700' : 3,'dt=2000' : 4}
    fieldnames = dic.keys()
    data_list = {
        'dt=50': [],
        'dt=150': [],
        'dt=700': [],
        'dt=2000': []
    }

    with open('data3.csv', 'r') as csv_file:
        # Создание объекта для чтения CSV (параметры соответствуют DictWriter)
        csv_reader = get_csv_reader(csv_file, fieldnames)

        line_count = 1
        for row in csv_reader:
            if line_count == 1:
                line_count += 1
                continue
            data_list['dt=50'].append(float(row['dt=50']))
            data_list['dt=150'].append(float(row['dt=150']))
            data_list['dt=700'].append(float(row['dt=700']))
            data_list['dt=2000'].append(float(row['dt=2000']))
            line_count += 1
    line_count = 0


    res_list = {
        'dt=50': [],
        'dt=150': [],
        'dt=700': [],
        'dt=2000': [],
    }
    for i in range(1, len(data_list['dt=50'])//2):
        sum = 0
        for j in range(50, len(data_list['dt=50'])-i):
            if j >= 50 and j <= 6805:
                sum += abs(data_list['dt=50'][j+] - data_list['dt=50'][j])
        res_list['dt=50'].append(sum/(len(data_list['dt=50'])-i))

    for i in range(1, len(data_list['dt=150'])//2):
        sum = 0
        for j in range(150, len(data_list['dt=150'])-i):
            if j >= 150 and j <= 6708:
                sum += abs(data_list['dt=150'][j+i] - data_list['dt=150'][j])
        res_list['dt=150'].append(sum/(len(data_list['dt=150'])-i))

    for i in range(1, len(data_list['dt=700'])//2):
        sum = 0
        for j in range(699, len(data_list['dt=700'])-i):
            if j >= 699 and j <= 6156:
                sum += abs(data_list['dt=700'][j+i] - data_list['dt=700'][j])
        res_list['dt=700'].append(sum/(len(data_list['dt=700'])-i))

    for i in range(1, len(data_list['dt=2000'])//2):
        sum = 0
        for j in range(999, len(data_list['dt=2000'])-i):
            if j >= 999 and j <= 5856:
                sum += abs(data_list['dt=2000'][j+i] - data_list['dt=2000'][j])
        res_list['dt=2000'].append(sum/(len(data_list['dt=2000'])-i))


    res_res_list = [res_list['dt=50'], res_list['dt=150'], res_list['dt=700'], res_list['dt=2000']]

    # Создание CSV-файла
    with open("data4.csv", "w") as csv_file:
        # Получение объекта для работы с CSV
        csv_writer = get_csv_writer(csv_file, fieldnames)

        # Запись заголовков в CSV файл, переданных в поле fieldnames
        csv_writer.writeheader()

        # Запись данных в CSV файл
        i=0
        while i < len(res_res_list[0]):
            row = {'dt=50' : res_res_list[0][i]//0.0000001/10000000, 'dt=150' : 0, 'dt=700' : 0, 'dt=2000' : 0}
            if i < len(res_res_list[1]):
                row['dt=150'] = res_res_list[1][i]//0.0000001/10000000
            if i < len(res_res_list[2]):
                row['dt=700'] = res_res_list[2][i]//0.0000001/10000000
            if i < len(res_res_list[3]):
                row['dt=2000'] = res_res_list[3][i]//0.0000001/10000000
            csv_writer.writerow(row)
            i += 1

if __name__ == "__main__":
    main()