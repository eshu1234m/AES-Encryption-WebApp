# 🔐 AES Encryption Web App

A simple web-based tool for AES encryption and decryption using Python (Flask), HTML, and CSS.

---

## 🚀 Features

- AES encryption and decryption (128/192/256-bit key using SHA-256)
- Secure padding and Base64 encoding
- User-friendly interface
- Built with Flask (Python), HTML, and CSS
- Lightweight and easy to run locally

---

## 📷 Screenshots

> Add screenshots of your web app here!

---

## 📁 Project Structure

aes_web_app/ ├── app.py ├── templates/ │ └── index.html ├── static/ │ └── style.css


---

## 🛠️ Requirements

- Python 3.x  
- Flask  
- pycryptodome  

Install dependencies:

```bash
pip install flask pycryptodome
```
## ▶️ How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/AES-Encryption-WebApp.git
cd AES-Encryption-WebApp
```
2.Install dependencies:
```bash
pip install flask pycryptodome
```
3.Run the Flask app:
```bash
python app.py
```
4.Open your browser and go to:
```bash
(http://127.0.0.1:5000)
```
## 🧪 Sample Test Inputs

1. **Key:** `myStrongPass123!`  
   **Text:** `Confidential: The meeting is scheduled at 10:00 AM on Monday.`

2. **Key:** `SecureKey456@`  
   **Text:** `The OTP for your transaction is 984512. Do not share it.`

3. **Key:** `Encrypt@789`  
   **Text:** `Project deadline is moved to Friday. Update your progress.`

4. **Key:** `AESKeyTest321#`  
   **Text:** `Login credentials: user123, pass@456. Keep this private.`

5. **Key:** `SafeKey999!`  
   **Text:** `This message will self-destruct in 10 seconds. 🔒`

> Use the same key to decrypt the encrypted output.




