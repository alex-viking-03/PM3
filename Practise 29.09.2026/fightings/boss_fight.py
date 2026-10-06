import random
import time

from operations import clear_console
from enemies.enemy import Enemy
class BossFight:
    def __init__(self, hero):
        self.attacks = [
            {"attack": "Attack from the top", "action": "roll", "parry": "r"},
            {"attack": "Fire breath", "action": "shield", "parry": "s"},
            {"attack": "Attack in legs", "action": "jump", "parry": "j"}
        ]
        self.monster = Enemy(
            name = "AZRAGOR",
            hp = 270,
            reward = 0,
            description = "Azragor has burned entire cities and slaughtered every army sent to stop him."
                          "The king offers a fortune for his head, but no hunter has ever returned. "
                          "You are the next to try.",
            damage = 40,
            chance = 5,
            get_weak_damage_chance = 5,
            get_strong_damage_chance = 5
        )
        self.hero = hero
        self.fighting = True
        self.stage = 1

        self.breathing_story()
        self.start_fight()

    def breathing_story(self):
        print('''While walking through the vast, dark halls, you start wondering: why are you here? Why is reaching the end
so important to you?

You had a good life. A warm home, friends who stayed up with you until sunrise, and a mother who 
always complained that you spent too much time at your computer. There were places you wanted to 
visit and things you kept putting off until next summer. You thought you had plenty of time.
Your game was supposed to be the beginning of something great. You had spent months building its 
dark halls, filling them with monsters, and creating Azragor—the final boss. Tonight, you were 
finally going to test the ending.
But when you pressed “Start,” the screen went black. Then something on the other side grabbed 
your wrist.

You woke up on cold stone. You recognised the corridor before you even stood up. You had designed 
it yourself.

There was no keyboard. No exit button. Only a message glowing on the wall:
“Kill Azragor to return home.”

You remembered laughing when you gave him enough strength to kill a player in two hits. It didn't 
seem quite so funny now.

There were only two ways this could end: you would kill your own creation and go home, or die 
somewhere no one would ever think to look.

Now or never…''')
        input("Press enter to continue...")

        clear_console()

        print('''Entering the room, you see this monster. The only thing he knows, he wants to kill you.
He don't know you, but you are already his main enemy.

He stands up and your fight starts. It's only you and him. One of you will stay here, dead, and other will
leave this room. Who will it be?''')

        input("Press enter to continue...")
        clear_console()

    def start_fight(self):
        self.tutorial()
        while self.monster.hp > 0 and self.fighting:
            clear_console()
            print(f"HP: {self.monster.hp}")

            if self.monster.hp > 180:
                self.stage = 1
            elif self.monster.hp > 90:
                self.stage = 2
            elif self.monster.hp > 0:
                self.stage = 3

            incoming_attack = random.choices(self.attacks, k=self.stage)
            print("WARNING! The attack is coming")
            print(" -> ".join(attack["attack"] for attack in incoming_attack))

            correct_order = ""

            for attack in incoming_attack:
                correct_order += attack['parry']

            start = time.monotonic()
            answer = input("Try to parry that: ")
            end = time.monotonic() - start

            if end > 10:
                print(f"What's wrong with you, dumbass? You got {self.monster.damage} HP")
                self.hero.get_damage(self.monster.damage)
                time.sleep(2)

            elif answer != correct_order:
                print(f"What's wrong with you, dumbass? You got {self.monster.damage} HP")
                self.hero.get_damage(self.monster.damage)
                time.sleep(2)

            else:
                hit = random.randint(1, 5)
                if hit <= 3:
                    print(f"You nicely parried this attack and kicked his ass strongly! "
                          f"You dealt {self.monster.name} {self.hero.strong_attack} damage")

                    self.monster.get_damage(self.hero.weak_attack)
                else:
                    print(f"You nicely parried this attack, but didn't hit him well! "
                          f"You dealt {self.monster.name} {self.hero.weak_attack} damage")
                    self.monster.get_damage(self.hero.strong_attack)

            self.fighting = self.check_results()

        clear_console()

        if self.hero.hp <= 0:
            print("""That is the biggest fail in your life. You will rot there forever.

GAME OVER""")
            time.sleep(2)

        else:
            print("""Azragor falls at your feet. The walls dissolve into light, and you
wake up at your desk. On the screen, two words appear: “Game completed.”

You hear your mother calling from downstairs. This time, you don’t make her wait.

DUNGEON CLEARED!""")

    def check_results(self):
        if self.monster.hp <= 0 or self.hero.hp <= 0:
            return False
        return True

    def tutorial(self):
        print('''TUTORIAL
Boss will have several studies. He will attack you. Your goal is to write correct letters in time.
There are attacks and methods to parry them:\n''')
        for attack in self.attacks:
            print(f"Attack: {attack['attack']}\nAction: {attack['action']}\nButton: {attack['parry']}\n")
        print("\nWarning! Make sure your keyboard is in 'English' mode.")

        input("Press any key start...")