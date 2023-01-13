# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 21:33:13 2023

@author: roman
"""



import difflib
import feedparser
import pickle

class Annonce(object):
    
    
    def __init__(self, title, description, link):
        self.title = title
        self.description = description        
        self.link = link


class Catalogue(object):
    def __init__(self, annonces=None):
        self.annonces = []
        if isinstance(annonces, Annonce):
            annonces = [annonces]
        if annonces:
            self.annonces.extend(annonces)
        

    def append(self, annonce):
        if isinstance(annonce, Annonce):
            self.annonces.append(annonce)
        else:
            msg = 'Append only supports a single Trace object as an argument.'
            raise TypeError(msg)
        return self






# URL du flux RSS à analyser
rss_url = "https://brgm-recrute.talent-soft.com/handlers/offerRss.ashx?LCID=1036&Rss_Contract=559"

# Recherche de mot clé
search_key = ['géophysique',
              'traitement du signal',
              'géologie',
    ]

print("test2")

def Recherche_annonce(rss_url, search_key):
    # Parse le flux RSS à l'aide de feedparser
    feed = feedparser.parse(rss_url)
    test = Catalogue()
    #Boucle sur les mots clés
    for elem in search_key:
    # Boucle sur les entrées du flux
        for entry in feed.entries:
            # Vérifie si le titre de l'entrée contient le mot-clé
            similar_words = difflib.get_close_matches(elem, entry.description.split(), cutoff=0.7)
            if len(similar_words)!=0:
                test.append(Annonce(entry.title, entry.description, entry.link))
    
    a = len(feed.entries)
        
    liste_offre = []
    for elem in test.annonces:
        liste_offre.append(elem.title)
    liste_offre = set(liste_offre)
    
    Catalogue_offre = Catalogue()
    
    for elem in liste_offre:
        for entry in feed.entries:
            if elem==entry.title:
                Catalogue_offre.append(Annonce(entry.title, entry.description, entry.link))
        
    print("nombre d'annonces parcourues : ",a)
    print("nombre d'annonces correctes : ",len(Catalogue_offre.annonces))
    print("Les mots cles sont : ",search_key)
    
    #sauvegarder le Catalogue dans un fichier pkl
    with open("Catalogue_offre_a_suppr.pkl", "wb") as f:
        pickle.dump(Catalogue_offre, f)
    
    return

Recherche_annonce(rss_url,search_key)
