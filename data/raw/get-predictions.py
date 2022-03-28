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

def is_intstring(s):
    """
    Check if input argument is string
    
    Parameters
    ----------
    s = Some integer
    """
    try:
        int(s)
        return True
    except ValueError:
        return False
for arg in sys.argv[1]:
    if not is_intstring(arg):
        sys.exit("All arguments must be integers. Exit.")

fixture_id = int(sys.argv[1])

def get_pred(id):
    """
    Parameters
    ----------
    id : int
        Fixture ID

    Returns
    ----------
    results : str
        Prediction results
    """
    
    req = "/predictions?fixture={id}".format(id=fixture_id)
    print('Requesting Fixture ID', req)

    try:
        conn.request("GET", req, headers=headers)

        res = conn.getresponse()
        data = res.read()
        #print(data.decode("utf-8"))
        return data.decode("utf-8")
    except ValueError:
        return False

get_pred(fixture_id)