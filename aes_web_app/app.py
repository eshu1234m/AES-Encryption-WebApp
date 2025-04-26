
from flask import Flask, render_template, request
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import hashlib

app = Flask(__name__)

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    mode = ""
    if request.method == 'POST':
        key = hashlib.sha256(request.form['key'].encode()).digest()
        text = request.form['text']
        mode = request.form['mode']

        if mode == 'encrypt':
            cipher = AES.new(key, AES.MODE_ECB)
            ct_bytes = cipher.encrypt(pad(text).encode('utf-8'))
            result = base64.b64encode(ct_bytes).decode('utf-8')
        elif mode == 'decrypt':
            cipher = AES.new(key, AES.MODE_ECB)
            ct = base64.b64decode(text)
            result = cipher.decrypt(ct).decode('utf-8').strip()

    return render_template('index.html', result=result, mode=mode)

if __name__ == '__main__':
    app.run(debug=True)
