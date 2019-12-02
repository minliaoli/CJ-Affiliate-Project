#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import sqlite3
from pyrebase_settings import db
import pymongo
import urllib


""" products = db.child("products").get()
    for product in products.each():
        print(product.val())
    conn = sqlite3.connect('db.sqlite3') #/Users/nathanguan/Documents/capstone/CJ_Affliliate-Project/OfferManager/offerManager/
    c = conn.cursor()
    for product in products.each():
        c.execute('INSERT INTO offers_offers VALUES (NULL, description, name, price)', product.val()) """
def main():

    #products = db.child("products").get()
    """for product in products.each():
        print(product.val())
    conn = sqlite3.connect('db.sqlite3') #/Users/nathanguan/Documents/capstone/CJ_Affliliate-Project/OfferManager/offerManager/
    c = conn.cursor()
    for product in products.each():
        c.execute('INSERT INTO offers_offers VALUES (NULL, description, name, price)', product.val()) """

    client = pymongo.MongoClient("mongodb+srv://nguan:Ng5668253@cluster0-kmbeq.mongodb.net/test?retryWrites=true&w=majority")
    db = client['test']
    col = db['OneOffer']
    for x in col.find():
        print(x)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'offerManager.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()