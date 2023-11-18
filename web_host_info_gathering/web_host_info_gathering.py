import requests
import socket
from bs4 import BeautifulSoup
import dns.resolver
import whois
import ssl
import shodan

# Define the target host
target_host = "Replace with Target IP"

# Define the Shodan API key
shodan_api_key = "Replace with key"

# Define the target URL
target_url = f"https://{target_host}"

# HTTP Request to get server information
response = requests.get(target_url)
headers = response.headers
server_version = headers.get("Server", "N/A")

# Socket Programming to gather banner information
try:
    target_port = 443  # Assuming HTTPS
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))
    banner = client.recv(1024)
    client.close()
except Exception as e:
    banner = "N/A"

# BeautifulSoup to parse HTML content
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")
page_title = soup.title.string.strip()

# DNS Query to gather DNS information
try:
    dns_resolver = dns.resolver.Resolver()
    result = dns_resolver.resolve(target_host, "A")
    ip_addresses = [ip.address for ip in result]
except Exception as e:
    ip_addresses = []

# WHOIS lookup for domain information
try:
    domain_info = whois.whois(target_host)
    registrar = domain_info.registrar if domain_info else "N/A"
except Exception as e:
    registrar = "N/A"

# SSL/TLS Information
try:
    ssl_info = ssl.get_server_certificate((target_host, target_port))
    ssl_subject = ssl.cert_subject(ssl_info)
    ssl_issuer = ssl.cert_issuer(ssl_info)
except Exception as e:
    ssl_subject = "N/A"
    ssl_issuer = "N/A"

# Shodan functionality
try:
    api = shodan.Shodan(shodan_api_key)
    shodan_host = api.host(target_host)
    shodan_ports = shodan_host.get("ports", "N/A")
    shodan_services = shodan_host.get("data", [])
except Exception as e:
    shodan_ports = "N/A"
    shodan_services = []

# Print gathered information
print(f"Target Host: {target_host}")
print(f"Server Version: {server_version}")
print(f"Banner Information: {banner}")
print(f"Page Title: {page_title}")
print(f"IP Addresses: {', '.join(ip_addresses)}")
print(f"Domain Registrar: {registrar}")
print(f"SSL/TLS Subject: {ssl_subject}")
print(f"Shodan Ports: {shodan_ports}")
print(f"Shodan Services: {shodan_services}")

# HTTP Headers
for key, value in headers.items():
    print(f"HTTP Header: {key}: {value}")

# HTTP Status Codes
print(f"HTTP Status Code: {response.status_code}")

# Security Headers
security_headers = [
    "X-Content-Security-Policy",
    "Strict-Transport-Security",
    # Add more security headers as needed
]

for header in security_headers:
    header_value = headers.get(header, "N/A")
    print(f"Security Header {header}: {header_value}")

# Response Time Analysis
response_time = response.elapsed.total_seconds()
print(f"Response Time: {response_time} seconds")
