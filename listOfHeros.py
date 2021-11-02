import requests, json, time, os
import pandas as pd

# get up to date info on game heroes
def get_hero_stats():
    data = requests.get("https://api.opendota.com/api/heroStats").json()
    pd.DataFrame(data).to_csv("hero_stats.csv", sep=",")
    with open('hero_stats.json','w') as outfile:
        json.dump(data, outfile)

get_hero_stats()