n = int(input())
n1 = n
count = 1
while n != 0:
    count += 1
    n //= 10
print((n1 // (10 ** (count - 3))) % 10)

#===============================================
7.5 Цикл while: обработка цифр числа
8 из 10 шагов пройдено
27 из 42 баллов  получено
Вторая цифра
Дано натуральное число n \, (n > 9)n(n>9). Напишите программу, которая определяет его вторую (с начала) цифру.

Формат входных данных
На вход программе подается одно натуральное число, состоящее как минимум из двух цифр.

Формат выходных данных
Программа должна вывести его вторую (с начала) цифру.

Тестовые данные 🟢
Sample Input 1:

455672
Sample Output 1:

5
Sample Input 2:

59
Sample Output 2:

9
Sample Input 3:

123
Sample Output 3:

2
Напишите программу. Тестируется через stdin → stdout
Верно решили 80 867 учащихся
Из всех попыток 65% верных
 Прекрасный ответ.
Теперь вам доступен Форум решений , где вы можете сравнить свое решение с другими или спросить совета.
n = int(input())
n1 = n
count = 1
while n != 0:
    count += 1
    n //= 10
print((n1 // (10 ** (count - 3))) % 10)
1
# put your python code here
2
n = int(input())
3
n1 = n
4
count = 1
5
while n != 0:
6
    count += 1
7
    n //= 10
8
print((n1 // (10 ** (count - 3))) % 10)
9
​
10
​
11
​
12
​
Test input:
123
Test output:
2