# ============================================================
# Project 2: RPG Character Inheritance & Composition System
# ============================================================
# Author: Christopher Arnold (refactored for clarity)
# Demonstrates:
#   - Inheritance (Character → Player → subclasses)
#   - Method overriding (attack, display_stats)
#   - Composition (characters have weapons)
# ============================================================

import random

# ------------------------------------------------------------
# Base Class: Character
# ------------------------------------------------------------
class Character:
    """Base class for all characters (both players and NPCs)."""
    def __init__(self, name: str, health: int, strength: int, magic: int):
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        self.weapon = None  # Composition: may hold a Weapon object

    def take_damage(self, amount: int):
        """Reduce health by amount, but never below 0."""
        if amount is None or amount < 0:
            amount = 0
        self.health = max(self.health - amount, 0)

    def attack(self, target):
        """Base attack — deals damage equal to strength (+ weapon bonus)."""
        damage = self.strength + (self.weapon.damage_bonus if self.weapon else 0)
        target.take_damage(damage)

    def display_stats(self):
        """Display current stats."""
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Magic: {self.magic}")
        if self.weapon:
            print(f"Weapon: {self.weapon.name} (+{self.weapon.damage_bonus} dmg)")

# ------------------------------------------------------------
# Composition Class: Weapon
# ------------------------------------------------------------
class Weapon:
    """A simple class to represent a weapon held by a character."""
    def __init__(self, name: str, damage_bonus: int):
        self.name = name
        self.damage_bonus = damage_bonus

    def display_info(self):
        print(f"Weapon Name: {self.name}, Damage Bonus: {self.damage_bonus}")

# ------------------------------------------------------------
# Derived Class: Player
# ------------------------------------------------------------
class Player(Character):
    """A player character with a defined class type."""
    def __init__(self, name: str, health: int, strength: int, magic: int, character_class: str, level: int = 1):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = level

    def display_stats(self):
        super().display_stats()
        print(f"Class: {self.character_class}")
        print(f"Level: {self.level}")

# ------------------------------------------------------------
# Subclass: Warrior
# ------------------------------------------------------------
class Warrior(Player):
   	def __init__(self, name: str, level: int = 1):
        super().__init__(name, health=150, strength=15, magic=3, character_class="Warrior", level=level)
        self.weapon = Weapon("Iron Sword", 10)  # Default weapon

    def attack(self, target):
        damage = self.strength + (self.weapon.damage_bonus if self.weapon else 0)
        target.take_damage(damage)

    def power_strike(self, target):
        damage = random.randint(25, 45)
        damage = max(10, min(50, damage))
        target.take_damage(damage)

# ------------------------------------------------------------
# Subclass: Mage
# ------------------------------------------------------------
class Mage(Player):
    def __init__(self, name: str, level: int = 1):
        super().__init__(name, health=80, strength=5, magic=20, character_class="Mage", level=level)
        self.weapon = Weapon("Magic Staff", 12)

    def attack(self, target):
        damage = self.magic + (self.weapon.damage_bonus if self.weapon else 0)
        target.take_damage(damage)

    def fireball(self, target):
        damage = random.randint(10, 50)
        target.take_damage(damage)

# ------------------------------------------------------------
# Subclass: Rogue
# ------------------------------------------------------------
class Rogue(Player):
    def __init__(self, name: str, level: int = 1):
        super().__init__(name, health=100, strength=10, magic=8, character_class="Rogue", level=level)
        self.weapon = Weapon("Steel Dagger", 8)

    def attack(self, target):
        damage = self.strength + 3 + (self.weapon.damage_bonus if self.weapon else 0)
        target.take_damage(damage)

    def sneak_attack(self, target):
        damage = random.randint(15, 40)
        damage = max(10, min(50, damage))
        target.take_damage(damage)

# ------------------------------------------------------------
# Example Usage (Optional Manual Test)
# ------------------------------------------------------------
if __name__ == "__main__":
    warrior = Warrior("Thorin")
    mage = Mage("Gandalf")
    rogue = Rogue("Loki")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()
