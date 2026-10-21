import argparse
import json
import sys

import requests

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "X-XSS-Protection",
    "Referrer-Policy",
    "Permissions-Policy",
    "Cross-Origin-Opener-Policy",
    "Cross-Origin-Embedder-Policy",
    "Cross-Origin-Resource-Policy"
]

def check_headers(target_url: str) -> str:
    print(f"[*] Checking headers for: {target_url}")
    result = {
        "url": target_url,
        "status": "error",
        "missing_headers": [],
        "present_headers": {}
    }

    try:
            response= requests.get(target_url, timeout=10, allow_redirects=True)
            result["status"] = "success"
            result["status_code"] = response.status_code

            for header in SECURITY_HEADERS:
                found = False
                for h_key, h_val in response.headers.items():
                     result["present_headers"][header] = h_val
                     found = True
                     break

            if not found:
                 result["missing_headers"].append(header)

    except requests.exceptions.RequestException as e:
        result["error_message"] = str(e)
        print(f"[-] Error connecting to {target_url}: {e}")

    return result

def main():
    parser = argparse.ArgumentParser(descripton="SecOps HTTP Security Headers Checker")
    parser.add_argument("-i", "--input", default="targets.txt", help="Path to file with URLs")
    parser.add_argument("-o", "--output", default="security_report.json", help="Path to output JSON report")
    args = parser.parse_args()

    try:
         with open(args.input, "r") as f:
              urls = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    except FileNotFoundError:
         print(f"[-] Error: Input file '{args.input}' not found.")
         sys.exit(1)

    report_data = []
    for url in urls:
         report_data.append(check_headers(url))

    with open(args.output, "w") as f:
         json.dump(report_data, f, indent=4)

    print(f"\n[+] Security audit report saved to: {args.output}")

if __name__ == "__main__":
    main()