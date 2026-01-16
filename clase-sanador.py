# sanador.py
# Rama: clase-sanador

class Sanador:
    """
    Clase que representa al personaje Sanador.
    Utiliza magia (maná) para curar o regenerar estadísticas.
    """

    def __init__(self):
        self.nombre = "Clérigo Sabio"
        self.mana = 200          # Energía o magia
        self.curacion = 60       # Poder de curación

    def mostrar_info(self):
        """Muestra el estado actual del sanador"""
        return (
            f"[ESTADO] {self.nombre}\n"
            f"Maná: {self.mana}\n"
            f"Poder de Curación: {self.curacion}"
        )

    def habilidad_especial(self):
        """
        Simula una habilidad especial de curación.
        Consume maná y cura al equipo.
        """
        if self.mana >= 40:
            self.mana -= 40
            return (
                f"[ACCIÓN] {self.nombre} lanza 'Rayo de Luz'\n"
                f"El equipo recupera {self.curacion} puntos de vida.\n"
                f"Maná restante: {self.mana}"
            )
        else:
            return "[ERROR] Maná insuficiente para usar la habilidad."


# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    sanador = Sanador()

    print(sanador.mostrar_info())
    print()
    print(sanador.habilidad_especial())
    print()
    print(sanador.mostrar_info())
