# janus-scan
A simple Python script to retreive subdomains of a domain using crt.sh service.


The script is a subdomain scanner that uses the crt.sh website to get a list of subdomains for a given domain and then resolves the IP addresses of those subdomains. The script also allows you to match the subdomains' IP addresses against a scope of IP addresses that you provide, which is usefull when you have a scope of penetration test.

To use the script, you need to have Python 3 installed on your machine, along with the required libraries listed in the requirements.txt file. You can install the libraries by running:

pip3 install -r requirements.txt

Run the script by using the command:
python3 janus-scan.py domain_name

Use the --names option to only show the subdomains and not their IP addresses:
janus.py domain_name --names

Use the --ips option to only show the IP addresses and not the subdomains. 
Example: python3 script_name.py domain_name --ips

Use the --scope option to provide a file containing a list of IP addresses to match against the subdomains' IP addresses. 
Example: python script_name.py domain_name --scope scope.txt

Why Janus?

In Roman mythology, Janus is the god of beginnings and transitions, often depicted with two faces looking towards the past and future. The script is named after him as it enumerates all the subdomains of a domain and their IP addresses, similar to how Janus looks towards the past and future, seeing all the beginning and end of things. And it's a shortcut for Just ANother Utility Scanner, if I ever expand the functions.

And, I'm just a sucker for mythological references.
