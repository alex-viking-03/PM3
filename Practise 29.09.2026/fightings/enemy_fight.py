from operations import clear_console


class Fighting:
    def __init__(self, monster, hero):
        self.monster = monster
        self.hero = hero
        self.fighting = True

    def start_fighting(self):
        while self.fighting:
            clear_console()
            self.information_about_enemy()
            action = self.hero.do_action(self.monster)

            if action:
                self.exit_fighting()
                break
            self.check_results_of_fighting()
            try:
                if self.result or not self.result:
                    break
            except:
                pass
            self.monster.deal_damage(self.hero)
            self.check_results_of_fighting()


        return self.result

    def information_about_enemy(self):
        print(f"BOOM! {self.monster.name} is on your way. He's going to kill you!")
        print("Description: ", self.monster.description)
        print()
        print(f"Enemy: {self.monster.name}\n"
              f"HP: {self.monster.hp}\n"
              f"You will get {self.monster.reward} gold for it's head")

    def exit_fighting(self):
        print()
        print("You seemed stronger")
        self.fighting = False
        self.result = False

    def check_results_of_fighting(self):
        if self.monster.hp <= 0:
            self.fighting = False
            self.result = True

        elif self.hero.hp <= 0:
            self.fighting = False
            self.result = False