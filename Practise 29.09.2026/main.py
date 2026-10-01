import time
import random

from enemies.enemy import Enemy
from hero.hero import MainHero
from fightings.enemy_fight import Fighting
from fightings.boss_fight import BossFight
from operations import clear_console

def prepare_game():
    monsters_list = [
        {"enemy": lambda: Enemy(
            name = "Slime",
            hp = 30,
            reward = 30,
            description = "Slime is weak, but fast enemy. He's chance to hit you 4/5,"
                          "but your chance to hit him weakly 3/5, strongly 1/5",
            damage = 5,
            chance = 4,
            get_weak_damage_chance = 3,
            get_strong_damage_chance = 1,
        ),
         "amount": 1},
        {"enemy": lambda: Enemy(
            name = "Goblin",
            hp = 50,
            reward = 50,
            description = "Goblin is medium enemy. His attacks are stronger, then slime's,"
                          "but his chance to hit you 3/5. Your chance to hit him weakly 4/5, strongly 2/5",
            damage = 10,
            chance = 3,
            get_weak_damage_chance = 4,
            get_strong_damage_chance = 2
        ),
          "amount": 1},
         {"enemy": lambda: Enemy(
             name = "Knight",
             hp = 80,
             reward = 80,
             description = "Dark khight is one of the Boss's defenders. His attacks are  strong,"
                           "but slow. His chance to hit you 2/5. Your chances are: weak hit - 5/5,"
                           "strong hit 3/5",
             damage = 30,
             chance = 2,
             get_weak_damage_chance = 5,
             get_strong_damage_chance = 3
         ),
          "amount": 1}
        ]

    for monster_info in monsters_list:
        monster_info["amount"] += random.randint(1, 4)
    return monsters_list

def count_monsters(monsters_dict):
    counter = 0
    for monster_info in monsters_dict:
        counter += monster_info["amount"]
    return counter

if __name__ == "__main__":
    operation = int(input('''
DUNGEON TERMINAL
Try not to die!

1. Start
2. Exit

Enter your choice: '''))

    GAME_OVER = False
    monsters = prepare_game()
    hero = MainHero(
        hp=100,
        gold=50,
        potions=2
    )

    prepare_game()

    if operation == 2:
        print("There is no room here for cowards!")
        GAME_OVER = True

    time.sleep(2)
    if not GAME_OVER:
        print("Welcome to Dungeon! Good luck, brave knight")
        time.sleep(1)
        print("\n"*4)

    while not GAME_OVER:
        clear_console()
        if random.randint(1, 4) == 1:
            print("\nYou found a shop!")
            hero.shop()
        else:
            if len(monsters) == 0:
                boss_fight = BossFight(hero)
                break

            monster = random.choice(monsters)
            if monster["amount"] <= 0:
                monsters.remove(monster)
                continue

            monster_object = monster['enemy']()
            fighting = Fighting(monster_object, hero)
            winning = fighting.start_fighting()

            if not winning:
                print("\n"*1)
                print("You lost! The fighting is over! Rest in piece!")
                GAME_OVER = True
                break

            print("Enemy down. There is your reward!")
            monsters[monsters.index(monster)]["amount"] -= 1
            time.sleep(1)
            print(f"+{monster_object.reward} gold!")
            hero.gold += monster_object.reward
            time.sleep(1)
            print("Let's go further")
            time.sleep(2)
            print()