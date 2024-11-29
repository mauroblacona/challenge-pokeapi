import asyncio
import sys
from handler_poke_api import PokeAPIHandler
from battle import BattleLogic

async def main(pokemon1_name: str, pokemon2_name: str) -> None:
    """
    Función principal que maneja el flujo de la aplicación.
    """
    try:
        # Obtener datos de los Pokémon
        pokemon1 = await PokeAPIHandler.get_pokemon(pokemon1_name)
        pokemon2 = await PokeAPIHandler.get_pokemon(pokemon2_name)

        # Mostrar información básica de los Pokémon
        print(f"\nInformación de {pokemon1.name}:")
        print(f"Tipos: {', '.join(pokemon1.types)}")
        print(f"HP: {pokemon1.hp}, Ataque: {pokemon1.attack}, Defensa: {pokemon1.defense}")
        print(f"Ataque Especial: {pokemon1.special_attack}, Defensa Especial: {pokemon1.special_defense}")
        print(f"Velocidad: {pokemon1.speed}\n")

        print(f"\nInformación de {pokemon2.name}:")
        print(f"Tipos: {', '.join(pokemon2.types)}")
        print(f"HP: {pokemon2.hp}, Ataque: {pokemon2.attack}, Defensa: {pokemon2.defense}")
        print(f"Ataque Especial: {pokemon2.special_attack}, Defensa Especial: {pokemon2.special_defense}")
        print(f"Velocidad: {pokemon2.speed}\n")

        # Ejecutar la batalla
        battle_log, winner = BattleLogic.battle(pokemon1, pokemon2)

        # Mostrar el registro de la batalla
        print("\nRegistro de la batalla:")
        for event in battle_log:
            print(event)

        # Mostrar el resultado final
        if winner:
            print(f"\n¡{winner.name} ha ganado la batalla!")
        else:
            print("\n¡La batalla ha terminado en empate!")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso correcto de ejecucion: python battle.py <pokemon1> <pokemon2>")
        sys.exit(1)

    asyncio.run(main(sys.argv[1], sys.argv[2]))