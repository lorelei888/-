import requests #放在最前面? 函數stock內?
 
# 使用者輸入
stock_no = input("請輸入股票代號（例如 2330）：")
 
# API URL
url = f"https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&stockNo={stock_no}"
 
# 發送請求
res = requests.get(url) #原始
data = res.json() #解析後的資料
 
# 判斷是否成功
if data["stat"] == "OK":
     print("前一天收盤價：",data["data"][-1][6]) #return render_template('stock.html', question=question, answer=answer)
else:
    print("查無資料，請確認股票代號或日期") #return render_template('stock.html', question=question, answer=answer)

