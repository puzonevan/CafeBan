""" Recipe Script """
# Open browser to page with recipe 
# Find the Description 
# Find the Ingredients 
# Find the Directions 

import selenium 
import bs4
import requests

RECIPE_URLS = [
    'https://mykoreankitchen.com/dalgona-coffee-whipped-coffee/',
    'https://mykoreankitchen.com/yuja-tea-korean-citron-tea/',
    'https://mykoreankitchen.com/sweet-potato-latte/',
    'https://mykoreankitchen.com/korean-banana-milk/',
    'https://mykoreankitchen.com/sparkling-strawberry-punch/',
    'https://www.mrcoffee.com/service-and-support/recipes/cafe-barista-recipes/cafe-barista-recipes.html',
    ''
]

