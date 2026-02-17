import random

from hero import Hero


class Team:
    def __init__(self, name):
        '''Initialize your team with its team name and an empty list of heroes'''
        self.name = name
        self.heroes = list()

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        # Expecting a Hero instance; append it to the list
        self.heroes.append(hero)

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        foundHero = False
        # loop through each hero in our list
        for hero in list(self.heroes):
            # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                # set our indicator to True
                foundHero = True
        # if we looped through our list and did not find our hero,
        # the indicator would have never changed, so return 0
        if not foundHero:
            return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        for hero in self.heroes:
            print(hero.name)

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths if hero.deaths != 0 else hero.kills
            print(f"{hero.name} Kill/Deaths:{kd}")

    def revive_heroes(self, health=100):
        '''Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        '''Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            # 1) Randomly select a living hero from each team
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            # 2) Have the heroes fight each other
            hero.fight(opponent)

            # 3) Update living lists based on who is still alive
            if not hero.is_alive() and hero in living_heroes:
                living_heroes.remove(hero)
            if not opponent.is_alive() and opponent in living_opponents:
                living_opponents.remove(opponent)


if __name__ == "__main__":
    # Simple manual test of Team behavior
    team = Team("Testers")
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    team.add_hero(hero1)
    team.add_hero(hero2)
    team.view_all_heroes()
    team.remove_hero("Wonder Woman")
    team.view_all_heroes()
