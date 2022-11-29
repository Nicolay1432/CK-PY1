list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

maximum = list_numbers[0]  # Пусть значение в переменной будет самой большой
for i, value in enumerate(list_numbers):  # Перебираем пары индекс -значения
    if value >= maximum:  # Сравниваем текущее значение с более ранним
        maximum = value
        print(i, value) # последня строка и будет последним максимальным индексом/элементом

print("последнее максимальное значение", maximum)

list_numbers[9], list_numbers[-1] = list_numbers[9], list_numbers[-1]
print(list_numbers)
print("Меняем местами элементы по индексу")
list_numbers[9], list_numbers[-1] = list_numbers[-1], list_numbers[9]
print(list_numbers)
# GitHub