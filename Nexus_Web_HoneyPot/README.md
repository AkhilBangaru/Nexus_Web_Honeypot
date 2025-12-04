# Nexus Web Honeypot

## 1. Project Title
**Nexus Web Honeypot & Threat Dashboard**

## 2. Description
Nexus Web Honeypot is a lightweight, low-interaction web honeypot designed to mimic a vulnerable corporate login portal ("Apex Solutions"). It silently logs unauthorized access attempts, captures credentials, and analyzes attack patterns (SQL Injection, XSS, Brute Force). It features a real-time, futuristic "Command Center" dashboard for monitoring threats as they happen.

## 3. Features
-   **Deceptive Login Portal**: A realistic-looking "Apex Solutions" employee login page designed to entice attackers.
-   **Attack Logging**: Captures IP address, username, password, User-Agent, and timestamp of every login attempt.
-   **Threat Analysis**: Automatically detects and categorizes attacks:
    -   **SQL Injection (SQLi)**: Detects patterns like `' OR 1=1`, `UNION SELECT`.
    -   **Cross-Site Scripting (XSS)**: Detects script tags and alert functions.
    -   **Brute Force**: Identifies repeated failed login attempts without specific payloads.
-   **Real-Time Dashboard**: A premium, cyberpunk-themed interface displaying:
    -   Total Threats Blocked
    -   Unique Attackers
    -   Top Attack Vector (SQLi, XSS, Brute Force)
    -   Live Attack Map (Leaflet.js)
    -   Attack Velocity Graph (Chart.js)
    -   Live Threat Feed
-   **Hydra Compatible**: Specifically designed to handle and log automated brute-force attacks from tools like Hydra.
-   **WSL & Windows Compatible**: Runs seamlessly on Windows and is accessible from WSL for penetration testing simulations.

## 4. Technology Stack
-   **Backend**: Python, Flask
-   **Database**: SQLite (`honeypot.db`)
-   **Frontend**: HTML5, CSS3 (Custom Dark/Neon Theme), JavaScript
-   **Visualization**: Chart.js (Graphs), Leaflet.js (Maps)
-   **Testing Tools**: Hydra (for brute-force simulation)

## 5. How It Works
1.  **The Trap**: The server exposes a login page at `/admin` (and `/`).
2.  **The Capture**: When an attacker submits the form, the backend (`app.py`) intercepts the request.
    -   It logs the credentials and metadata to the SQLite database.
    -   It analyzes the input for malicious signatures (SQLi, XSS).
    -   It returns a generic "Incorrect username or password" error to keep the attacker guessing (or a fake success message for specific "vulnerable" credentials).
3.  **The Monitoring**: The `/nexus-security-view-882a` dashboard polls the internal API (`/api/stats`) every 3 seconds to update the UI with the latest attack data without refreshing the page.

## 6. Installation Instructions

### Prerequisites
-   Python 3.x
-   Git (optional)

### Setup
1.  Clone or download this repository.
2.  Navigate to the project directory:
    ```bash
    cd web-honeypot
    ```
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 7. Data Population (Optional)
The project includes a `populate_data.py` script to fill the database with dummy attack data for testing purposes.

### Option A: Start Fresh (Clean Database)
By default, the honeypot starts with an empty database.
1.  Simply run `python app.py`.
2.  The database `honeypot.db` will be created automatically when the server starts.
3.  The dashboard will show 0 attacks until you perform some login attempts.

### Option B: Pre-fill with Dummy Data
If you want to see what the dashboard looks like with data immediately:
1.  Run the population script:
    ```bash
    python populate_data.py
    ```
2.  This will create `honeypot.db` and fill it with random attack logs (SQLi, XSS, Brute Force) from various countries.
3.  Then start the server: `python app.py`.

## 8. Exposing the Server
To make the honeypot accessible from other devices on your network (or from WSL), the Flask app is configured to listen on all interfaces (`0.0.0.0`).

In `app.py`, the run command is configured as:
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

## 9. Running Hydra from WSL
You can simulate a brute-force attack using Hydra from a WSL (Windows Subsystem for Linux) terminal.

### 1. Find your Windows IP
From your WSL terminal, run:
```bash
ip route show | grep default
```
The IP address shown (e.g., `172.x.x.x`) is your Windows host IP. Use this IP instead of `127.0.0.1` if `localhost` doesn't work.

### 2. Run the Attack
Use the following command (replace `127.0.0.1` with your Windows IP if needed):

```bash
hydra -l admin -P passwords.txt 127.0.0.1 http-post-form "/admin:username=^USER^&password=^PASS^:Incorrect username or password"
```

*Note: The honeypot is configured with a secure, random password. Hydra will likely report 0 valid passwords found. This is expected behavior—the goal is to log the attack attempts, not to grant access.*

## 10. WSL ↔ Windows Networking
-   **Windows Host**: Runs the Flask Honeypot.
-   **WSL Instance**: Acts as the "Attacker" machine.
-   **Connection**: WSL sees the Windows host as the default gateway. By binding Flask to `0.0.0.0`, we allow the WSL instance to connect to port 5000 on the Windows IP.

## 11. Usage Guide

### Accessing the Honeypot (The Trap)
-   **URL**: `http://localhost:5000/admin`
-   **Action**: Try to log in with any credentials. The system is designed to reject all common passwords to keep attackers engaged and logging their attempts.

### Accessing the Dashboard (The Monitor)
-   **URL**: `http://localhost:5000/dashboard-login`
-   **Credentials**:
    -   Username: `operator`
    -   Password: `nexus-secure-882a`
-   **Features**: Watch the counters and graphs update automatically as you perform attacks on the `/admin` page.

### Viewing Logs
-   Logs are stored in `honeypot.db`.
-   You can view them in the "Live Threat Feed" on the dashboard (`/nexus-feed`) or by inspecting the SQLite database directly.

## 12. Screenshots
*(Placeholders - Add actual screenshots of your dashboard here)*
-   **Login Page**: The fake corporate portal.
-   **Command Center**: The main dashboard view.
-   **Live Feed**: The scrolling list of attack attempts.

## 13. Security Disclaimer
> **⚠️ EDUCATIONAL PURPOSES ONLY**
> This project is intended for educational and research purposes only. Do not use this honeypot to entrap malicious actors without proper authorization and legal consultation. Do not use the attack tools (Hydra) on systems you do not own or have explicit permission to test. The author assumes no liability for misuse of this software.

## 14. Future Improvements
-   **Docker Support**: Containerize the application for easier deployment.
-   **Advanced Fingerprinting**: Better detection of automated scanners vs. human attackers.
-   **Email Alerts**: Integrate SMTP to send email notifications on high-severity alerts.
-   **Export Logs**: Add functionality to export logs to CSV/JSON.

## 15. License
This project is open-source and available under the **MIT License**.
