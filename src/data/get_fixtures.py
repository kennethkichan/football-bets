import http.client
import sys
from dotenv import load_dotenv
import os
import json
import pandas as pd
from datetime import datetime

load_dotenv()

source_path = '../data/raw/fixtures.csv'

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': os.getenv("API_KEY")
    }

league_id = int(os.getenv("LEAGUE_ID"))

# If arguments exist
if len(sys.argv) > 1:
    arg0 = sys.argv[1] if len(sys.argv) > 1 else int(os.getenv("LEAGUE_ID"))
    arg1 = sys.argv[2] if len(sys.argv) > 1 else 'next'
    arg2 = sys.argv[3] if len(sys.argv) > 1 else '10'


def get_fixtures(id=league_id, var='next', num=10):
    """
    Get fixture data for next x games or last x games by League ID

    Parameters
    ----------
    id : int
        League ID, defaults to EPL
    var : str
        Enter 'next' for next coming games, 'last' for previous games, defaults to 'next'.
        Enter 'season' for entire season
    num : int
        Get number of games, defaults to 10.
        Enter season year when using season, e.g. 2021
   
    Example
    ----------
    get_fixtures(39, 'next', 10)
    """
    if var == 'next':
        req = "/fixtures?league={lid}&next={n}".format(lid=id, n=num)
    if var == 'last':
        req = "/fixtures?league={lid}&last={n}&status=ft".format(lid=id, n=num)
    if var =='season':
        req = "/fixtures?league={lid}&season={n}&status=ft".format(lid=id, n=num)
    conn.request("GET", req, headers=headers)

    res = conn.getresponse()
    data = res.read()
    conn.close()
    
    return data.decode("utf-8")

def write_fixtures():
    """
    Runs get_fixtures() and defaults to next 10 games
    """
    j = get_fixtures(39,'next',10)

    # Convert to json dict
    data = json.loads(j)

    df_source = pd.read_csv(source_path)

    df_target = pd.DataFrame()

    # Iterate response to store into df_source
    for res in data['response']:
        df = pd.DataFrame()
        df['fixture_id'] = [res['fixture']['id']]
        df['referee'] = [res['fixture']['referee']]
        df['timestamp'] = [res['fixture']['timestamp']] #utc
        df['venue_id'] = [res['fixture']['venue']['id']]
        df['home_id'] = [res['teams']['home']['id']]
        df['away_id'] = [res['teams']['away']['id']]
        df['created_datetime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df['modified_datetime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df_target = pd.concat([df_target,df])

    # Upsert based on fixture_id
    df_final = pd.concat([df_source, df_target[~df_target.fixture_id.isin(df_source.fixture_id)]])

    # Write to fixture
    df_final.to_csv(source_path, index=False)
