import http.client
import sys
from dotenv import load_dotenv
import os

load_dotenv()

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': os.getenv("API_KEY")
    }

league_id = int(os.getenv("LEAGUE_ID"))

def get_fixtures(id=league_id, nxt='next', games=10):
    """
    Parameters
    ----------
    id : int
        League ID, default to EPL
    nxt : str
        Enter 'next' for next coming games, 'last' for previous games, default to 'next'
    games : int
        Get number of games, default to 10
    """
    if nxt == 'next':
        req = "/fixtures?league={lid}&next={g}".format(lid=id, g=games)
    if nxt == 'last':
        req = "/fixtures?league={lid}&last={g}&status=ft".format(lid=id, g=games)

    # conn.request("GET", req, headers=headers)

    # res = conn.getresponse()
    # data = res.read()

    # print(data.decode("utf-8"))
    print(req)

get_fixtures(league_id)