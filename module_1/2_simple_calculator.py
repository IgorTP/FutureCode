print("Привет! Это простой калькулятор.")

main_allowed_operation = ("-", "+")
print(f"Доступные операции: {main_allowed_operation}")

while True:
    operation = input("Выберите операцию ('q' => выйти): ")

    if operation == "q":
        exit()

    if operation not in main_allowed_operation:
        print(f"{operation} -> недоступная операция")
        continue

    try:
        num_1 = float(input("Введите 1 число: "))
        num_2 = float(input("Введите 2 число: "))
    except Exception as e:
        print(f"Невозможно преобразовать в число! \n {e}")
        continue

    if operation == "+":
        num_res = num_1 + num_2
    elif operation == "-":
        num_res = num_1 - num_2

    print(f"Рузультат: {num_res}")
