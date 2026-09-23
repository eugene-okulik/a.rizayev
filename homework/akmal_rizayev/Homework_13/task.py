import datetime
import os

current_path = os.path.dirname(__file__)

reading_file = os.path.join(current_path, '..', '..', 'eugene_okulik', 'hw_13', 'data.txt')

print(reading_file)


def string_to_date(string, from_sym, to_sym):
    raw_date = string[from_sym:to_sym]
    parsed_date = datetime.datetime.strptime(raw_date, '%Y-%m-%d %H:%M:%S.%f')
    return parsed_date


with open(reading_file, 'r', encoding="utf-8") as file_data:
    first_date = string_to_date(file_data.readline(), 3, 29)
    second_date = string_to_date(file_data.readline(), 3, 29)
    third_date = string_to_date(file_data.readline(), 3, 29)
    print(first_date + datetime.timedelta(weeks=1))
    print(datetime.datetime.strftime(second_date, '%A'))
    print((datetime.datetime.now() - third_date).days)
