import sys
import requests
from prettytable import PrettyTable
from colorama import Fore, Style
from dns import resolver

def get_subdomains(domain):
    # Connect to crt.sh 
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    response = requests.get(url)

    # parse the subdomains of the requested domain
    subdomains = [item["name_value"] for item in response.json()]

    # and return the subdomains of requested domain
    return subdomains

def get_ip_address(subdomain):
    try:
        ip_address = resolver.resolve(subdomain,rdtype='A')[0].to_text()
    except Exception as e:
        ip_address = None
    return ip_address

if __name__ == "__main__":
    # Parse the command line arguments
    show_names = "--names" in sys.argv
    show_ips = "--ips" in sys.argv
    domain = sys.argv[-1]
    scope_file = None
    if "--scope" in sys.argv:
        scope_index = sys.argv.index("--scope")
        scope_file = sys.argv[scope_index + 1]

    # Retreive the subdomains
    subdomains = get_subdomains(domain)

    # Filter the subdomains by name if requested
    if show_names:
        subdomains = [s for s in subdomains if s.split(".")[0] != "*"]

    # Get the IP addresses of the subdomains
    ip_addresses = {}
    for subdomain in subdomains:
        ip_address = get_ip_address(subdomain)
        ip_addresses[subdomain] = ip_address

    # Read the penetration IP addresses from the file
    if scope_file:
        with open(scope_file, "r") as f:
            scope_ips = set(line.strip() for line in f)
        match_ips = set(ip_addresses.values()) & scope_ips
        if match_ips:
            print(Fore.MAGENTA + "Following  IP addresses which are in scope have been found:" + Style.RESET_ALL)
            for ip_address in match_ips:
                print(ip_address)
        else:
            print(Fore.RED + "No matching IP addresses in scope are found." + Style.RESET_ALL)

    # Print the subdomains and IP addresses in a table
    table = PrettyTable()
    if show_names and not show_ips:
        table.field_names = [Fore.GREEN + "Subdomain" + Style.RESET_ALL]
        for subdomain in subdomains:
            table.add_row([subdomain])
    elif show_ips:
        table.field_names = [Fore.BLUE + "IP Address" + Style.RESET_ALL]
        for subdomain, ip_address in ip_addresses.items():
            table.add_row([ip_address])
    else:
        table.field_names = [Fore.GREEN + "Subdomain" + Style.RESET_ALL, Fore.BLUE + "IP Address" + Style.RESET_ALL]
        for subdomain, ip_address in ip_addresses.items():
            table.add_row([subdomain, ip_address])
    print(table)
