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

conn.request("GET", "/fixtures?live=all", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
