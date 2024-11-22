
class Character:
    """Персонаж
    """
   
    def __init__(self,health,weapon,armor):
        self.health = health # Здоровье
        self.weapon = weapon # Оружие
        self.armor = armor # Броня
    
    def clone(self):
        raise NotImplementedError
    

    def special_reception(self):
        """Спец прием
        """
        raise NotImplementedError

    def move(self):
        """Движение
        """
        raise NotImplementedError
