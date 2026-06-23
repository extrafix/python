# Прошлый пример https://github.com/extrafix/python/blob/main/fp/third.py (не уверен, что отправился)

from pymonad.tools import curry
from pymonad.maybe import Maybe, Just, Nothing
from pymonad.list import ListMonad

@curry(2)
def add(x, y):
    return x + y

add10 = add(10)

print(Just(7).then(add10))
print(Nothing.then(add10))

print(ListMonad(1,2,3,4).map(add10))

#out:
# Just 17
# Nothing
# [11, 12, 13, 14]


# Сначала передавал в функцию значение Just(10) 
# Из-за чего падало с ошибкой сложенияя int и Maybe,
# Потом разобрался что then и map передают в функцию уже Расспакованное значение.

    
