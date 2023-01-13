# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 15:28:32 2023

@author: roman
"""


import difflib
import feedparser
from OfferBag import *
import pickle

# charger l'objet à partir du fichier
with open("Catalogue_offre.pkl", "rb") as f:
    blazd = pickle.load(f)

