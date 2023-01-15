# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 21:33:13 2023

@author: roman
"""



import difflib
import feedparser
import pickle
from datetime import datetime
import pandas as pd

class Annonce(object):
    
    
    def __init__(self, title, description, link, published, tag):
        self.title = title
        self.description = description        
        self.link = link
        self.published = published
        self.tag = tag


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



def Recherche_annonce(rss_url, contrat_rss, search_key, contrats):
    # Parse le flux RSS à l'aide de feedparser
    feed = feedparser.parse(rss_url)
    annonce_contrat = []

    #Boucle sur les mots contrats
    for contrat in contrats:
    # Boucle sur les entrées du flux
        for entry in feed.entries:
            if len(entry.tags[contrat_rss].term) != contrat:
                annonce_contrat.append(Annonce(entry.title, entry.description, entry.link, entry.published, entry.tags[contrat_rss]))
    
    annonce_keyword = []
    #Boucle sur les mots clés
    for elem in search_key:
    # Boucle sur les entrées du flux
        for entry in feed.entries:
            if entry.tags[contrat_rss].term in contrats:
                # Vérifie si le titre de l'entrée contient le mot-clé
                similar_words = difflib.get_close_matches(elem, entry.description.split(), cutoff=0.7)
                if len(similar_words)!=0:
                    annonce_keyword.append(Annonce(entry.title, entry.description, entry.link, entry.published, entry.tags[contrat_rss].term))
        
            

    a = len(feed.entries)
    
    
    liste_offre = []
    for elem in annonce_keyword:
        liste_offre.append(elem.title)
    liste_offre = set(liste_offre)
    
    Catalogue_offre = []
    
    for elem in liste_offre:
        for entry in feed.entries:
            if elem==entry.title:
                publiched_date = datetime.strptime(entry.published[5:25], '%d %b %Y %H:%M:%S')
                Catalogue_offre.append(Annonce(entry.title, entry.description, entry.link, publiched_date, entry.tags[contrat_rss].term))
                
        
    print("nombre d'annonces parcourues : ",a)
    print("nombre d'annonces correctes : ",len(Catalogue_offre))
    print("Les mots cles sont : ",search_key)
    
    #sauvegarder le Catalogue dans un fichier pkl
    with open("Catalogue_offre_a_suppr.pkl", "wb") as f:
        pickle.dump(Catalogue_offre, f)
    
    return Catalogue_offre



#########################################################
#                   Paramètres                          #
#########################################################


# URL du flux RSS à analyser
rss_url = ["https://brgm-recrute.talent-soft.com/handlers/offerRss.ashx?LCID=1036","https://www.emploi.cea.fr/handlers/offerRss.ashx?LCID=1036"]

# Recherche de mot clé
search_key = ['géophysique',
              'traitement du signal',
              'géologie',
    ]


contrat_rss = 1
contrats = ['CDD','CDI']

#########################################################
#                       Main                            #
#########################################################


Offre_total = []
for elem in rss_url:
    Offres_corp = Recherche_annonce(elem, contrat_rss, search_key, contrats)
    Offre_total = Offre_total+Offres_corp #  .append(Offres_corp)

df = pd.DataFrame([Offre.__dict__ for Offre in Offre_total])
df.sort_values(by='published')
