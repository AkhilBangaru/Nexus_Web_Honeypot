import requests

def test_auth_bypass():
    url = "http://localhost:5000/nexus-security-view-882a"
    # Use a fresh session (no cookies)
    s = requests.Session()
    r = s.get(url, allow_redirects=False)
    
    print(f"Status Code: {r.status_code}")
    if r.status_code == 302:
        print(f"Redirect Location: {r.headers.get('Location')}")
        if '/dashboard-login' in r.headers.get('Location'):
            print("Auth Check: PASSED (Redirected to login)")
        else:
            print("Auth Check: FAILED (Redirected elsewhere)")
    elif r.status_code == 200:
        print("Auth Check: FAILED (Access granted without login)")
    else:
        print(f"Auth Check: UNKNOWN (Status {r.status_code})")

if __name__ == "__main__":
    test_auth_bypass()
