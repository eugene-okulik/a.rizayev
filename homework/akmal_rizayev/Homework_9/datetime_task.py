import datetime

input_str = "Jan 15, 2023 - 12:05:33"
python_f_date = datetime.datetime.strptime(input_str, '%b %d, %Y - %H:%M:%S')
print(python_f_date.strftime('%B'))
print(python_f_date.strftime('%d.%m.%Y, %H:%M'))
