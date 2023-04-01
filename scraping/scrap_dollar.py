from bs4 import BeautifulSoup
import requests
import pandas as pd
from urls import *


class ScrapDollar:

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

    def dollar_hoy(self):
        soup = self.validator_soup(DOLLAR_HOY)
        # Dollar compra
        dollar_compra = soup.find_all('div', {'class': 'compra'})
        dollar_venta = soup.find_all('div', {'class': 'venta'})

        count = 0
        compra_list = []
        for div in dollar_compra:
            compra = div.find('div', {'class': 'val'}).text.strip('$')
            compra_list.append(float(compra))
            count += 1
            if count == 6:
                break

        count = 0
        venta_list = []
        for div in dollar_venta:
            venta = div.find('div', {'class': 'val'}).text.strip('$')
            venta_list.append(float(venta))
            count += 1
            if count == 6:
                break

        del compra_list[0]
        del venta_list[0]

        data = {
            'Dollar Blue': [compra_list[0], venta_list[0]],
            'Dollar Oficial': [compra_list[1], venta_list[1]],
            'Dollar Bolsa': [compra_list[2], venta_list[2]],
            'Dollar Liqui': [compra_list[3], venta_list[3]],
            'Dollar Cripto': [compra_list[4], venta_list[4]]
        }

        df = pd.DataFrame.from_dict(data,
                                    orient='index',
                                    columns=['compra', 'venta'])
        print(df)


if __name__ == '__main__':
    doll = ScrapDollar()
    doll.dollar_hoy()
