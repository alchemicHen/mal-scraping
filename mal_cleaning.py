#Cleaning the topMAL.csv

import pandas as pd
import mal_scraper as mal
from datetime import datetime
import re

#importing csv from local file
mal_df = pd.read_csv(r'C:\Users\micha.DESKTOP-U2HVTMF\MyPythonScripts\Jupyter\MAL Scraping\mal-scraping\topMAL.csv')
print(mal_df.head())

#Removing # from user rank
ranklist = []
for rank in mal_df['User Rank']:
    rank = rank.replace('#', '')
    ranklist.append(rank)
mal_df['User Rank'] = ranklist

#Dropping Scraping Errors: user rank > 1000
for rank in mal_df['User Rank']:
    if int(rank) > 1000:
        index = mal_df.index[mal_df['User Rank'] == rank][0]
        mal_df.drop(mal_df.index[index], inplace=True)

#Standardizing dates - changing it do that it's the month/year when it ended
endDateList = []
for date in mal_df['Airdate']:
    dlist = re.findall('\d+', date)
    endDateList.append(dlist[-1])
mal_df['Airdate'] = endDateList

#Changing Airdate column to End Date and Unnamed:0 to Score Rank
mal_df.rename(columns = {'Airdate': 'End Date', 'Unnamed: 0': 'Score Rank'}, inplace=True)

#Adding 1 to all Score Ranks
srList = []
for rank in mal_df['Score Rank']:
    srList.append(rank + 1)
mal_df['Score Rank'] = srList

#Standardizing runtime and watchtime

#Converting string "x days, x hours, x minutes" to #hours to watch
hoursList = []
for time in mal_df['Time to Watch']:
    tlist = re.findall('\d+', time)
    if len(tlist) > 2:
        hmlist = [int(tlist[0]) * 24+ int(tlist[1]), int(tlist[2])] #Adds 24 to hours if #days exists
    else:
        hmlist = tlist
    hours = int(hmlist[0]) + int(hmlist[1])/60 #converting minutes to hours and adding to hours
    hours_r = round(hours, 2)
    hoursList.append(hours_r)
mal_df['Time to Watch'] = hoursList

#Converting string "x hours, x min" to runtime in minutes
minsList = []
for runtime in mal_df['Episode Runtime']:
    tlist = re.findall('\d+', runtime)
    if len(tlist) > 1:
        mins = int(tlist[0]) * 60 + int(tlist[1])
    else:
        mins = tlist[0]
    minsList.append(mins)
mal_df['Episode Runtime'] = minsList

#TODO: Write function that standardizes all this regex stuff: repeated 3 times for cleaning/not very efficient

print(mal_df.head())

#Exporting csv to local file
mal_df.to_csv(r'C:\Users\micha.DESKTOP-U2HVTMF\MyPythonScripts\Jupyter\MAL Scraping\mal-scraping\mal_cleaned.csv', index=False)



