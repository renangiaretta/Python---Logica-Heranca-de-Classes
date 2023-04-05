class Villager:
    def __init__(self, name: str, health: int = 50, defense: int = 0, attack: int = 0, is_alive: bool = True) -> None:
        self.name = name
        self.health = health
        self.defense = defense
        self.attack = attack
        self.is_alive = is_alive

    def __str__(self):
        return f'{vars(self)}'

    def check_health(self, incomming_attack_value: int):
        if incomming_attack_value < 0:
            raise ValueError('Ataque inválido')
        if self.defense < incomming_attack_value:
            self.health = self.health - incomming_attack_value
            if self.health < 0:
                self.health = 0
                self.is_alive = False
                return (self.is_alive, 'Target is dead!')
        if self.health > 0:
            return self.health

    def normal_attack(self, target):
        return target.check_health(self.attack)


class Mage(Villager):
    def __init__(self, name: str, attack: int = 10, mana: int = 100):
        super().__init__(name)
        self.attack = attack
        self.mana = mana

    def fire_ball(self, target):
        if self.mana < 20:
            return (False, 'Not enought mana!')
        self.mana = self.mana - 20
        attack_strength = (self.attack + 20)
        return target.check_health(attack_strength)


if __name__ == "__main__":
    villager = Villager("Villager")
    mage = Mage("Mage")

    print(
        "*"*50,
        "Esperado: {'name': 'Villager', 'health': 50, 'defense': 0, 'attack': 0, 'is_alive': True}",
        f"Resultado: {vars(villager)}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "Esperado: {'name': 'Mage', 'health': 50, 'defense': 0, 'attack': 10, 'is_alive': True, 'mana': 100}",
        f"Resultado: {vars(mage)}",
        "*"*50,
        sep="\n"
    )
    
    battle_result = mage.fire_ball(villager)

    print(
        "*"*50,
        "Esperado: 20",
        f"Resultado: {battle_result}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "Esperado: {'name': 'Villager', 'health': 20, 'defense': 0, 'attack': 0, 'is_alive': True}",
        f"Resultado: {vars(villager)}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "Esperado: {'name': 'Mage', 'health': 50, 'defense': 0, 'attack': 10, 'is_alive': True, 'mana': 80}",
        f"Resultado: {vars(mage)}",
        "*"*50,
        sep="\n"
    )

    battle_result = mage.normal_attack(villager)

    print(
        "*"*50,
        "Esperado: 10",
        f"Resultado: {battle_result}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "Esperado: {'name': 'Villager', 'health': 10, 'defense': 0, 'attack': 0, 'is_alive': True}",
        f"Resultado: {vars(villager)}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "Esperado: {'name': 'Mage', 'health': 50, 'defense': 0, 'attack': 10, 'is_alive': True, 'mana': 80}",
        f"Resultado: {vars(mage)}",
        "*"*50,
        sep="\n"
    )

    battle_result = mage.fire_ball(villager)

    print(
        "*"*50,
        f"Esperado: {(False, 'Target is dead!')}",
        f"Resultado: {battle_result}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "Esperado: {'name': 'Villager', 'health': 0, 'defense': 0, 'attack': 0, 'is_alive': False}",
        f"Resultado: {vars(villager)}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        "Esperado: {'name': 'Mage', 'health': 50, 'defense': 0, 'attack': 10, 'is_alive': True, 'mana': 60}",
        f"Resultado: {vars(mage)}",
        "*"*50,
        sep="\n"
    )

    battle_result = mage.fire_ball(villager)

    print(
        "*"*50,
        f"Esperado: {(False, 'Target is dead!')}",
        f"Resultado: {battle_result}",
        "*"*50,
        sep="\n"
    )

    print(
        "*"*50,
        f"Esperado: 40",
        f"Resultado: {mage.mana}",
        "*"*50,
        sep="\n"
    )

    battle_result = mage.fire_ball(villager)
    battle_result = mage.fire_ball(villager)
    battle_result = mage.fire_ball(villager)

    print(
        "*"*50,
        f"Esperado: {(False, 'Not enough mana!')}",
        f"Resultado: {battle_result}",
        "*"*50,
        sep="\n"
    )
