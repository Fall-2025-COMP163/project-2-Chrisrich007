class Character:
    def __init__(self, name: str, health: int, strength: int):
        self.name = name
        self.health = health
        self.strength = strength

    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")


class Player(Character):
    def __init__(self, name: str, health: int, strength: int, character_class: str, level: int = 1):
        super().__init__(name, health, strength)
        self.character_class = character_class
        self.level = level

    def display_stats(self):
        super().display_stats()
        print(f"Class: {self.character_class}")
        print(f"Level: {self.level}")


class Warrior(Player):
    def __init__(self, name: str, level: int = 1):
        super().__init__(name, 150, 20, "Warrior", level)
        self.defense = 30

    def display_stats(self):
        super().display_stats()
        print(f"Defense: {self.defense}")


class Mage(Player):
    def __init__(self, name: str, level: int = 1):
        super().__init__(name, 100, 10, "Mage", level)
        self.mana = 200

    def display_stats(self):
        super().display_stats()
        print(f"Mana: {self.mana}")


class Rogue(Player):
    def __init__(self, name: str, level: int = 1):
        super().__init__(name, 120, 15, "Rogue", level)
        self.agility = 25

    def display_stats(self):
        super().display_stats()
        print(f"Agility: {self.agility}")


# Example objects (optional)
if __name__ == "__main__":
    warrior = Warrior("Thorin", 5)
    mage = Mage("Gandalf", 10)
    rogue = Rogue("Loki", 7)

    warrior.display_stats()
    print()
    mage.display_stats()
    print()
    rogue.display_stats()
