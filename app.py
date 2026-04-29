import requests
from datetime import datetime

stock_no = input("請輸入股票代號（例如 2330）: ")
date = datetime.now().strftime("%Y%m01")  # 當月第一天

url = f"https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={date}&stockNo={stock_no}"

try:
    res = requests.get(url, timeout=10)
    data = res.json()
except Exception as e:
    print("請求失敗：", e)
    exit()

if data.get("stat") == "OK" and data.get("data"):
    print("最新收盤價：", data["data"][-1][6])
else:
    print("查無資料，請確認股票代號")
