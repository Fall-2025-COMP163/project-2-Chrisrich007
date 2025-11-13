# ============================================================
# Project 2: RPG Character Inheritance & Composition System
# ============================================================
# Author: Christopher Arnold
# Demonstrates:
#   - Inheritance (Character → Player → subclasses)
#   - Method overriding (attack, display_stats)
#   - Composition (characters have weapons)
#   - Special abilities unique to each subclass
# ============================================================

import random

# ------------------------------------------------------------
# Base Class: Character
# ------------------------------------------------------------
class Character:
    """Base class for all characters (both players and NPCs)."""

    def __init__(self, name, health, strength, magic):
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        self.weapon = None  # Composition: may hold a Weapon object

    def take_damage(self, amount):
        """Reduce health, but never below 0."""
        if amount < 0:
            amount = 0  # Safety check
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def attack(self, target):
        """Base attack — deals damage equal to strength (+ weapon bonus)."""
        damage = self.strength
        if self.weapon:
            damage += self.weapon.damage_bonus
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

    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus

    def display_info(self):
        """Show weapon info."""
        print(f"Weapon Name: {self.name}, Damage Bonus: {self.damage_bonus}")


# ------------------------------------------------------------
# Derived Class: Player (inherits from Character)
# ------------------------------------------------------------
class Player(Character):
    """A player character with a defined class type (Warrior, Mage, Rogue)."""

    def __init__(self, name, health, strength, magic, character_class, level=1):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = level  # ✅ Added to fix missing attribute test

    def display_stats(self):
        """Show all inherited stats plus character class and level."""
        super().display_stats()
        print(f"Class: {self.character_class}")
        print(f"Level: {self.level}")  # ✅ Added for more clarity


# ------------------------------------------------------------
# Subclass: Warrior
# ------------------------------------------------------------
class Warrior(Player):
    """Warrior: Strong and durable with a powerful melee ability."""

    def __init__(self, name):
        super().__init__(name, health=150, strength=15, magic=3, character_class="Warrior", level=1)
        self.weapon = Weapon("Iron Sword", 10)

    def attack(self, target):
        """Override: Stronger physical attack."""
        damage = self.strength + (self.weapon.damage_bonus if self.weapon else 0)
        target.take_damage(damage)

    def power_strike(self, target):
        """Special ability: Extra-powerful attack."""
        damage = random.randint(25, 45)  # ✅ Keeps within 10–50 range
        target.take_damage(damage)


# ------------------------------------------------------------
# Subclass: Mage
# ------------------------------------------------------------
class Mage(Player):
    """Mage: Fragile but capable of high magic damage."""

    def __init__(self, name):
        super().__init__(name, health=80, strength=5, magic=20, character_class="Mage", level=1)
        self.weapon = Weapon("Magic Staff", 12)

    def attack(self, target):
        """Override: Basic magic attack."""
        damage = self.magic + (self.weapon.damage_bonus if self.weapon else 0)
        target.take_damage(damage)

    def fireball(self, target):
    """Special ability: Large burst of magical fire."""
    damage = random.randint(20, 50)  # generate damage
    damage = min(50, max(10, damage))  # ensure stays between 10–50
    target.take_damage(damage)



# ------------------------------------------------------------
# Subclass: Rogue
# ------------------------------------------------------------
class Rogue(Player):
    """Rogue: Agile and precise, specializes in critical sneak attacks."""

    def __init__(self, name):
        super().__init__(name, health=100, strength=10, magic=8, character_class="Rogue", level=1)
        self.weapon = Weapon("Steel Dagger", 8)

    def attack(self, target):
        """Override: Quick attack with agility bonus."""
        damage = self.strength + 3 + (self.weapon.damage_bonus if self.weapon else 0)
        target.take_damage(damage)

    def sneak_attack(self, target):
        """Special ability: Critical backstab with high damage."""
        damage = random.randint(15, 40)  # ✅ Reasonable range (10–50)
        target.take_damage(damage)


# ------------------------------------------------------------
# Example Usage (Optional Manual Test)
# ------------------------------------------------------------
if __name__ == "__main__":
    hero = Warrior("Aragorn")
    monster = Character("Goblin", 100, 8, 0)

    hero.display_stats()
    hero.attack(monster)
    print(f"{monster.name}'s Health after attack: {monster.health}")
    hero.power_strike(monster)
    print(f"{monster.name}'s Health after Power Strike: {monster.health}")
