# RTX:Five★超抑鬱爬蟲連結
## Five諧音廢物。娛樂性搶購PChome的RTX3090，針對不講武德的上下架刷新機制進行多次更改
### v4.py為在不需要登入的電腦上進行新搶購連結刷新之用的程式，可以多開
### app.py和app-https.py功能是一樣的，可以接收v4裡面post出來的最新連結，啟動trader.py進行下單
### trader.py需要在selenium登入帳戶，因為需要結帳。app.py或者app-https.py僅僅接收第一個post（多了也沒用）
#### if you're using anaconda, you need to activate an environment with flask and other modules
#### modules used: BeautifulSoup4, Flask, json, re, requests, selenium