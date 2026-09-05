str_1 = 'результат операции: 42'
str_2 = 'результат операции: 514'
str_3 = 'результат работы программы: 9'

a = int(str_1[str_1.index(':') + 2:])
b = int(str_2[str_2.index(':') + 2:])
c = int(str_3[str_3.index(':') + 2:])

print(a + 10)
print(b + 10)
print(c + 10)