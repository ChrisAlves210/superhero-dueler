import random

from ability import Ability


class Weapon(Ability):
    def attack(self):
        """Return a random value between one half and the full attack power.

        The range is [max_damage // 2, max_damage].
        """
        half_damage = self.max_damage // 2
        return random.randint(half_damage, self.max_damage)


if __name__ == "__main__":
    weapon = Weapon("Test Weapon", 57)
    print(weapon.name)
    print(weapon.attack())
