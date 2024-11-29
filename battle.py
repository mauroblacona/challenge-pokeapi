import random
from pokemon import Pokemon
from typing import Tuple, List

class BattleLogic:
    """
    Maneja la lógica de la batalla Pokémon.
    """

    @staticmethod
    def calculate_damage(attacker: Pokemon, defender: Pokemon) -> int:
        """
        Calcula el daño infligido.
        """
        if random.choice([True, False]):
            return int((attacker.attack / defender.defense) * 10)
        else:
            return int((attacker.special_attack / defender.special_defense) * 10)

    @staticmethod
    def battle_turn(attacker: Pokemon, defender: Pokemon) -> Tuple[int, str]:
        """
        Ejecuta un turno y retorna daño y un mensaje de descripcion.
        """
        damage = BattleLogic.calculate_damage(attacker, defender)
        defender.take_damage(damage)
        return damage, f"{attacker.name} ataca a {defender.name} y causa {damage} puntos de daño."

    @staticmethod
    def determine_first_attacker(pokemon1: Pokemon, pokemon2: Pokemon) -> Tuple[Pokemon, Pokemon]:
        """
        Determina qué Pokémon ataca primero en base a su velocidad.
        """
        return (pokemon1, pokemon2) if pokemon1.speed >= pokemon2.speed else (pokemon2, pokemon1)

    @staticmethod
    def battle(pokemon1: Pokemon, pokemon2: Pokemon) -> Tuple[List[str], Pokemon]:
        """
        Ejecuta la batalla completa y retorna el paso a paso junto con el ganador.
        """
        first, second = BattleLogic.determine_first_attacker(pokemon1, pokemon2)
        battle_log = []

        for turn in range(1, 4):
            for attacker, defender in [(first, second), (second, first)]:
                message = BattleLogic.battle_turn(attacker, defender)
                battle_log.append(f"Turno {turn}: {message}")
                battle_log.append(f"{defender.name} HP restante: {defender.hp}")

                if not defender.is_alive():
                    battle_log.append(f"{attacker.name} ha ganado la batalla!")
                    return battle_log, attacker

        # Si después de 3 turnos ambos siguen vivos, gana el que tenga más HP
        if pokemon1.hp > pokemon2.hp:
            battle_log.append(f"{pokemon1.name} ha ganado la batalla con más HP restante!")
            return battle_log, pokemon1
        elif pokemon2.hp > pokemon1.hp:
            battle_log.append(f"{pokemon2.name} ha ganado la batalla con más HP restante!")
            return battle_log, pokemon2
        else:
            battle_log.append("¡La batalla ha terminado en empate!")
            return battle_log, None