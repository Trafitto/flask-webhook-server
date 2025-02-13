from flask import Flask, request
from wakeonlan import send_magic_packet
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

HOOK_ID = os.getenv("HOOK_ID")
MAC_ADDRESS = os.getenv("MAC_ADDRESS")

@app.route(f"/webhook/{HOOK_ID}", methods=["POST"])
def webhook():
    # data = request.json
    print(f"Received webhook")
    send_magic_packet(MAC_ADDRESS)
    
    return 204, None

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)