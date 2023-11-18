Cybersecurity and System Analysis Scripts Repository

Repository Overview

This repository contains a collection of Python scripts designed for various cybersecurity and system analysis tasks. These scripts cover a range of functions, from process monitoring and registry key analysis to web host information gathering, server inventory management, and specialized file operations.

Contents:

Process and Thread Information Script

Lists and details processes running on a system.

Dependencies: psutil

Registry Key Analysis Script

Fetches and displays values from specific Windows registry keys.

Dependencies: winreg (built-in)

Process and Registry Monitoring Script

Monitors specific Windows processes and their registry settings.

Dependencies: winreg, psutil

Web Host Information Gathering Script

Gathers detailed information about a web host.

Dependencies: requests, socket, BeautifulSoup, dns.resolver, whois, ssl, shodan

Server Information Retrieval Script

Fetches information about servers from a JSON file and writes to a text file.

Dependencies: json, requests

Process Base Address Search Script

Searches a log file for processes with a specified base address.

Dependencies: sys (built-in)

Windows Defender File Cleanup Script

Automates deletion of specific Windows Defender-related files.

Dependencies: subprocess, os, ctypes, sys

Installation
Each script has individual dependencies, most of which can be installed using pip. Refer to each script's README section for specific installation instructions.

Usage

Scripts can be run in a Python environment, with usage instructions detailed in the README section of each script. Ensure to have the necessary permissions and environment setup as required by each script.

Security and System Administration Context

These scripts are tailored for system administrators, cybersecurity enthusiasts, and professionals. They aid in tasks such as monitoring, analysis, data gathering, and maintenance, crucial for cybersecurity and system management.

Repository Maintenance

This repository is regularly updated to include more scripts and enhancements to existing ones. Contributions and feedback are welcome.

Author
J0hn-0
