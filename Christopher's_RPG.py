"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Christopher Arnold
Date: [Date]

AI Usage: AI was used to assist in building inheritance structure, method overriding, 
and ensuring correct OOP formatting. I reviewed and understood all final code.
"""

import random

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# CHARACTER CLASSES
# ============================================================================

class Character:
    """Base class for all characters."""

    def __init__(self, name, health, strength, magic):
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic

    def attack(self, target):
        """Basic attack based on strength."""
        damage = self.strength
        print(f"{self.name} attacks {target.name} for {damage} damage.")
        target.take_damage(damage)

    def take_damage(self, damage):
        """Reduce health; ensure it doesn't go below 0."""
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def display_stats(self):
        """Display base character stats."""
        print(f"Name: {self.name} | Health: {self.health} | Strength: {self.strength} | Magic: {self.magic}")

# ---------------------------------------------------------------------------

class Player(Character):
    """Inherits from Character, adds player-specific data."""

    def __init__(self, name, character_class, health, strength, magic):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0

    def display_stats(self):
        """Override to include class and level."""
        super().display_stats()
        print(f"Class: {self.character_class} | Level: {self.level} | EXP: {self.experience}")

# ---------------------------------------------------------------------------

class Warrior(Player):
    """Strong physical fighter."""

    def __init__(self, name):
        super().__init__(name, "Warrior", 120, 15, 5)

    def attack(self, target):
        """Override - physical attack with bonus damage."""
        damage = self.strength + 5
        print(f"{self.name} slashes fiercely at {target.name} for {damage} damage!")
        target.take_damage(damage)

    def power_strike(self, target):
        """Special ability - very strong attack."""
        damage = self.strength * 2
        print(f"{self.name} uses Power Strike on {target.name} for {damage} damage!!")
        target.take_damage(damage)

# ---------------------------------------------------------------------------

class Mage(Player):
    """Magical spellcaster."""

    def __init__(self, name):
        super().__init__(name, "Mage", 80, 8, 20)

    def attack(self, target):
        """Override - use magic for attacks."""
        damage = self.magic
        print(f"{self.name} casts a minor spell on {target.name} for {damage} magic damage!")
        target.take_damage(damage)

    def fireball(self, target):
        """Special ability - powerful spell."""
        damage = self.magic + 10
        print(f"{self.name} hurls a FIREBALL at {target.name} for {damage} magic damage!!")
        target.take_damage(damage)

# ---------------------------------------------------------------------------

class Rogue(Player):
    """Sneaky and agile fighter."""

    def __init__(self, name):
        super().__init__(name, "Rogue", 90, 12, 10)

    def attack(self, target):
        """Override - chance for critical hit."""
        crit_chance = random.randint(1, 10)
        if crit_chance <= 3:  # 30% chance
            damage = self.strength * 2
            print(f"{self.name} lands a CRITICAL HIT on {target.name} for {damage} damage!")
        else:
            damage = self.strength
            print(f"{self.name} attacks swiftly for {damage} damage.")
        target.take_damage(damage)

    def sneak_attack(self, target):
        """Special ability - guaranteed critical hit."""
        damage = self.strength * 2
        print(f"{self.name} performs a Sneak Attack on {target.name} for {damage} damage!")
        target.take_damage(damage)

# ---------------------------------------------------------------------------

class Weapon:
    """Composition class - characters can have weapons."""

    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus

    def display_info(self):
        print(f"Weapon: {self.name} | Damage Bonus: {self.damage_bonus}")

# ============================================================================
# MAIN TEST PROGRAM
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)

    # Create characters
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")

    # Display stats
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()

    # Polymorphism demonstration
    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    dummy = Character("Target Dummy", 100, 0, 0)
    for c in [warrior, mage, rogue]:
        print(f"\n{c.name} attacks dummy:")
        c.attack(dummy)
        dummy.health = 100  # reset

    # Test special abilities
    print("\n✨ Testing Special Abilities:")
    e1 = Character("Enemy1", 50, 0, 0)
    e2 = Character("Enemy2", 50, 0, 0)
    e3 = Character("Enemy3", 50, 0, 0)
    warrior.power_strike(e1)
    mage.fireball(e2)
    rogue.sneak_attack(e3)

    # Weapon composition
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
    sword.display_info()
    staff.display_info()
    dagger.display_info()

    # Battle test
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()

    print("\n✅ Testing complete!")
