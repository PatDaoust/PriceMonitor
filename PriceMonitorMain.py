# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 12:30:16 2022

@author: catal
"""
"""
concept:
    bot that checks specified amazon webpage, and emails if price is bellow a certain level

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
"""