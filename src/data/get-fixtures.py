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
arg0 = sys.argv[1] if len(sys.argv) > 1 else int(os.getenv("LEAGUE_ID"))
arg1 = sys.argv[2] if len(sys.argv) > 1 else 'next'
arg2 = sys.argv[3] if len(sys.argv) > 1 else '10'


def get_fixtures(id=league_id, nxt='next', games=10):
    """
    Parameters
    ----------
    id : int
        League ID, defaults to EPL
    nxt : str
        Enter 'next' for next coming games, 'last' for previous games, defaults to 'next'
    games : int
        Get number of games, defaults to 10
   
    Example
    ----------
    get_fixtures(39, 'next', 10)
    """
    if nxt == 'next':
        req = "/fixtures?league={lid}&next={g}".format(lid=id, g=games)
    if nxt == 'last':
        req = "/fixtures?league={lid}&last={g}&status=ft".format(lid=id, g=games)

    conn.request("GET", req, headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

get_fixtures(arg0, arg1, arg2)