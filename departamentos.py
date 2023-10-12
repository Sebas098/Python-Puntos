import random

# Crea un diccionario vacío llamado Departamentos
Departamentos = {}

# Ingresa el nombre del Departamento como llave y su Capital como valor.
Departamentos["Amazonas"] = "leticia"
Departamentos["Antioquia"] = "medellin"
Departamentos["Atlantico"] = "barranquilla"
Departamentos["Caldas"] = "manizales"
# Agrega más departamentos y capitales según tus necesidades

# Ciclo para imprimir el Departamento y la capital
while True:
    # Escoge un departamento al azar (random)
    departamento = random.choice(list(Departamentos.keys()))
    capital_correcta = Departamentos[departamento]

    print(f"Departamento: {departamento}")
    intentos = 0

    while intentos < 3:
        # Solicita al usuario que ingrese su capital
        capital_usuario = input("Ingresa la capital del departamento o escribe 'salir' para salir: ")

        # Si el usuario escribe 'salir', el programa termina.
        if capital_usuario.lower() == "salir":
            print("Hasta luego.")
            exit()

        # Si la capital es incorrecta, debe seguir solicitando la capital hasta que se ingrese la correcta.
        if capital_usuario != capital_correcta:
            intentos += 1
            print("Capital incorrecta. Intenta de nuevo.")
        else:
            # Si el usuario escribe la capital correcta, imprime "Correcto" y rompe el bucle.
            print("Correcto.")
            break
    else:
        # Si el usuario agota los 3 intentos, imprime "Hasta luego".
        print(f"Hasta luego. La capital correcta era {capital_correcta} intenta de nuevo en otra oportunidad")
