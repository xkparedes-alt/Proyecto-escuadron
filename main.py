#Nombres de los jugadores
from tanque import heroe_tanque
from atacante import heroe_atacante
from sanador import heroe_sanador
from explorador import heroe_explorador

def mostrar_menu():
    print("\n---BIENVENIDO A ESCUADRÓN HERO ---")
    print("Selecciona tu héroe para combatir:")
    print("1. Tanque (" + heroe_tanque.nombre + ")")
    print("2. Atacante (" + heroe_atacante.nombre + ")")
    print("3. Sanador (" + heroe_sanador.nombre + ")")
    print("4. Explorador (" + heroe_explorador.nombre + ")")
    print("5. Salir del juego")

def ejecutar_juego():
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción (1-5): ")

        # 2 y 3. Gestionar el flujo con switch (usando if/elif en Python)
        if opcion == "1":
            print(f"\nHas elegido al TANQUE.")
            print(f"Stats: Vida {heroe_tanque.vida}, Defensa {heroe_tanque.defensa}")
            print(heroe_tanque.accion_especial())
        
        elif opcion == "2":
            print(f"\nHas elegido al ATACANTE.")
            print(f"Stats: Ataque {heroe_atacante.ataque}, Energía {heroe_atacante.energia}")
            print(heroe_atacante.accion_especial())

        elif opcion == "3":
            print(f"\nHas elegido al SANADOR.")
            print(f"Stats: Magia {heroe_sanador.magia}, Fe {heroe_sanador.fe}")
            print(heroe_sanador.accion_especial())

        elif opcion == "4":
            print(f"\nHas elegido al EXPLORADOR.")
            print(f"Stats: Sigilo {heroe_explorador.sigilo}, Alcance {heroe_explorador.alcance}")
            print(heroe_explorador.accion_especial())

        elif opcion == "5":
            print("¡Gracias por jugar a Escuadrón Hero! Saliendo...")
            break
        
        #Opción incorrecta
        else:
            print(" Opción inválida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    ejecutar_juego()