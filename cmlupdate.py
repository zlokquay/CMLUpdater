"""
Written By: Zach Taylor
Open to use by any who find it, just change out/add to the players list and off you go.

Simple python3 script to update me and a few choice players on CrystalMathLabs.
Using python.requests to easily GET the endpoint from CML, and print the response
code out to the terminal. If it is any number except good (1), wait 15 seconds and try again.

Oldschool Runescape hiscores are a little funky right now, so having multiple tries is required
for optimal use. Once a patch comes out, I'll update to fix this.
"""

import requests, time

players = ["GFHL", "Kaznae_btw", "lron_coop", "Xoivex", "Karamja_Only", "Rive_r", "Pipinel"]
url = "https://crystalmathlabs.com/tracker/api.php?type=update&player="

def getUpdate(player_name):
    r = requests.get(url + player_name)
    print(player_name + ": code " + r.text)
    if r.text != "1":
        time.sleep(15)
        getUpdate(player_name)

def run():
    for player in players:
        getUpdate(player)

run()