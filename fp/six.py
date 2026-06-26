"""
Задача:
На вход подается 
source_numbers: список исходных чисел для запоминания
selected_numbers: список введенных чисел

На выходе получаем 
check_result: список из объектов, позиция каждого элемента соответствует позиции в source_numbers.
Число элементов совпадает с source_numbers.
[{color: red}, {color: green}, {color: orange}, {color: green}]

Итог:
* На языке лямд и монад автоматически работает добавление элементов в новый список

* Фактически над списком введенных элементов я выполню map в которой для каждого элемента буду вызывать карированную функцию содержащую исходный список.

* Исходный список при этом не меняется, значит лямда законно работает с final аргументом.

* Так как позиция элемента хранится в отдельном поле, можно выполнять проверки параллельно для разных элементов.

Таким образом я инкапсулирую формирование нового списка с добавлением в него подходящих элементов, но сама проверка кодируется достаточно явно.
"""
from pymonad.tools import curry
from pymonad.maybe import Maybe, Just, Nothing
from pymonad.list import ListMonad

class NumberItem:

    def __init__(self, value: int, position: int):
        self.value = value
        self.position = position

    def __str__(self):
        return f"{self.value, self.position}"

class CheckedNumberItem:

    def __init__(self, value: int, position: int, color: str):
        self.value = value
        self.position = position
        self.color = color

    def __repr__(self):
        return f"{self.value, self.position, self.color}"

@curry(2)
def check_green_orange_red(sources, selected_item: NumberItem):
    for source in sources:
        if (source.value == selected_item.value):
            if (source.position == selected_item.position):
                return CheckedNumberItem(selected_item.value, selected_item.position, "green")
            else:
                return CheckedNumberItem(selected_item.value, selected_item.position, "orange")
    return CheckedNumberItem(selected_item.value, selected_item.position, "red")





source_numbers = [NumberItem(10, 1), NumberItem(22, 2), NumberItem(33, 3), NumberItem(44, 4)]

selected_numbers = [NumberItem(11, 1), NumberItem(44, 2), NumberItem(33, 3), NumberItem(55, 4)]

check_with_sources = check_green_orange_red(source_numbers)

print("source_numbers")
for source in source_numbers:
    print(source)
print("")

print("selected_numbers")
for selected in selected_numbers:
    print(selected)
print("")

checkedNumbers = ListMonad(*source_numbers).map(check_with_sources)

print("")
print("checkedNumbers")
print(checkedNumbers)

"""
OUT:
source_numbers
(10, 1)
(22, 2)
(33, 3)
(44, 4)

selected_numbers
(11, 1)
(44, 2)
(33, 3)
(55, 4)


checkedNumbers
[(10, 1, 'green'), (22, 2, 'green'), (33, 3, 'green'), (44, 4, 'green')]


Анализ

Решение:
Мне требуется сверять совпадает ли пара чисел в списке, тогда возвращается green
если поданное из введенных чисел есть в последовательности, но на другой позиции, тогда возвращать orange (числа НЕ повторяются в последовательности)

Исходное состояние - пустой список чисел (еще ничего не введено и фон подсвечивается white
После проверки
Заполненный список чисел и каждому числу соответствует один цвет

Или даже лучше все что вижу на экране описать монадой? 
Тогда монада будет содержать 2 списка. 

1 исходный
2 введенный

Третий результирующий, где содержится порядковый номер элемента, его цвет и значение (введенное число)

Сложность в том, что каждое из проверяемых чисел я буду сравнивать со всем списком.
Если нашел элемент у которого 
совпадает значение
= ставлю промежуточное значение orange и иду до конца списка
= если нашел у которого совпадает значение И позиция
выхожу из проверки
= дефолтное значение в исходящем списке red

Мне нужны функции предикаты, применяя которые буду получать новое значение

Причем предикат может быть каррированной функцией, первым аргументов в которую я 1 раз передам исходную последовательность и сохраню как новую функцию,
которой уже каждый раз буду передавать по 1 аргументу - текущий рассматриваемый элемент из введенных данных.

"""
