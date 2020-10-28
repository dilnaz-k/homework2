print('Введите глубину ёлки:')
stars = int(input())
star = 1
while star < stars+1:
    print(star * '*')
    star = star + 1
for star in range(3):
  print('*''*')

Numbers = [1 , 2 , 3 , 4 , 5, 6 , 7 , 8, 9 , 10 , 11 , 12, 13 , 14 , 15]

print('Меню:')
print('1. Вывести на экран все знаения')
print('2. Добавить значение')
print('3. Удалить значение')
print('4. Найти значение')
print('5. Отсортировать значения')
print('Введите опцию:')


# Задание 2: в цикле while создать ограничения для ввода опций таким образом, чтобы
# программа принимала только значения, из меню (1-6), в остальных случаях выдвала ошибку.

# Задание 3: Реализовать опцию 1 и 2 из списка меню.
while userChoice == 6:
        userChoice = int(input())
        if userChoice == 1:
            print(Numbers)
        elif userChoice == 2:
            print('Введите значение')
            NewValue = int(input())
            Numbers.append(NewValue)
            print(Numbers)
        elif userChoice == 3:
            print
        elif userChoice == 4:
            print
        elif userChoice == 5:
            print
        else:
            print('Ошибка. Выберите существующую опцию')

        print('Меню:')
        print('1. Вывести на экран все значения')
        print('2. Добавить значение')
        print('3. Удалить значение')
        print('4. Найти значение')
        print('5. Отсортировать значения')
        print('Введите опцию:')
