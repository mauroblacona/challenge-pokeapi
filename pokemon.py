from dataclasses import dataclass
from typing import List

@dataclass
class Pokemon:
    """
    Representa un Pokémon con su informacion.
    """
    name: str
    types: List[str]
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int

    def is_alive(self) -> bool:
        """
        Verifica si el Pokémon todavia tiene vida.
        """
        return self.hp > 0

    def take_damage(self, damage: int) -> None:
        """
        Aplica el daño recibido.
        """
        self.hp = max(0, self.hp - damage)

    def __str__(self) -> str:
        """
        Retorna nombre y vida del Pokémon.
        """
        return f"{self.name} (HP: {self.hp})"

