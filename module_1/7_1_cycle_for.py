str_num = input("Введите цело число: ")

try:
    int_num = int(str_num)
except ValueError as val_err:
    print("Ошибка при преобразовании строки в число!")
    print(val_err)
    exit()

for current_num in range(0, int_num + 1):
    print(current_num)
