from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def stock():
    result = None

    if request.method == "POST":
        stock_no = request.form.get("stock_no")

        url = f"https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&stockNo={stock_no}"

        try:
            res = requests.get(url, timeout=10)
            res.raise_for_status()
            data = res.json()

        except requests.exceptions.RequestException as e:
            result = f"連線或請求錯誤：{e}"
            return render_template("stock.html", result=result)

        except ValueError:
            result = "回傳資料格式錯誤（不是有效的 JSON）"
            return render_template("stock.html", result=result)

        # 判斷資料
        if data.get("stat") == "OK" and data.get("data"):
            try:
                latest_day = data["data"][-1]
                close_price = latest_day[6]
                result = f"股票 {stock_no} 最新收盤價：{close_price}"
            except (IndexError, TypeError):
                result = "資料格式異常，無法解析收盤價"
        else:
            result = "查無資料，請確認股票代號或是否有交易資料"

    return render_template("stock.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
