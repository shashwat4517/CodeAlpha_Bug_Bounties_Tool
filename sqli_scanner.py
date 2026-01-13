import requests

def scan_sqli(url):
    payload = "' OR '1'='1"
    test_url = f"{url}?id={payload}"

    try:
        response = requests.get(test_url)
        errors = ["sql", "syntax", "mysql", "database"]

        for error in errors:
            if error in response.text.lower():
                return True
        return False
    except:
        return False
