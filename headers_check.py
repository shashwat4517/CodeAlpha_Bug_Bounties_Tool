import requests

def check_headers(url):
    response = requests.get(url)

    security_headers = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-XSS-Protection",
        "Strict-Transport-Security"
    ]

    missing_headers = []

    for header in security_headers:
        if header not in response.headers:
            missing_headers.append(header)

    return missing_headers
