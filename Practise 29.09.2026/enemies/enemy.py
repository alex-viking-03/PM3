import random
import time


class Enemy:
    def __init__(self,
                 name,
                 hp,
                 reward,
                 description,
                 damage,
                 chance,
                 get_weak_damage_chance,
                 get_strong_damage_chance):

        self.name = name
        self.hp = hp
        self.reward = reward
        self.description = description
        self.damage = damage
        self.chance = chance
        self.get_weak_damage_chance = get_weak_damage_chance
        self.get_strong_damage_chance = get_strong_damage_chance


    def get_damage(self, damage):
        self.hp -= damage

    def deal_damage(self, hero):
        attack = random.randint(1, 5)
        if attack <= self.chance:
            hero.get_damage(self.damage)
            print()
            print(f"Take {self.damage} damage! {self.name.capitalize()} kicked you! ")
            time.sleep(2)
