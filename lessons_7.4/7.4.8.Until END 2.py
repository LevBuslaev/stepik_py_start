# put your python code here
word = input()
while word != 'КОНЕЦ' and word != 'конец':
    print(word)
    word = input()





'''Ч

тобы понять, какой оператор or или and необходимо использовать в цикле while, нужно правильно сформулировать условие, а именно: "Цикл продолжается пока ...",  а не "Цикл прекратится, когда ...".  Таким образом, логично, что если мы используем оператор or, то цикл продолжится, если будет выполнено хотя бы одно из условий. Даже если оно противоречит другому.

Изначально оба условия True и всё выражение True. А цикл остановится тогда, когда выражение будет False. Если использовать or, то на слове 'конец' или  'КОНЕЦ' лишь одно условие станет False, но выражение останется True, ведь 0 or 1 = 1. А если использовать and, получится как раз то, что и нужно: 1 and 0 = 0

Вот, допустим, while доходит до слова "конец":
"конец" != "конец" (False)    and     "конец" != "КОНЕЦ" (True)   =   False'''


# =========================================================================

'''                        До КОНЦА 2
На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является слово «КОНЕЦ» или «конец» (большими или маленькими буквами, без кавычек). Напишите программу, которая выводит члены данной последовательности.

Формат входных данных
На вход программе подается последовательность слов, каждое слово на отдельной строке.

Формат выходных данных
Программа должна вывести члены данной последовательности.

Тестовые данные 🟢
Sample Input 1:

JavaScript
C++
C#
Ruby
PHP
КОНЕЦ
Python
Sample Output 1:

JavaScript
C++
C#
Ruby
PHP
Sample Input 2:

Великобритания
США
Китай
КОНЕЦ
Ватикан
Sample Output 2:

Великобритания
США
Китай
Sample Input 3:

for
while
конец
for while
Sample Output 3:

for
while'''