from bs4 import BeautifulSoup
import requests
import pandas as pd
from urls import *


class ScrapIndices:

    def validator_soup(self, url: str):
        """
        Validador Soup HTML
        Args:
            url: string url site
        Returns:
            soup: html pared
        """

        header = {
            'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
        }
        page = requests.get(url, headers=header)

        try:
            soup = BeautifulSoup(page.content, "html.parser")
        except:
            return None
        return soup

    def scrap_indices(self):
        """ 
        Tabla extraida con la libreria Pandas
        """
        column_names = {
                0: "Indices",
                1: "Nombre",
                2: "Fecha",
                3: "Dato",
                4: "Hace 3 meses",
                5: "Hace un año"
                }
        tabla = pd.read_html(INDICES_FINANCIERONS)

        # Eliminas de nulls 
        df = tabla[0].dropna()
        df = df.rename(columns=column_names)
        print(df)



if __name__ == '__main__':
    indices = ScrapIndices()
    indices.scrap_indices()
