# Domain Enumerator

A lightweight domain enumerator tool written in Python for discovering common subdomains of a target domain. This project is designed for junior cybersecurity enthusiasts to understand basic domain enumeration concepts and to serve as a foundation for further development.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Features

- **Subdomain Discovery**: Enumerates a preset list of common subdomains (e.g., `www`, `mail`, `ftp`, etc.) by performing DNS lookups.
- **Simplicity**: Designed with minimal dependencies and straightforward logic, making it perfect for beginners.
- **Ease of Extension**: The codebase is organized and commented to allow easy modifications and enhancements.
- **Cross-Platform**: Runs on any system with Python 3 installed.

## Installation

### Prerequisites

- Python 3.x must be installed on your system.

### Steps

1. **Clone the Repository**

   Open your terminal or command prompt and run:
    ```
   git clone https://github.com/yourusername/domain-enumerator.git
   cd domain-enumerator

2. Install Dependencies

This tool uses only Python's standard libraries, so no additional packages are required. If future enhancements add dependencies, install them using:

```
pip install -r requirements.txt
```

## Usage
To run the domain enumerator, execute the following command from your terminal:

```
python domain_enumerator.py <target-domain>
```

This command will:

Append a list of common subdomains (e.g., www, mail, ftp) to the provided domain

Perform DNS lookups for each constructed subdomain.

Print out any subdomains that successfully resolve to an IP address.

Command-line Arguments
```
<target-domain>: The domain you wish to enumerate subdomains for (e.g., example.com). Do not include URL schemes like http:// or https://.
```

## How It Works

The tool leverages Python’s built-in socket module to perform DNS resolution. The basic workflow is as follows:

Subdomain List: A pre-defined list of common subdomains is maintained within the script.

DNS Lookup: For each subdomain, the script constructs a full domain name (e.g., mail.example.com) and attempts to resolve it.

Result Output: If the subdomain resolves to an IP address, it is printed out to the console.

Here’s a snippet of the core functionality:

```
import socket

def check_subdomain(domain, subdomain):
    full_domain = f"{subdomain}.{domain}"
    try:
        ip = socket.gethostbyname(full_domain)
        return ip
    except socket.gaierror:
        return None
```
This function encapsulates the DNS resolution for each subdomain, returning the IP address if the resolution is successful.

## Contributing

Contributions to enhance the functionality of this tool are welcome! Please follow these steps:

Fork the Repository: Create a fork of this repository on GitHub.

Create a Branch: Develop your feature or bug fix on a separate branch.

Submit a Pull Request: Once your changes are complete, submit a pull request for review.

For any significant changes, please open an issue first to discuss the proposed modifications.

## Future Enhancements

The following features are planned for future releases:

Multi-threading: Add multi-threading support to perform DNS lookups concurrently for faster results.

Custom Subdomain Lists: Allow users to supply their own list of subdomains.

Integration with Third-Party APIs: Enhance subdomain detection by integrating with additional services.

Advanced Reporting: Provide options to output the results in various formats (e.g., CSV, JSON).
Wildcard Subdomain Support: Improve detection of wildcard DNS entries.


## License

This project is licensed under the MIT License. See the LICENSE file for detailed information.
