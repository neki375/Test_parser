#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
import csv


HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"}
PAGES = ["https://ten-nis.ru/39-raketki-dlja-bolshogo-tennisa/?gclid=EAIaIQobChMIkcCbh72P8AIVfgWiAx0n_ALeEAAYASAAEgLoH_D_BwE&page=%s" % i
         for i in range(1, 21)]

csvfile = open("parser.csv", "w")
writer = csv.writer(csvfile)
writer.writerow(["Название", "Цена", "Описание", "Ссылка на картинку"])


def get_dom(page):
    try:
        html = requests.get(page, headers=HEADERS).text
    except Exception as e:
        print(e)
    return BeautifulSoup(html, "lxml")


def main():
    for page_url in tqdm(PAGES, "Pages"):
        all = get_dom(page_url)
        product_list = all.find_all(class_="products")
        for item in product_list:
            names_conteiner = item.find_all(class_="h3")
            for name in names_conteiner:
                page_with_info = name.find("a")["href"]
                names = name.find("a").text
                info = get_dom(page_with_info)
                price = info.find(class_="current-price").text.replace("\xa0", "").replace("\n", "")
                description = info.find(class_="product-description").text.replace("\xa0", "").replace("\n", "")
                img = info.find(class_="js-qv-product-cover")["src"]
                writer.writerow([names, price, description, img])


if __name__ == "__main__":
    main()
