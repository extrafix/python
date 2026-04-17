
from __future__ import annotations
from enum import Enum

class Health:
    def __init__(self, current_health: int):
        self.__current_health = current_health
    
    def get_current_health(self):
        """
        Получить текущее численное значение очков здоровья.
        """
        return self.__current_health

class Power:
    def __init__(self, current_power: int):
        self.__current_power = current_power

    def get_current_power(self):
        """
        Получить текущее численное значение очков силы.
        """
        return self.__current_power

    def divide(self, divider: int) -> Power:
        return Power(self.__current_power//divider)

class Warrior:
    def __init__(self, health: Health, power: Power, id: int):
        self.__health = health
        self.__power = power
        self.__id = id
    
    def get_health(self):
        """
        Получить текущее значение здоровья.
        """
        return self.__health

    def get_power(self):
        """
        Получить текущее значение силы.
        """
        return self.__power

    def __str__(self):
        return f"Warrior: {self.__health} : {self.__id}"

    def hit(self, attack: Power) -> Warrior:
        # меняю текущий экземпляр Health, вместо создания нового, из-за чего будет ошибка логики.
        health_after_attack_int: int = self.__health.get_current_health() - attack.get_current_power()
        health_after_attack: Health = Health(health_after_attack_int)
        return Warrior(health_after_attack, self.__power, self.__id)

# Часть тела для атаки/защиты.
class BodyPartEnum(Enum):
    HEAD = 0
    TORSO = 1
    LEGS = 2

# DTO с информацией о сделанном бойцами выборе во время хода.
class Hod:
    def __init__(self, bodyPartTargetForHit: BodyPartEnum, bodyPartTargetForProtect: BodyPartEnum):
        self.__bodyPartTargetForHit = bodyPartTargetForHit
        self.__bodyPartTargetForProtect = bodyPartTargetForProtect

    def get_bodyPartTargetForHit(self):
        """
        Получить выбранную часть для удара.
        """
        return self.__bodyPartTargetForHit

    def get_bodyPartTargetForProtect (self):
        """
        Получить выбранную часть для защиты.
        """
        return self.__bodyPartTargetForProtect

    @staticmethod
    def make_hod() -> Hod:
        """
        Выполнение хода игроком.
        """
        print("Воин, выбери часть тела противника для Атаки (HEAD, TORSO или LEGS)")
        userSelectedPartTargetForHit2: str = input("Введите Атаку: ").upper()
        bodyPartTargetForHit2: BodyPartEnum = BodyPartEnum[userSelectedPartTargetForHit2]
        print("Воин, выбери часть своего тела для Защиты (HEAD, TORSO или LEGS)")
        userSelectedPartTargetForProtect2: str = input("Введите Защиту: ").upper()
        bodyPartTargetForProtect2: BodyPartEnum = BodyPartEnum[userSelectedPartTargetForProtect2]
        return Hod(bodyPartTargetForHit2, bodyPartTargetForProtect2)


    @staticmethod
    def try_make_hod() -> Hod:
        """
        Выполнение хода игроком с обработкой ошибки неверного аргумента.
        """
        try:
            return Hod.make_hod()
        except ValueError as exception:
            print("Введена неверная часть тела. Допустимые значения: HEAD, TORSO или LEGS.")
            print(f"Было введено: {exception}")
            print("Попробуйте выбрать часть тела еще раз.")
            return Hod.try_make_hod()



class Battle:
    def start_battle(self) -> None:
        """
        Реализация логики битвы с NPC.
        """
        print("Начало битвы")
        defaultHealth: Health = Health(100)
        defaultPower: Power = Power(30)
        w_1: Warrior = Warrior(defaultHealth, defaultPower, 1)
        w_2: Warrior = Warrior(defaultHealth, defaultPower, 2)
        print(f"Идентификатор воина 1: {w_1.id}")
        print(f"Идентификатор воина 2: {w_2.id}")
        hod_1: Hod = Hod.try_make_hod()
        hod_2: Hod = Hod.try_make_hod()
        w_2 = self.calculate_damage(hod_1, hod_2, w_1, w_2)
        assert w_1.get_health().get_current_health() == 100 , "Атаковали воина 2, а здоровье уменьшилось у 1"

    def calculate_damage(self, h_1: Hod,  h_2: Hod, attacking_w: Warrior, protecting_w: Warrior):
        """
        Получаем бойца после хода, в котором его атакуют.
        Returns:
            Warrior: Боец после атаки по нему.
        """
        is_protected_part_for_hit: bool = h_2.get_bodyPartTargetForProtect() == h_1.get_bodyPartTargetForHit()
        if (is_protected_part_for_hit):
            powerOfHit: int = attacking_w.get_power().divide(2)
            protecting_w = protecting_w.hit(powerOfHit)
            return protecting_w
        power_of_hit: int = attacking_w.get_power().get_current_power()
        protecting_w = protecting_w.hit(power_of_hit)
        return protecting_w
    # Проверка на то, что у боцов остались очки жизней для продолжения.
    def is_continue(w_1: Warrior, w_2: Warrior) -> bool:
        return(w_1.get_health().get_current_health() > 0
                                and w_2.get_health().get_current_health() > 0)


class Equipment:

    def __init__(self, weight: int, damage: int):
        self.__weight = weight
        self.__damage = damage


class Bow(Equipment):

    def __init__(self, weight: int, damage: int, shot_range: int):
        super.__init__(weight, damage)
        self.__shot_range = shot_range


    def shot(self, hod: Hod, w_1: Warrior, w_2: Warrior):
        print("Выстрел из лука в {hod.get_bodyPartTargetForHit}. Будет учтено расстояние между соперниками.")

class Knife(Equipment):

    def __init__(self, weight: int, damage: int, sharpness: int):
        super.__init__(weight, damage)
        self.__sharpness = sharpness


    def attack(self, hod: Hod, w_1: Warrior, w_2: Warrior):
        print("Ближняя атака в {hod.get_bodyPartTargetForHit}.")
        print("Сработает только при нахождении соверников в <1 метра друг от друга. Урон умножается на остроту ножа.")


# Можно было сделать, конечно, и через has-a, поэтому такой рефакторинг часто и выполняется.
class Civil(Warrior):

    def fatality(self):
        print ("Приезжают из Спортлото по жалобе и забирают противника.")

    def battle_cry(self):
        print ("Я напишу в Спортлото")

    def write_letter(self, text):
        print (f"Отправляю письмо: {text}")



class Leopold(Warrior):

    def fatality(self):
        self.tail_swish()
        print("Враг падает")

    def battle_cry(self):
        print("Ребята, давайте жить дружно")

    def tail_swish(self):
        print("Элегантный взмах хвостом")

if __name__== "__main__":
    game = Battle()
    game.start_battle()
