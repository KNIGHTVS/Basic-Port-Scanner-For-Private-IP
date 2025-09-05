from flask import Flask, render_template, request, jsonify
import socket
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


app = Flask(__name__)

# 🔑 Gemini API Key (replace with your key)
GEMINI_API_KEY = api_key
genai.configure(api_key=GEMINI_API_KEY)

# Offline port info (fallback)
port_info = {
    139: {
        "service": "netbios-ssn",
        "risk": "Unauthorized access to files and printers",
        "mitigation": "Disable NetBIOS over TCP/IP or block the port via firewall"
    },
    445: {
        "service": "microsoft-ds",
        "risk": "SMB vulnerabilities (ransomware, worms)",
        "mitigation": "Disable SMBv1 and block unused SMB services"
    }
}

# 🔍 Function to scan ports


def scan_ports(host, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        try:
            result = sock.connect_ex((host, port))
            if result == 0:
                service = socket.getservbyport(port, "tcp") if port not in [
                    139, 445] else port_info[port]["service"]
                open_ports.append({
                    "port": port,
                    "service": service,
                    "risk": port_info.get(port, {}).get("risk", "Unknown risk"),
                    "mitigation": port_info.get(port, {}).get("mitigation", "No offline info available")
                })
        except:
            pass
        finally:
            sock.close()
    return open_ports

# ✅ Helper to get system’s private IP


def get_private_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Google DNS trick (no real traffic sent)
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

# 🏠 Homepage


@app.route("/", methods=["GET", "POST"])
def index():
    open_ports = []
    ip = get_private_ip()  # ✅ Now shows actual private IP (192.168.x.x)

    if request.method == "POST":
        ports = range(20, 1025)
        open_ports = scan_ports(ip, ports)

    return render_template("index.html", ip=ip, open_ports=open_ports)

# 📌 Route for Gemini details


@app.route("/details/<int:port>", methods=["GET"])
def details(port):
    try:
        prompt = f"""
        Explain the security risks, possible attacks, and step-by-step mitigation for open TCP port {port}.
        Divide the answer into 3 sections with headings:
        ### Risks:
        ### Mitigation:
        ### Steps:
        Keep it concise and professional.
        """
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return jsonify({"success": True, "details": response.text})
    except Exception as e:
        return jsonify({"success": False, "details": f"⚠️ Error fetching details: {str(e)}"})


if __name__ == "__main__":
    app.run(debug=True)
