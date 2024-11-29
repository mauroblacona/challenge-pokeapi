import aiohttp
import ssl
from typing import Dict, Any
from pokemon import Pokemon

class PokeAPIHandler:
    """
    Maneja las interacciones con la PokeAPI.
    """
    BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

    @staticmethod
    async def get_pokemon_data(name: str) -> Dict[str, Any]:
        """
        Obtiene los datos de un Pokémon.
        """
        
        # Crear un ClientSession con configuración SSL personalizada
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        connector = aiohttp.TCPConnector(ssl=ssl_context)
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.get(f"{PokeAPIHandler.BASE_URL}{name.lower()}") as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise ValueError(f"No se pudo obtener datos para el Pokémon: {name}")

    @staticmethod
    def create_pokemon_from_data(data: Dict[str, Any]) -> Pokemon:
        """
        Crea un objeto Pokemon a partir de los datos de la API.
        """
        stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
        return Pokemon(
            name=data['name'].capitalize(),
            types=[t['type']['name'] for t in data['types']],
            hp=stats['hp'],
            attack=stats['attack'],
            defense=stats['defense'],
            special_attack=stats['special-attack'],
            special_defense=stats['special-defense'],
            speed=stats['speed']
        )

    @classmethod
    async def get_pokemon(cls, name: str) -> Pokemon:
        """
        Obtiene un Pokémon de la API y lo convierte en un objeto Pokemon.
        """
        try:
            data = await cls.get_pokemon_data(name)
            return cls.create_pokemon_from_data(data)
        except ValueError as e:
            print(f"Error: {e}")
            raise