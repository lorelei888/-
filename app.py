import requests

def stock():
    # 使用者輸入
    stock_no = input("請輸入股票代號（例如 2330）：")

    # API URL
    url = f"https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&stockNo={stock_no}"

    try:
        # 發送請求
        res = requests.get(url, timeout=10)
        res.raise_for_status()  # HTTP 錯誤會丟出例外

        data = res.json()  # 解析 JSON

    except requests.exceptions.RequestException as e:
        print("連線或請求錯誤：", e)
        return
    except ValueError:
        print("回傳資料格式錯誤（不是有效的 JSON）")
        return

    # 判斷資料狀態與內容
    if data.get("stat") == "OK" and data.get("data"):
        try:
            latest_day = data["data"][-1]  # 最新交易日
            close_price = latest_day[6]   # 收盤價（第 7 欄）

            print("最新交易日收盤價：", close_price)

        except (IndexError, TypeError):
            print("資料格式異常，無法解析收盤價")
    else:
        print("查無資料，請確認股票代號或是否有交易資料")

# 執行
stock()
