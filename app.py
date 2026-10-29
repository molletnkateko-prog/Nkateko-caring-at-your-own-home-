from flask import Flask, request
import os
app = Flask(__name__)

@app.route("/")
def home():
    return "Nkateko Caring LIVE - All 9 Provinces!"

@app.route("/webhook", methods=["GET","POST"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == "nkateko123":
            return request.args.get("hub.challenge")
        return "fail"
    return "ok", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
