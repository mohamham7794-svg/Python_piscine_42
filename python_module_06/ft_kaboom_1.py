

from alchemy.grimoire import dark_spellbook


print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
result = dark_spellbook.dark_spell_record('Shadow Bolt', 'bats and frogs')
print(f"Testing dark spell: {result}")
