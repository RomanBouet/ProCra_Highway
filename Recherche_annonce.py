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
import configparser

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



def Recherche_annonce(rss_url, contrat_rss, search_key, contrats, precision):
    # Parse le flux RSS à l'aide de feedparser
    feed = feedparser.parse(rss_url)
    annonce_contrat = []
    print(rss_url)

    annonce_keyword = []
    annonce_parcouru = 0

    for entry in feed.entries:
        annonce_parcouru +=1
        print(annonce_parcouru)
        if entry.tags[contrat_rss].term in contrats:
            for elem in search_key:
                similar_words = difflib.get_close_matches(elem, entry.description.split(), cutoff=precision)
                if len(similar_words) != 0:
                    annonce_keyword.append(Annonce(entry.title, entry.description, entry.link, entry.published, entry.tags[contrat_rss].term))


    test = feed.entries[1].title
    print('annonce parcouru infunction : ',annonce_parcouru)        
    
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
                
        
    #print("nombre d'annonces parcourues : ",annonce_parcouru)
    print("nombre d'annonces correctes : ",len(Catalogue_offre))
    #print("Les mots cles sont : ",search_key)
    
    #sauvegarder le Catalogue dans un fichier pkl
    with open("Catalogue_offre_a_suppr.pkl", "wb") as f:
        pickle.dump(Catalogue_offre, f)
    
    return Catalogue_offre, annonce_parcouru, test



#########################################################
#                   Paramètres                          #
#########################################################


# URL du flux RSS à analyser
config_files_url = pd.read_csv('site_web.txt',header=0)
# Recherche de mot clé


#CONFIGPARSER FILE A AJOUTER
search_key = ['géophysique',
              'traitement du signal',
              'géologie'
    ]

precision = 0.8

contrats = ['CDD','CDI','VIE']

#########################################################
#                       Main                            #
#########################################################


Offre_total = []
for elem in config_files_url.itertuples():
    Offres_corp, annonce_parcouru,test = Recherche_annonce(elem[1], elem[2], search_key, contrats, precision)
    Offre_total = Offre_total+Offres_corp
    print("annonce parcouru : ",annonce_parcouru)

df = pd.DataFrame([Offre.__dict__ for Offre in Offre_total])
df.sort_values(by='published')


df