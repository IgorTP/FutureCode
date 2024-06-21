str_num = input("Введите цело число: ")

try:
    int_num = int(str_num)
except ValueError as val_err:
    print("Ошибка при преобразовании строки в число!")
    print(val_err)
    exit()


counter = 0
while counter <= int_num:
    print(counter)
    counter += 1
