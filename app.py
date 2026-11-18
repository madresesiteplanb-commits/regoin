from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Render Region Test</title>
        <style>
            body {
                background: #101827;
                color: white;
                font-family: Arial;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 90vh;
                text-align: center;
            }
            .box {
                background: #1e293b;
                padding: 35px;
                border-radius: 18px;
            }
            h1 { color: #4ade80; }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>سایت با موفقیت بالا آمد!</h1>
            <p>UP AND RUNNING</p>
            <p>Render Region Test</p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
