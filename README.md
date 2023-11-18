Cybersecurity and System Analysis Scripts Repository README

Repository Overview

This repository, created and maintained by J0hn-0, is a curated collection of Python scripts focused on cybersecurity and system analysis tasks. These scripts serve a variety of purposes, ranging from process monitoring to data gathering, each tailored to enhance cybersecurity efforts and system management.

Contents

	1.	Process and Thread Information Script
	•	Function: Lists and provides details of running processes.
	•	Dependencies: psutil
	2.	Registry Key Analysis Script
	•	Function: Fetches and displays values from specific Windows registry keys.
	•	Dependencies: winreg (built-in)
	3.	Process and Registry Monitoring Script
	•	Function: Monitors specific Windows processes and their registry settings.
	•	Dependencies: winreg, psutil
	4.	Web Host Information Gathering Script
	•	Function: Gathers detailed information about a web host.
	•	Dependencies: requests, socket, BeautifulSoup, dns.resolver, whois, ssl, shodan
	5.	Server Information Retrieval Script
	•	Function: Retrieves information about servers from a JSON file and writes to a text file.
	•	Dependencies: json, requests
	6.	Process Base Address Search Script
	•	Function: Searches a log file for processes with a specified base address.
	•	Dependencies: sys (built-in)
	7.	Windows Defender File Cleanup Script
	•	Function: Automates the deletion of specific Windows Defender-related files.
	•	Dependencies: subprocess, os, ctypes, sys

Installation

Each script in this repository has its own set of dependencies, most of which can be installed using pip. For detailed installation instructions, please refer to the README section of each script.

Usage

All scripts are designed to be run in a Python environment. Users should ensure they have the necessary permissions and environment setup as required for each script. Usage instructions are detailed in the individual README sections.

Security and System Administration Context

These scripts are especially useful for system administrators, cybersecurity enthusiasts, and professionals. They assist in critical tasks such as monitoring, analysis, data gathering, and maintenance, playing a vital role in cybersecurity and system management.

Repository Maintenance

The repository is an evolving collection of scripts, regularly updated to include new tools and enhancements to existing ones. Contributions and feedback from the community are highly valued and welcomed.

Author

J0hn-0

