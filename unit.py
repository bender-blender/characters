
from interface import Character
import copy


class Warrior(Character):
    """
    Воин
    """

    def __init__(self, health:int, weapon:int, armor:int):
        self.health = health
        self.weapon = weapon
        self.armor = armor
    
    def __str__(self) -> str:
        return f"Воин\nЗдоровье:{self.health}\nОружие:{self.weapon}\nБроня:{self.armor}"

    def clone(self):
        print("Призыв воина!")
        return copy.deepcopy(self)

    def move(self):
        """Движение
        """
        return f"Воин движется в {self.armor}"

    def special_reception(self):
        """Спец прием
        """
        for i in range(5):
            print(f"Размах {self.weapon}а! ")


class Mage(Character):
    """Маг
    """

    def __init__(self, health:int, weapon:str, armor:str):
        
        self.health = health
        self.armor = armor
        self.weapon = weapon
    
    def __str__(self) -> str:
        return f"Маг\nЗдоровье:{self.health}\nОружие:{self.weapon}\nБроня:{self.armor}"


    def clone(self):
        print("Вызов Мага!")
        return copy.deepcopy(self)

    def move(self):
        return f"Маг движется на {self.armor}"

    def special_reception(self, unit: Character):
        """Спец прием
        """

        while unit.health <= 100:
            unit.health += 1
        print("Восстановление!")
