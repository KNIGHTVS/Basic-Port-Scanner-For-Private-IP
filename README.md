# 🔍 Basic Port Scanner for Private IP

A simple **Flask-based web application** that scans open ports on devices within a private IP range.  
This tool is made for **educational and local network testing purposes only** ⚡.

---

## 📌 Features

- Scan private IP addresses for open ports
- Simple web interface (HTML + Flask)
- Lightweight and easy to run locally
- Uses **Google Gemini API** for additional functionality

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/KNIGHTVS/Basic-Port-Scanner-For-Private-IP.git
cd Basic-Port-Scanner-For-Private-IP
```

### 2. Create a virtual environment (recommended)

For Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

For Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install requirements

Make sure you have pip updated:
```bash
pip install --upgrade pip
```

Then install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🔑 Setting up Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey) and create an API key.
2. Inside the project folder, create a file named `.env`.
3. Add your Gemini API key like this:

```
GEMINI_API_KEY=your_api_key_here
```

4. Make sure `.env` is not shared (it's already in `.gitignore`).

---

## 🚀 Running the App Locally

For Linux / macOS:
```bash
python3 PortScann.py
```

For Windows:
```powershell
python PortScann.py
```

By default, the app runs on:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📂 Project Structure

```
Basic-Port-Scanner-For-Private-IP/
│── PortScann.py          # Main Flask app
│── requirements.txt      # Python dependencies
│── .env.example          # Example for Gemini API key
│── templates/
│     └── index.html      # Frontend page
│── static/               # (Optional) CSS/JS files
```

---

## ⚠️ Important Notes

- This project is intended for educational purposes only.
- Always run scans on your own private/local network.
- Unauthorized port scanning may be illegal. 🚨
- If ports do not scan properly, check your firewall settings.

### ⚡ Why you can't deploy on Render/Vercel:
- These platforms don't allow scanning private/local IP addresses.
- Since the app works only on LAN/localhost, it must be run on your own machine.

---

## 🛠️ Requirements

- Python 3.8+
- Flask
- python-dotenv
- google-generativeai

---

## 👤 Author

**Vivek (KNIGHTVS)**  
📌 [GitHub Profile](https://github.com/KNIGHTVS)
