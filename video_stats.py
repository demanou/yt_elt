import requests
import json

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='./.env')

API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLE = "MrBeast"

url = f"https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

def get_playlist_id():
    try:
        # read data
        response = requests.get(url)

        response.raise_for_status()

        #print(response)

        data = response.json()
        #print(json.dumps(data, indent=4))

        channel_items = data['items'][0]
        channel_playlistid = channel_items['contentDetails']['relatedPlaylists']['uploads']
        return channel_playlistid
    except requests.exceptions.RequestException as e:
        raise e

if __name__ == "__main__":
    # channel playlist id
    print(f"Channel playlist Id : {get_playlist_id()}")
