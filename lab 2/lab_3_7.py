# 1. Считываем массив из параметров командной строки

import sys

args = sys.argv[1:]

if len(args) == 0:
    print("Ошибка: не переданы параметры командной строки.")
    print("Пример запуска: python lab_3_7.py 1 2 3 4 5")
    sys.exit(1)

array = []
for arg in args:
    array.append(int(arg))

print(f"1. Исходный массив: {array}")
print(f"   Количество элементов: {len(array)}\n")

# 2. Сумма элементов с четными номерами
# Четные номера (2, 4, 6...) = индексы 1, 3, 5... (0-based)

sum_even_positions = 0
for i in range(1, len(array), 2):
    sum_even_positions += array[i]

print(f"2. Сумма элементов с четными номерами: {sum_even_positions}")

# 3. Произведение элементов с нечетными номерами
# Нечетные номера (1, 3, 5...) = индексы 0, 2, 4... (0-based)

product_odd_positions = 1
has_odd_positions = False

for i in range(0, len(array), 2):
    product_odd_positions *= array[i]
    has_odd_positions = True

if has_odd_positions:
    print(f"3. Произведение элементов с нечетными номерами: {product_odd_positions}")
else:
    print("3. Произведение элементов с нечетными номерами: нет элементов")

# 4. Поменять местами минимальный и максимальный элементы

# Находим индексы минимального и максимального элементов
min_index = 0
max_index = 0

for i in range(1, len(array)):
    if array[i] < array[min_index]:
        min_index = i
    if array[i] > array[max_index]:
        max_index = i

# Сохраняем значения ДО замены для корректного вывода
min_value = array[min_index]
max_value = array[max_index]

# Меняем местами значения
array[min_index], array[max_index] = array[max_index], array[min_index]

print(f"4. Массив после замены мин и макс элементов: {array}")
print(f"   Минимальный элемент (был на индексе {min_index}): {min_value}")
print(f"   Максимальный элемент (был на индексе {max_index}): {max_value}")



