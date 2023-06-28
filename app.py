import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'LazyDeveloper'

os.system("git clone https://kherachohan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@github.com/kherachohan/LazyPrincessV2 okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
