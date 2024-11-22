from unit import (
    Warrior,
    Mage
)



def client_code():
    warrior = Warrior(100,"Меч","Доспехи")
    mage = Mage(100,"Посох","Ковер")
    print(warrior)
    
    warrior.move()
    warrior.special_reception()
    print("\n")
    print(mage)
    mage.move()
    mage.special_reception(warrior)
    print("\n")
    new_warrior = warrior.clone()
    
    new_warrior.health = 80
    print(new_warrior)
    new_warrior.move()
    new_warrior.special_reception()
    print("\n")
    new_mage = mage.clone()
    print(new_mage)
    new_mage.move()
    new_mage.special_reception(new_warrior)

client_code()