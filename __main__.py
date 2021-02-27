#Scraping mal and creating dataframe

import mal_scraper as mal
from mal_scraper import GetTop
import pandas as pd
import os

# self.title
# self.url
# self.episode_count
# self.runtime
# self.airdate
# self.status
# self.time_to_watch
# self.user_rating
# self.user_rank
# self.user_popularity
# self.similar_shows
# self.studios
# self.genres
# self.JSON 

#Getting a list of the top 50 titles
top50 = mal.GetTop(50)
t50titles= []
for tp in top50.items():
    details = tp[1]
    t50titles.append(details['title'])
print(t50titles)

#empty dataframe for list of dictionaries to be appended to
mal_df = pd.DataFrame()
#Creating empty list to be filled with dictionaries
anime_lod = [
            ]

count = 0 #count for index in t50titles
for anime in t50titles:
    malobj = mal.MAL(anime)
    title = t50titles[count]
    count += 1
    user_rank = malobj.user_rank
    user_rating = malobj.user_rating
    popularity = malobj.user_popularity
    members = malobj.members
    episode_count = malobj.episode_count
    runtime = malobj.runtime
    airdate = malobj.airdate
    watchtime = malobj.time_to_watch
    studios = malobj.studios
    genres = malobj.genres
    status = malobj.status

    anime_dict = {'Title': title, 'User Rank': user_rank, 'User Rating': user_rating, 'Popularity Ranking': members, 'Episode Count': episode_count, 
                'Episode Runtime': runtime, 'Airdate': airdate, 'Time to Watch': watchtime, 'Studios': studios, 'Genres':genres, 'Status': status}
    
    anime_lod.append(anime_dict)
    #TODO: AttributeError: probably means that that page doesn't have that type. Can catch and assign value to clean

#Changing list of dictionaries into dataframe
anime_df = pd.DataFrame(anime_lod)
mal_df = mal_df.append(anime_df)
print(mal_df.head())

#Exporting dataframe to local csv
os.chdir(r'C:\Users\micha.DESKTOP-U2HVTMF\MyPythonScripts\Jupyter\MAL Scraping\mal-scraping')
mal_df.to_csv(r'C:\Users\micha.DESKTOP-U2HVTMF\MyPythonScripts\Jupyter\MAL Scraping\mal-scraping\topMAL.csv', index=True)
print('Exported to CSV')


#Standardize dates
#Standardize time to watch
#EDA: splitting genres