import requests

def scan_xss(url):
    payload = "<script>alert(1)</script>"
    test_url = f"{url}?q={payload}"

    try:
        response = requests.get(test_url)
        if payload in response.text:
            return True
        else:
            return False
    except:
        return False
