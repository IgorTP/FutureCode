rand_list = [5, "Привет", True, 6.95, "10", 0, False, "Helow, world!", None, float("inf")]

print(rand_list, "\n")

print(f"Первые 5 элементов списка: {rand_list[:5]}")
print(f"Последние 3 элемента списка: {rand_list[-3:]}")

print(f"Каждый 2-ой элемент списка: {rand_list[slice(0, len(rand_list), 2)]}\n")

# Изменяем 3-ий элемент списка (по индексу 2-ой)
rand_list[2] = float("nan")

print(f"Изменённый список: {rand_list}")
