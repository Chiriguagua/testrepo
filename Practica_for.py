from tkinter import Menu


def run():
    # menu ="""
    # Bienvenido a la impresora de números.
    # ¿Hasta qué número deseas imprimir? """
    # advertencia = """
    # Por favor ingresa un número mayor que 0: """
    # numero = int(input(menu))
    
    # while numero <= 0 :
    #     numero = int(input(advertencia))
    
    # for i in range(numero + 1):
    #     print(i)
    # Abajo sigue una nueva secuencia de código.

    menu = """
    Bienvenido a la pirámide.
    ¿Cuántos niveles desea en su pirámide? """
    advertencia = """
    Ingrese un número mayor que cero: """

    niveles = int(input(menu))

    while niveles < 0 :
        niveles = int(input(advertencia))
    
    piramide = []
    counter = 1

    while niveles > len(piramide):
        piramide.append(1)
        print(piramide)
        if niveles > len(piramide):
            while counter < niveles:
                piramide.append(1)
                print(piramide)
                counter = counter + 1
                






if __name__ == "__main__":
    run()