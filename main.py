from scanner.recon import recon
from scanner.xss_scanner import scan_xss
from scanner.sqli_scanner import scan_sqli
from scanner.headers_check import check_headers

print("=== Bug Bounty Automation Tool ===")

target = input("Enter target URL (example: http://testphp.vulnweb.com): ")

report = []
report.append(f"Target: {target}\n")

if recon(target):

    if scan_xss(target):
        print("[!] XSS Vulnerability Found")
        report.append("Reflected XSS: FOUND")
    else:
        report.append("Reflected XSS: NOT FOUND")

    if scan_sqli(target):
        print("[!] SQL Injection Vulnerability Found")
        report.append("SQL Injection: FOUND")
    else:
        report.append("SQL Injection: NOT FOUND")

    missing = check_headers(target)
    if missing:
        print("[!] Missing Security Headers:", missing)
        report.append("Missing Security Headers:")
        for h in missing:
            report.append(f" - {h}")
    else:
        report.append("All Security Headers Present")

    with open("reports/report.txt", "w") as file:
        for line in report:
            file.write(line + "\n")

    print("\n[+] Scan Completed")
    print("[+] Report Generated: reports/report.txt")
