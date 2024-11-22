#Lista de nombres
nombres = ["Harry Houdini",
    "Newton",
    "David Blaine",
    "Hawking",
    "Messi",
    "Teller",
    "Einstein",
    "Pele",
    "Juanes"]

# listas de magos, científicos y otros
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = ["pele", "Juanes"]

# Función para hacer grandiosos a los magos y modificar la lista original
def hacer_grandioso(lista_magos):
    for i in range(len(lista_magos)):
        lista_magos[i] = "El gran " + lista_magos[i]

# Función para imprimir el nombre de cada persona en la lista
def imprimir_nombres(titulo, lista):
    print(titulo)
    for nombre in lista:
        print(nombre)
    print()  #Dejamos una filaa en blanco para separar

# Imprimir la lista completa de nombres antes de ser modificados
imprimir_nombres("Nombres originales antes de ser modificados:", nombres)

# Hacer grandiosos a los magos y imprimir las listas separadas
hacer_grandioso(magos)
imprimir_nombres("Magos Grandiosos: ", magos)
imprimir_nombres("Cientificos: ", cientificos)
imprimir_nombres("Otros: ", otros)
