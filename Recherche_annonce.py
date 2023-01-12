# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 21:33:13 2023

@author: roman
"""



import difflib
import feedparser


class Annonce:
    def __init__(self, title, description, link):
        self.title = title
        self.description = description        
        self.link = link

        



# URL du flux RSS à analyser
rss_url = "https://brgm-recrute.talent-soft.com/handlers/offerRss.ashx?LCID=1036&Rss_Contract=559"

# Recherche de mot clé
search_key = 'géophysique'

# Compteur d'annonce correspondant au critere | à suppr
a=0

# Parse le flux RSS à l'aide de feedparser
feed = feedparser.parse(rss_url)

# La liste des annonces contenant les mots clés.
annonces = []

# Boucle sur les entrées du flux
for entry in feed.entries:
    # Vérifie si le titre de l'entrée contient le mot-clé
    similar_words = difflib.get_close_matches(search_key, entry.description.split(), cutoff=0.7)
    print("Les mots similaires : ", similar_words) 
    if len(similar_words)!=0:
        annonces.append(Annonce(entry.title, entry.description, entry.link))






for annonce in annonces:
    print(annonce.title)




