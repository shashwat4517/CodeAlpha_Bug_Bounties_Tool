import requests

def recon(target):
    print("\n[+] Reconnaissance Started")
    try:
        response = requests.get(target, timeout=5)
        print("[+] Target is Live")
        print("[+] Status Code:", response.status_code)
        print("[+] Server:", response.headers.get("Server"))
        return True
    except:
        print("[-] Target is not reachable")
        return False
