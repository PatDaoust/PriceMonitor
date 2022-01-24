# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 12:30:16 2022

@author: catal
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen
"""
concept:
    bot that checks specified amazon webpage, and emails if price is bellow a set price

    in 1st method:
    input: amazon URL, max price
    use web scraping techniques to gather:
        name of item
        price of item
    if current_price <= max_price:
        return True

    in 2nd method:
    email if True
    input: bollean True/False
    info to email:
        name of item
        URL
        current price
        listed maz price
        recommend to buy now

    bonus method:
        auto runs daily
        can run mutiple URLs in one shot
"""


def priceUnderMax(URL, max_price):
    """assumes URL is a string, representing an amazon item listing's URL
    assumes max_price is a numerice, representing the price at which to alert
    returns a boolean if the price of the item is <= max_price
    """
    # get webpage
    # find current_price
    current_price = 0  # TODO
    # return result
    return current_price < max_price


if __name__ == "__main__":
    print("kittens")
    priceUnderMax("https://www.amazon.ca/gp/product/B00K0A37OG/", 99.99)
