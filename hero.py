from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
            deaths: Integer
            kills: Integer
        '''
        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
        # statistics
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        '''Add ability to abilities list'''
        # We use the append method to add ability objects to our list.
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
           return: total_damage:Int
        '''
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors
           Armor: Armor Object
        '''
        self.armors.append(armor)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # Weapons behave like abilities, so we store them together
        self.abilities.append(weapon)

    def defend(self):
        '''Calculate the total block amount from all armor blocks.
           return: total_block:Int
        '''
        # If hero is dead, they can't defend
        if self.current_health <= 0:
            return 0
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        defense = self.defend()
        net_damage = damage - defense
        # Simple guard: ignore healing from over-block
        if net_damage < 0:
            net_damage = 0
        self.current_health -= net_damage

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        return self.current_health > 0

    def add_kill(self, num_kills):
        '''Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        '''Update deaths with num_deaths'''
        self.deaths += num_deaths

    def fight(self, opponent):
        '''Current Hero will take turns fighting the opponent hero passed in.
        '''
        # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")
            return

        # 1) start the fighting loop until a hero has won
        while self.is_alive() and opponent.is_alive():
            # 2) each hero attacks and the other takes damage
            opponent.take_damage(self.attack())
            self.take_damage(opponent.attack())

            # 3) After each round, check both heroes' status
            if not self.is_alive() and not opponent.is_alive():
                # both heroes died -> each gets a kill and a death
                self.add_kill(1)
                opponent.add_kill(1)
                self.add_death(1)
                opponent.add_death(1)
                print("Draw")
                return
            elif not opponent.is_alive():
                # self wins
                self.add_kill(1)
                opponent.add_death(1)
                print(f"{self.name} won!")
                return
            elif not self.is_alive():
                # opponent wins
                opponent.add_kill(1)
                self.add_death(1)
                print(f"{opponent.name} won!")
                return


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
