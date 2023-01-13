# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 15:29:00 2023

@author: roman
"""

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


