import requests

def stock():
    stock_no = input("請輸入股票代號（例如 2330）：")
    url = f"https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&stockNo={stock_no}"
  
    res = requests.get(url)
    data = res.json()

    if data["stat"] == "OK":
        print("前一天收盤價：", data["data"][-1][6])
    else:
      print("查無資料，請確認股票代號或日期")
      
stock()
