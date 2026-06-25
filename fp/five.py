from pymonad.tools import curry
from pymonad.maybe import Maybe, Just, Nothing
from pymonad.list import ListMonad

@curry(2)
def to_left_curry(num, left_right_amount):
    left_amount, right_amount = left_right_amount
    if abs((left_amount + num) - right_amount) > 4:
        return Nothing
    else:
        return Just((left_amount + num, right_amount))

@curry(2)
def to_right_curry(num, left_right_amount):
    left_amount, right_amount = left_right_amount
    if abs((right_amount + num) - left_amount) > 4:
        return Nothing
    else:
        return Just((left_amount, right_amount + num))

# банановая кожура
banana = lambda x: Nothing

# отображение результата
def show(maybe):
    if maybe == Nothing:
        print("Loose.")
    else:
        print("Win!")

# начальное состояние
begin = lambda: Just( (0,0) )

show(
    begin()
    .bind(to_left_curry(2))
    .bind(to_right_curry(5))
    .bind(to_left_curry(-2)) # канатоходец упадёт тут
)
show(
    begin()
    .bind(to_left_curry(2))
    .bind(to_right_curry(5))
    .bind(to_left_curry(-1))
) # в данном случае всё ок
show(
    begin()
    .bind(to_left_curry(2))
    .bind(banana) # кожура всё испортит
    .bind(to_right_curry(5))
    .bind(to_left_curry(-1))
)

# Сначала было сложно понять как запрограммировать
# Резкий взлет сложности по сравнению с крайним заданием, 
# Но когда понял, что надо только синтаксис изменить - разобрался.
# Непонятным был механизм передачи распакованного значения списка из двух элементов, 
# В моей версии python пришлось писать явную распаковку left_amount, right_amount = left_right_amount
