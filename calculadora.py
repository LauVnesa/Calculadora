# Función para suma
def suma(a, b):
    return a + b

# Función para resta
def resta(a, b):
    return a - b

# Función para multiplicación
def multiplicacion(a, b):
    return a * b

# Función para división
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

# Función principal de la calculadora
def calculadora():
    print("Bienvenido a la calculadora")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    while True:
        opcion = input("Elija una operación (1/2/3/4/5): ")

        if opcion == '5':
            print("¡Hasta luego!")
            break
        
        if opcion in ('1', '2', '3', '4'):
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == '1':
                print("Resultado:", suma(num1, num2))
            elif opcion == '2':
                print("Resultado:", resta(num1, num2))
            elif opcion == '3':
                print("Resultado:", multiplicacion(num1, num2))
            elif opcion == '4':
                print("Resultado:", division(num1, num2))
        else:
            print("Opción inválida. Por favor, elija una opción válida.")

# Ejecutar la calculadora
calculadora()
