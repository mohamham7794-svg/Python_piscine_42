import time
from decorator_mastery import spell_timer, retry_spell, MageGuild


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.101)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print("\nTesting retrying spell...")

    attempts = [0]

    @retry_spell(3)
    def unstable_spell():
        attempts[0] += 1
        if attempts[0] < 3:
            raise RuntimeError("Spell unstable!")
        return "Spell casting failed after 3 attempts"

    print(unstable_spell())
    print("Waaaaaaagh spelled !")

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Al"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))