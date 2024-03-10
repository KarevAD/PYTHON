# Вводим кол-во строк/столбцов
h = int(input())
w = int(input())
answer = ""
# Для каждой строки создаём массив чисел 
# Длина которого равна числу столбцов
# И заполняем строками
for i in range(h):
    mass = [input() for _ in range(w)]
    # Если это не первая и не последняя строка,
    # Сортируем
    if i != 0 and i != h - 1:
        mass = sorted(mass)
    # Перебираем слова в массиве и ставим \t или \n, где надо
    for i in range(len(mass)):
        if i != len(mass) - 1:
            answer = answer + mass[i] + '\t'
        else:
            answer = answer + mass[i] + '\n'
print(answer)