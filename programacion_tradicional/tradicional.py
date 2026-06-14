# Programa Tradicional
# Sistema de gestión de mascotas utilizando variables y funciones

def registrar_mascota():
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    edad = int(input("Ingrese la edad de la mascota: "))

    return nombre, especie, edad


def mostrar_mascota(nombre, especie, edad):
    print("\n--- INFORMACIÓN DE LA MASCOTA ---")
    print(f"Nombre: {nombre}")
    print(f"Especie: {especie}")
    print(f"Edad: {edad} años")


# Programa principal
nombre, especie, edad = registrar_mascota()
mostrar_mascota(nombre, especie, edad)
