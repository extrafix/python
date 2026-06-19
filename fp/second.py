from pymonad.tools import curry

@curry(2)
def concate(x, y): 
    return x + y

helloToName = concate("Hello, ")
print(helloToName("World!"))

# Тривиальный вариант с порядком в кортеже
@curry(4)
def concate(hello_word, comma, end, name): 
    return hello_word + comma + " " + name + end

final = concate("Hello")(",")("!")
print(final("Petya"))

class Comma:
    # Конструктор
    def __init__(self, value: str):
        self.value = value   # Атрибут экземпляра

    def __str__(self):
        return f"{self.value}"

# Перспективным был бы вариант с каррингом по типам, что бы не завязываться на порядок, 
# но он не сработает 
@curry(4)
def concateTyped(hello_word: str, comma: Comma, name: Name, end: EndSymbol): 
    return f"{hello_word}{comma}" "{name}{end}"
