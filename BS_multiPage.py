#連線網路取得原始資料
import urllib.request as req

def getData(url):
    #建立一個Request物件，附加Request Headers的資訊，Headers的資訊可以從F12=>網路=>要求標題中尋找
    #在request中又以User-Agent和cookie最為重要
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "cookie": "cookie: _ga=GA1.2.2039479191.1646595094; _gid=GA1.2.1186217690.1646595094; __cf_bm=4SWsqeT.pIxKYkclTHLODJlH3TtGvw9eLM6st0P6ieU-1646597802-0-ARdrsfpir/csqLwuh5aUJtixMSrOWvnJO+CD5x2/Pka5m04tSOW9SqhBNX46ctb6XzneNT6l8JCImCK+o6XxgLE=; _gat=1; over18=1"
    })

    #利用Request物件打開網址
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8") #如果沒有用request物件來打開網頁，很容易會被擋掉，因為request物件會帶有一些使用者資訊

    #解析原始碼，取得內文
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title") #尋找所有class="title"的標籤
    for title in titles:
        if title.a != None:
            print(title.a.string) #如果div底下還有包其他的tag，可以直接用.往下取，然後如果要取文字就直接打.string
