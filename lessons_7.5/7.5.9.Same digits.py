n = int(input())
count = 1
while n != 0:
    n_pred = n % 10
    n_posl = n // 10
    if n_pred == n_posl:
        count += 1
    else:
        print('NO')

# ================================================
'''7.5 Цикл while: обработка цифр числа
8 из 10 шагов пройдено
27 из 42 баллов  получено
                                            Одинаковые цифры
Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести «YES» если число состоит из одинаковых цифр и «NO» в противном случае.

Тестовые данные 🟢
Sample Input 1:

11111
Sample Output 1:

YES
Sample Input 2:

11112111
Sample Output 2:

NO'''