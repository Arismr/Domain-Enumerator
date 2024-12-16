Subdomain Enumerator

Overview

This Python script is designed to perform subdomain enumeration for a given domain by leveraging DNS resolution and optional HTTP status checks. The results are saved to a file and displayed in real-time in the terminal.

This tool is beginner-friendly and demonstrates how a junior-level penetration tester might build a basic enumeration script. It includes DNS resolution, optional HTTP status checking, multithreading for efficiency, and error handling.

Features

DNS Resolution: Attempts to resolve subdomains to their IP addresses.

HTTP Status Checking (Optional): Checks if the resolved subdomain is active by sending an HTTP request.

Multithreading: Scans multiple subdomains simultaneously for faster results.

Error Handling: Handles DNS resolution failures and HTTP request timeouts gracefully.

Output: Results are saved to a CSV-style text file for further analysis.

Prerequisites

Python 3.x installed on your machine.

Basic understanding of Python scripting.

A subdomain wordlist (e.g., subdomains.txt).

Example wordlist:

www
mail
api
blog
test

Install the required Python libraries:

pip install requests

Usage

Run the script from the command line with the required arguments:

python subdomain_enumerator.py <domain> -w <wordlist> -o <output_file> -t <threads>

Arguments:

domain: The target domain (e.g., example.com).

-w / --wordlist: Path to the subdomain wordlist file (default: subdomains.txt).

-o / --output: Path to save the results (default: output.txt).

-t / --threads: Number of threads to use (default: 10).

Example:

python subdomain_enumerator.py example.com -w subdomains.txt -o results.txt -t 20

Sample Output

Terminal Output:

Starting scan on domain: example.com

Found: www.example.com (93.184.216.34) - HTTP 200
Found: api.example.com (93.184.216.34) - No HTTP Response
Found: mail.example.com (93.184.216.34) - HTTP 403

Results saved to results.txt

Saved File (results.txt):

Subdomain,IP,HTTP Status
www.example.com,93.184.216.34,200
api.example.com,93.184.216.34,N/A
mail.example.com,93.184.216.34,403

Design Notes

DNS Resolution: The socket.gethostbyname function is used to resolve subdomains.

HTTP Status Check: The requests library is used to send GET requests and fetch HTTP status codes.

Multithreading: The concurrent.futures.ThreadPoolExecutor class improves performance by running scans concurrently.

Error Handling: Handles scenarios where subdomains fail to resolve or HTTP requests time out.

Ethical Considerations

Use this tool only on domains you own or have explicit permission to test.

Ensure compliance with all applicable laws and ethical guidelines when performing penetration tests.

Enhancements and Next Steps

Add support for HTTPS status checking.

Implement retries for DNS resolution failures.

Include wildcard support for domain inputs.

Add verbose logging and progress bars for better UX.

License

This project is licensed under the MIT License. Feel free to modify and use this script for ethical and educational purposes.



