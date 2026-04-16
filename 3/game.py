
from __future__ import annotations
from enum import Enum

class Health:
    def __init__(self, current_health: int):
        self.current_health = current_health

class Power:
    def __init__(self, current_power: int):
        self.current_power = current_power
    def divide(self, divider: int) -> Power:
        return Power(self.current_power//divider)

class Warrior:
    def __init__(self, health: Health, power: Power, id: int):
        self.health = health
        self.power = power
        self.id = id
    def __str__(self):
        return f"Warrior: {self.health} : {self.id}"
    def hit(self, attack: Power) -> Warrior:
        # меняю текущий экземпляр Health, вместо создания нового, из-за чего будет ошибка логики.
        self.health.current_health = self.health.current_health - attack.current_power
        return Warrior(self.health, self.power, self.id)

# Часть тела для атаки/защиты.
class BodyPartEnum(Enum):
    HEAD = 0
    TORSO = 1
    LEGS = 2

# DTO с информацией о сделанном бойцами выборе во время хода.
class Hod:
    def __init__(self, bodyPartTargetForHit: BodyPartEnum, bodyPartTargetForProtect: BodyPartEnum):
        self.bodyPartTargetForHit = bodyPartTargetForHit
        self.bodyPartTargetForProtect = bodyPartTargetForProtect

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
        print("После хода")
        print(f"Здоровье Воина 1: {w_1.health.current_health}")
        print(f"Здоровье Воина 2: {w_2.health.current_health}")
      assert w_1.health.current_health == 100 , "Атаковали воина 2, а здоровье уменьшилось у 1"
    def calculate_damage(self, h_1: Hod,  h_2: Hod, attacking_w: Warrior, protecting_w: Warrior):
        """
        Получаем бойца после хода, в котором его атакуют.
        Returns:
            Warrior: Боец после атаки по нему.
        """
        is_protected_part_for_hit: bool = h_2.bodyPartTargetForProtect == h_1.bodyPartTargetForHit
        if (is_protected_part_for_hit):
            powerOfHit: int = attacking_w.power.divide(2)
            protecting_w = protecting_w.hit(powerOfHit)
            return protecting_w
        power_of_hit: int = attacking_w.power.current_power
        protecting_w = protecting_w.hit(power_of_hit)
        return protecting_w
    # Проверка на то, что у боцов остались очки жизней для продолжения.
    def is_continue(w_1: Warrior, w_2: Warrior) -> bool:
        return(w_1.health
                ().current_health() > 0
                                and w_2.health
                ().current_health() > 0)

if __name__== "__main__":
    game = Battle()
    game.start_battle()
