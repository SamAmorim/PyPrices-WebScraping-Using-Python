import requests
from bs4 import BeautifulSoup
import re
import pandas as pd 
import math

class Mercado_Livre:
    
    def __init__(self, category, url, headers, extraction_date):
        self.extraction_date = extraction_date
        self.category = category
        self.url = url
        self.headers = headers
        
        self.produtos = {
            "Titulo" : [],
            "Categoria" : [],
            "Preco" : [],
            "Vendedor" : [],
            "Desconto": [],
            "Data_Extracao": []    
        }
        
    def __set_products(self, tittle, price, seller, discount, category, extraction_date):
        self.produtos["Titulo"].append(tittle) 
        self.produtos["Categoria"].append(category)
        self.produtos["Preco"].append(price)
        self.produtos["Vendedor"].append(seller) 
        self.produtos["Desconto"].append(discount)      
        self.produtos["Data_Extracao"].append(extraction_date)
        
    def set_url(self, url):
        self.url = url
        
    def get_products(self):
        return self.produtos
    
    def get_url(self):
        return self.url
    
    def get_headers(self):
        return self.headers
    
    def get_category(self):
        return self.category
    
    def get_extraction_date(self):
        return self.extraction_date

    def extract_data(self):
        while True:
            site = requests.get(self.get_url(), self.get_headers())
            soup = BeautifulSoup(site.content, 'html.parser')
            
            products = soup.find_all('div', {'class': 'poly-card__content'})
            for product in products:
                try:
                    product_tittle = product.find('a', {'class': 'poly-component__title'}).get_text()
                except:
                    product_tittle = 'N/A'
                try:
                    product_price = product.find('span', {'class': 'andes-money-amount andes-money-amount--cents-superscript'}).get_text()
                except:
                    product_price = 'N/A'
                try:
                    product_discount = product.find('span', {'class': 'andes-money-amount__discount'}).get_text()
                except:
                    product_discount = 'N/A'
                try:
                    product_seller = product.find('span', {'class': 'poly-component__brand'}).get_text()
                except:
                    product_seller = 'N/A'
                try:
                    product_category = self.get_category()
                except:
                    product_category = 'N/A'
                try:
                    product_extraction_date = self.get_extraction_date()
                except:
                    product_extraction_date = 'N/A'
                
                self.__set_products(tittle=product_tittle, price=product_price, seller=product_seller,discount=product_discount, category=product_category, extraction_date=product_extraction_date)
            self.set_url(self.next_page(soup))
            if not self.get_url():
                break
            print('Procurando em ', self.get_url())
        return self.get_products()
            
                

    def next_page(self, soup):
        pagina = soup.find('ul', {'class': 'andes-pagination ui-search-andes-pagination andes-pagination--large'})
        if not pagina.find('li', {'class','andes-pagination__button andes-pagination__button--next andes-pagination__button--disabled'}):
            proxima = paginas = soup.find('a', title='Seguinte', href= True)
            url_final = str(proxima['href'])
            return url_final
        else:
            return None