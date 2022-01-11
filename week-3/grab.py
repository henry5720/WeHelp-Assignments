import urllib.request as request #
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)
# print(data)
clist=data["result"]["results"]
# print(clist)
# print(clist[0]["stitle"])
# print(clist[0]["address"][5:8])
# print("htpps://"+clist[0]["file"].split("https://")[1])
with open("data.csv", mode="w", encoding="UTF-8-Sig") as csvfile:
    # 景點名稱,區域,經度,緯度,第一張圖檔網址
    for i in clist:
        csvfile.write(i["stitle"]+",")
        csvfile.write(i["address"][5:8]+",")
        csvfile.write(i["longitude"]+",")
        csvfile.write(i["latitude"]+",")
        img_src="https://"+i["file"].split("https://")[1]
        csvfile.write(img_src+"\n")



