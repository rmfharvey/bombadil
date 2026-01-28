import requests
import json

with open("ids.json", "r") as f:
    ids = json.load(f)
    CLIENT_ID = ids["client_id"]
    CLIENT_SECRET = ids["client_secret"]

# Step 1: Get Access Token
token_url = "https://api.digikey.com/v1/oauth2/token"

token_data = {
    "code": auth_code,
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "redirect_uri": redirect_uri,
    "grant_type": "authorization_code",
}

token_response = requests.post(token_url, data=token_data)
tokens = token_response.json()
access_token = tokens["access_token"]
refresh_token = tokens["refresh_token"]
