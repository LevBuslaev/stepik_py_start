
 Примеры
Пример 1. Требовалось написать программу, которая выводит символ А 10 раз. Вы ревьювите следующий код:

print('A')
print('A')
print('A')
print('A')
print('A')
print('A')
print('A')
print('A')
print('A')
print('A')
Что вы о нем скажете? Правильно ли он работает? Как его улучшить?

Ревью. Приведенный код выполняет поставленную задачу, однако его можно улучшить. Поскольку действия в строках одинаковые, то можно использовать цикл. Поскольку мы знаем количество повторений (итераций), то нам подходит цикл for:

for _ in range(10):
    print('A')
Пример 2. Требовалось написать программу которая должна вывести все числа от 1 до 100 кратные 7. Вы ревьювите следующий код:

i = 1
while i < 101:
    if i % 7 == 0:
        print(i)
        i += 1
Что вы о нем скажете? Правильно ли он работает? Как его улучшить?

Ревью. Приведенный код содержит достаточно распространенную ошибку: неверно поставленный отступ. Поскольку управление циклом while происходит при помощи переменной i, то ее необходимо инкрементировать (увеличивать) каждую итерацию. В приведенном коде она инкрементируется только если выполняется условие i % 7 == 0, которое ложно для начального значения i = 1. Таким образом, получаем бесконечный цикл. Для исправления ошибки необходимо удалить отступ у строки i += 1:

i = 1
while i < 101:
    if i % 7 == 0:
        print(i)
    i += 1
В данном случае лучше использовать цикл for с шагом, равным 7. Это позволит сделать код более наглядным и сократит время выполнения программы, так как нет необходимости просматривать и проверять все числа на делимость на 7:

for i in range(7, 101, 7):
    print(i)
Пример 3. Требовалось написать программу которая выводит все числа от 100 до 1 в порядке убывания. Вы ревьювите следующий код:

for i in range(1, 100):
    print(101 - i)
Что вы о нем скажете? Правильно ли он работает? Как его улучшить?

Ревью. Приведенный код содержит достаточно распространенную ошибку: неправильная правая граница цикла for. Следует помнить, что правая граница в цикле for всегда не включительна. Таким образом, для исправления ошибки необходимо заменить число 100 на 101:

for i in range(1, 101):
    print(101 - i)
В данном случае лучше использовать цикл for с шагом, равным -1:

for i in range(100, 0, -1):
    print(i)
Пример 4. Требовалось написать программу которая находит сумму всех нечетных чисел от 1 до 1000. Вы ревьювите следующий код:

a = 1
for i in range(1, 1000):
    if i % 2 == 1:
        a = a + 1
print(a)
Что вы о нем скажете? Правильно ли он работает? Как его улучшить?

Ревью. Приведенный код содержит достаточно распространенные ошибки:

неправильная начальная инициализация переменной a;
неправильная правая граница цикла for;
неправильно записанная операция накапливания значения суммы.
a = 0
for i in range(1, 1001):
    if i % 2 == 1:
        a = a + i
print(a)
Для улучшения читабельности кода изменим название переменной a на total и используем расширенный оператор присваивания:

total = 0
for i in range(1, 1001, 2):
    total += i
print(total)
Пример 5. Требовалось написать программу которая вычисляет факториал числа. Вы ревьювите следующий код:

n = input()
a = 0
for i in range(n):
    a = a * i
print(a)
Что вы о нем скажете? Правильно ли он работает? Как его улучшить?

Ревью. Приведенный код содержит достаточно распространенные ошибки:

отсутствие преобразования строки текста в целое число;
неправильная начальная инициализация переменной a;
неправильная работа с границами итерирования: переменная i принимает значения от 0 до n - 1.
n = int(input())
a = 1
for i in range(1, n + 1):
    a = a * i
print(a)
Для улучшения читабельности кода, изменим название переменной a на factorial и используем расширенный оператор присваивания:

n = int(input())
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)
В модуле math есть функция factorial(), которая вычисляет факториал числа. Поэтому вместо реализации своей версии, куда правильнее и удобнее воспользоваться уже готовой.

