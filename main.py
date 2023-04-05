from scraping.scrap_dollar import ScrapDollar
from scraping.scrap_i_financieros import ScrapIndices
#from scraping.urls import *


class Menu:

    def __init__(self):
        self.dollar = ScrapDollar()
        self.indices = ScrapIndices()

    def run(self):
        while True:
            print("Menu")
            print("1 Valores actuales del dóllar")
            print("2 Indices financieros")

            opcion = input("Seleccione la opción: ")

            if opcion == "1":
                self.dollar.dollar_hoy()

            elif opcion == "2":
                self.indices.scrap_indices()

            elif opcion == "x":
                print("Programa finalizado")
                break

            else:
                print("Por favor elija una opción de la lista")
                


if __name__ == '__main__':
    menu = Menu()
    menu.run()
