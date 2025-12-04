# 🛡️ NEXUS WEB HONEYPOT & THREAT COSOLE

![LOGO](https://github.com/user-attachments/assets/1fffe8e3-d926-4909-bc32-5a246fe406d6)


## 🚀 Overview
**Nexus Web Honeypot** is a deceptive, low‑interaction attack observation system disguised as a corporate login portal (**Apex Solutions Employee/Admin Access Portal**).  
It silently logs malicious activity, identifies attack trends, and displays them in a futuristic, real-time threat dashboard.

Perfect for:
- Cybersecurity portfolios  
- Threat intelligence research  
- Honeypot experiments  
- Hydra/Brute-force analysis  
- Network attack visualization  

---

## ✨ Features

### 🎭 **Deceptive Login Portal**
A fully realistic corporate login page designed to lure:
- Botnets  
- Credential stuffers  
- Hydra attackers  
- Script kiddies  

### 📝 **Full Attack Logging**
Captured per attempt:
- IP Address  
- Submitted Username & Password  
- User-Agent  
- Timestamp  
- URL Path  
- Query/body payloads  

### 🧠 **Attack Classification Engine**
Automatically detects:

| Attack Type | Detection Method | Examples |
|------------|------------------|----------|
| **SQL Injection (SQLi)** | Regex & signature matching | `' OR '1'='1`, `UNION SELECT`, `--` |
| **XSS Payloads** | Script tag + event handler detection | `<script>alert(1)</script>` |
| **Brute Force** | High-frequency failed logins | Hydra, Burp Intruder |

### 🛰️ **Cyberpunk-Themed Dashboard**
Live threat command center showing:
- Total threats
- Top attacker IPs
- Attack velocity graph (Chart.js)
- Live threat feed
- Geographic attack map (Leaflet.js)
- Payload frequency charts

### 💥 **Hydra Compatible**
Honeypot gracefully handles large brute-force sequences:

```
hydra -l admin -P wordlist.txt 127.0.0.1 http-post-form "/admin:username=^USER^&password=^PASS^:Incorrect username or password"
```

### 🧪 **WSL ↔ Windows Compatible**
- Windows runs Flask honeypot  
- WSL simulates attacker using Hydra  
- Dashboard updates in real-time  

---

## 🏗️ System Architecture

```
     Attacker (Hydra/Bots)
                 │
                 ▼
       ┌──────────────────┐
       │  Fake /admin     │
       │  Login Portal     │
       └──────────────────┘
                 │
                 ▼
       ┌──────────────────┐
       │ Flask Engine     │
       │ • Log parser     │
       │ • Pattern matcher│
       └──────────────────┘
                 │
                 ▼
       ┌──────────────────┐
       │  SQLite Database │
       └──────────────────┘
                 │
                 ▼
       ┌──────────────────┐
       │ Command Center   │
       │  Dashboard       │
       └──────────────────┘
```

---

## 📁 Project Structure

```
🌐 Nexus Web Honeypot
├── 📁 templates/
│   ├── about.html
│   ├── base_public.html
│   ├── dashboard_base.html
│   ├── dashboard_command.html
│   ├── dashboard_database.html
│   ├── dashboard_feed.html
│   ├── dashboard_login.html
│   ├── dashboard_profile.html
│   ├── dashboard.html
│   ├── index.html
│   ├── login.html
│   └── services.html
│
├── 🐍 app.py
├── 🗄️ honeypot.db
├── 🧪 populate_data.py
├── 📘 README.md
├── 📦 requirements.txt
├── 🔍 test_auth.py
└── 🔍 test_honeypot.py

```

---

## ⚙️ Installation

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/nexus-web-honeypot
cd nexus-web-honeypot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🧪 Run the Honeypot

```bash
python app.py
```

Flask listens on:
```
http://0.0.0.0:5000
```

---

## 🧨 Simulate Attacks (Hydra)

### 1. Get Windows Host IP (from WSL)
```bash
ip route show | grep default
```

### 2. Attack the Honeypot
```bash
hydra -l admin -P passwords.txt <WINDOWS-IP> http-post-form "/admin:username=^USER^&password=^PASS^:Incorrect username or password"
```

The honeypot logs every attempt.

---

## 🖥 Dashboard Access

### **Dashboard Login**
```
http://localhost:5000/dashboard-login
```

**Credentials:**
- Username: `operator`
- Password: `nexus-secure-882a`

Features:
- Real-time live feed  
- Geo attack map  
- Top attackers  
- Payload breakdown  
- Alerts  

---

## 🧪 Optional: Populate Dummy Data

```bash
python populate_data.py
```

Shows the dashboard fully populated instantly.

---

## 🖼 Screenshots (placeholders)

### Fake Website
<img width="2311" height="1746" alt="Screenshot 2025-12-04 at 19-44-18 Apex Solutions" src="https://github.com/user-attachments/assets/aa56d585-10d0-4b5a-8175-af8aa8d37a38" />

### Login Portal (HoneyPot)
<img width="2311" height="1520" alt="Screenshot 2025-12-04 at 19-46-22 Login - Apex Solutions" src="https://github.com/user-attachments/assets/bc6077df-9670-46d2-a4cc-1265fdc3d3d0" />

### HoneyPot-Management-Daashboard
<img width="2311" height="1520" alt="Screenshot 2025-12-04 at 19-45-18 Nexus Security Access" src="https://github.com/user-attachments/assets/cf2a889d-c11d-41a6-82c1-55e7aa616918" />

### Command Center  
<img width="2311" height="1520" alt="Screenshot 2025-12-04 at 19-45-49 Nexus SOC Command" src="https://github.com/user-attachments/assets/b9338d48-3503-49e1-9fda-76073e22e2d7" />

### Live Threat Feed  
<img width="2311" height="1520" alt="Screenshot 2025-12-04 at 19-45-56 Nexus SOC Command" src="https://github.com/user-attachments/assets/87514a72-e7f0-4bfe-b7a0-fb9f7af79de0" />

### Attacker Database
<img width="2311" height="1520" alt="Screenshot 2025-12-04 at 19-46-02 Nexus SOC Command" src="https://github.com/user-attachments/assets/2ac71ad2-2708-4897-9cf9-01422f873ac0" />

### Detailed Profile Review
<img width="2311" height="1520" alt="Screenshot 2025-12-04 at 20-03-28 Nexus SOC Command" src="https://github.com/user-attachments/assets/aea5374b-626e-443e-91c1-b99fd70d120d" />


---

## ⚠️ Security Disclaimer
> **This project is STRICTLY for educational & research purposes.**  
> Do **NOT** deploy publicly or attempt attacks on systems without explicit permission.  
> The author assumes zero liability for misuse.

---

## 🚀 Future Roadmap
- SMTP email alerts  
- Automated attacker fingerprinting  
- CSV / JSON export  
- High-interaction fake admin shell  
- ML-based anomaly detection  

---

## 📜 License
Released under the **MIT License** — free for personal & commercial use.

---

**For Dockerized Version Visit** --> https://github.com/AkhilBangaru/Nexus_Web_HoneyPot_Docker_Version/

## ⭐ Final Note
If you like this project, consider giving it a **GitHub star ⭐** and contributing enhancements!

