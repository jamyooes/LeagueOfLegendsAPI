from config import API_KEY, champion, champion_json
import json
from readable_json import champ_stats_readable
import urllib.request, json 

with urllib.request.urlopen(champion) as url:
    data = json.load(url)
    # print(data)

"""
id : Has the Name of the champion
key : Some internal key number
name : Name again
title : Champion title/nickname
image : Image- not too useful
skins : Skins
lore : Lore
blurb : Truncated Version of the lore
allytips : empty
enemytips : empty 
tags : Class type like mage / assassins
partype : Resource type
info : Some arbitrary numbers
stats : Stats -> Useful
spells : Spells and tooltips -> Useful
passive : Indicator on hover
recommended : Empty
"""
test_field = "recommended"
datatum = data["data"]["Katarina"]
# print(datatum)

champ_stats_readable(datatum)
# for i in datatum:
#     print(datatum[i])

# for i in data:
#     print(i)
#     print()
#print(data[""])
