#!/usr/bin/env python3
import socket
import sys

def check_subdomain(domain, subdomain):
    """
    Attempt to resolve the full domain composed of subdomain + domain.
    Returns the IP address if found, otherwise None.
    """
    full_domain = f"{subdomain}.{domain}"
    try:
        ip = socket.gethostbyname(full_domain)
        return ip
    except socket.gaierror:
        return None

def enumerate_subdomains(domain):
    """
    Enumerates a list of common subdomains for the given domain.
    Prints and returns any subdomains that successfully resolve.
    """
    # A basic list of common subdomains
    subdomains = ["www", "mail", "ftp", "ns1", "ns2", "blog", "webmail", "server", "smtp", "vpn"]
    found = {}
    for sub in subdomains:
        ip = check_subdomain(domain, sub)
        if ip:
            found[sub] = ip
            print(f"Found: {sub}.{domain} -> {ip}")
    if not found:
        print("No common subdomains found.")
    return found

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: domain_enumerator.py <domain>")
        sys.exit(1)
    target_domain = sys.argv[1]
    print(f"Enumerating subdomains for: {target_domain}")
    enumerate_subdomains(target_domain)
