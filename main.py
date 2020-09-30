import time
import requests

Client_ID = "Input your client_id"
botToken = "Input your botToken"

def GetTwitchInfo(streamer_name, type=None):
    API_ENDPOINT = f"https://api.twitch.tv/helix/streams?user_login={streamer_name}"


    head = {
        'client-id': Client_ID,
        'authorization': 'Bearer ' + botToken
    }

    r = requests.get(url=API_ENDPOINT, headers=head)

    out = r.text
    if '"type":"live"' in out:
        if type == None:
            print(out)
        if type == "viewers":
            x = out.find("viewer_count")
            y = out.find("started_at")
            newout = out[x+14:y-2]
            print(newout)
        if type == "thumbnail":
            x = out.find("thumbnail_url")
            y = out.find("{width}")
            newout = out[x+16:y] + "1920x1080.jpg"
            print(newout)
        if type == "title":
            x = out.find("title")
            y = out.find("viewer_count")
            newout = out[x+8:y-3]
            print (newout)
        if type == "game_id":
            x = out.find("game_id")
            y = out.find("type")
            newout = out[x + 10:y - 3]
            print (newout)
    else:
        print("ERROR: could not get info or streamer inst streaming in the moment")
