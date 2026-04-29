from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/stock")
def get_stock():
    stock_no = request.args.get("stockNo", "2330")  # 從 URL 參數取得
    date = datetime.now().strftime("%Y%m01")

    url = f"https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={date}&stockNo={stock_no}"

    try:
        res = requests.get(url, timeout=10)
        data = res.json()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    if data.get("stat") == "OK" and data.get("data"):
        return jsonify({
            "stock": stock_no,
            "close": data["data"][-1][6]
        })
    else:
        return jsonify({"error": "查無資料"}), 404

if __name__ == "__main__":
    app.run()
