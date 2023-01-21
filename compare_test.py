
import difflib
import feedparser
import pickle
from datetime import datetime
import pandas as pd
import configparser









Main_file = pd.read_csv('Data/Daily_offers.csv',delimiter='|',header=0)
daily_offers = pd.read_csv('Data/Main_file.csv',delimiter='|',header=0)


new_offers = pd.DataFrame()
index_offer = 0
for offer in daily_offers.title: 
    if offer not in list(Main_file.title):
        Main_file = pd.concat([Main_file, daily_offers.iloc[index_offer].to_frame().T], ignore_index=True)
        new_offers = pd.concat([new_offers, daily_offers.iloc[index_offer].to_frame().T], ignore_index=True)
    index_offer = 1 + index_offer

print('main_file : ',Main_file)
print('new_offers : ',new_offers)
new_offers.to_csv('Data/new_offers.csv', index=False, sep='|')
Main_file.to_csv('Data/Main_file.csv', index=False, sep='|')

"""
new_offers = pd.read_csv('Data/new_offers.csv',delimiter='|',header=0)
report_offers = pd.read_csv('Data/Main_file.csv',delimiter='|',header=0)
"""