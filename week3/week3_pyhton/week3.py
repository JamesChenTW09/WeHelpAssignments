import urllib.request as req
import json
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with req.urlopen(src) as response:
    data = json.load(response)

data = data["result"]["results"]

with open("data.csv",mode="w",encoding="utf-8")as file:
          for datas in data:
              stitle = datas["stitle"]
              address = datas["address"][5:8]
              longitude = datas["longitude"]
              files = "https://"+datas["file"].split("https://")[1]
              file.write(stitle+","+ address +","+longitude+","+files+"\n")