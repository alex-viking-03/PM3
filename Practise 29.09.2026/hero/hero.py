import time
import random

class MainHero:
    def __init__(self, hp, gold, potions):
        self.hp = hp
        self.gold = gold
        self.potions = potions
        self.weak_attack = 10
        self.strong_attack = 20

    def do_action(self, enemy):
        actions = ["1. Weak attack (10 damage)",
                   "2. Strong attack (20 damage)",
                   "3. Use potion (+30 HP)",
                   "4. See characteristics (see your statistics and skip your order)",
                   "5. Give up"]
        print()

        for i in actions:
            print(i)
        print()
        try:
            users_action = int(input("Choose an action: "))
        except:
            print("Invalid input. You lost your order")
            return False

        match users_action:
            case 1:
                self.deal_damage(self.weak_attack, enemy)
                return False
            case 2:
                self.deal_damage(self.strong_attack, enemy)
                return False
            case 3:
                self.use_potion()
                return False
            case 4:
                self.heros_characteristics()
                return False
            case 5:
                return True
            case _:
                return None

    def deal_damage(self, damage, enemy):
        if (damage == self.weak_attack
                and random.randint(1, 5) <= enemy.get_weak_damage_chance):
            print(f"Great! You deal {damage} damage to {enemy.name.capitalize()}!")
            enemy.get_damage(damage)

        elif (damage == self.strong_attack
                and random.randint(1, 5) <= enemy.get_strong_damage_chance):
            print(f"Great! You deal {damage} damage to {enemy.name.capitalize()}!")
            enemy.get_damage(damage)

        else:
            print("Oops! It blocked you!")

        time.sleep(2)

    def get_damage(self, damage):
        self.hp -= damage
        return self.hp

    def use_potion(self):
        if self.potions <= 0:
            print("You realised, that you don't have potions. You did nothing this order")
            time.sleep(2)
        else:
            self.hp += 30
            self.potions -= 1
            if self.hp > 100:
                self.hp = 100
            print(f"You used potion! Your have {self.potions} potions left and {self.hp} HP")
            time.sleep(2)

    def heros_characteristics(self):
        print()
        print(f"HP: {self.hp}\n"
              f"Gold: {self.gold}\n"
              f"Potions: {self.potions}")
        print()
        input("Press any button to continue...")

    def shop(self):
        while True:
            print(f"\nGold: {self.gold}")
            print("1. Buy potion — 20 gold")
            print("2. Upgrade weapon (+5 to both attacks) — 50 gold")
            print("3. Leave")

            choice = input("Choose: ").strip()

            if choice == "1":
                if self.gold < 20:
                    print("Not enough gold!")
                    continue

                self.gold -= 20
                self.potions += 1
                print(f"Potion purchased! Potions: {self.potions}")

            elif choice == "2":
                if self.gold < 50:
                    print("Not enough gold!")
                    continue

                self.gold -= 50
                self.weak_attack += 5
                self.strong_attack += 5
                print(
                    f"Weapon upgraded! "
                    f"Weak attack: {self.weak_attack}, "
                    f"strong attack: {self.strong_attack}"
                )

            elif choice == "3":
                break

            else:
                print("Invalid choice!")