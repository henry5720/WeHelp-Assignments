# 抓取ptt電影版網路原始碼(html)
from itertools import count
from turtle import title
import urllib.request as req
def getData(url): 
    # 建立 Request 物件,附加 Request.Headers 資訊
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    # print(data)
    
    # 解析原始碼,取得每篇文章標題
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    # print(root.title.string)
    titles=root.find_all("div", class_="title") # 尋找class="title"的div標籤
    # print(titles)
    for i in titles:
        if i.a != None:
            print(i.a.string)
    nextLink=root.find("a", string="‹ 上頁")
    return nextLink["href"]
# 抓取一個頁面標題(先呼叫函式 > 再用回傳值跟新網址 ps.以此為loop)
pageUrl="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<3:
    pageUrl="https://www.ptt.cc"+getData(pageUrl)
    count+=1