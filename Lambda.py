# Definir funciones lambda 
area_circulo = lambda radio: 3.14159265359 * radio ** 2
area_triangulo = lambda base, altura: 0.5 * base * altura
area_cuadrado = lambda lado: lado ** 2

# Menú para que el usuario elija la figura geométrica
while True:
    print("Elige una figura geométrica:")
    print("1. Círculo")
    print("2. Triángulo")
    print("3. Cuadrado")
    print("4. Salir")
    
    opcion = input("Opción: ")

    if opcion == '1':
        radio = float(input("Ingresa el radio del círculo: "))
        print("Área del círculo:", area_circulo(radio))
    elif opcion == '2':
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        print("Área del triángulo:", area_triangulo(base, altura))
    elif opcion == '3':
        lado = float(input("Ingresa el lado del cuadrado: "))
        print("Área del cuadrado:", area_cuadrado(lado))
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
