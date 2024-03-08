import requests
import json

# Ignoriert SSL-Zertifikatsüberprüfungen (Nicht empfohlen für Produktivumgebungen)
requests.packages.urllib3.disable_warnings()  # Unterdrückt Warnungen

################ LOGIN ######################
url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"

user = 'devnetuser'
pw = 'Cisco123!'

response = requests.post(url, auth=(user, pw), verify=False).json()
# print(response)
token = response['Token']

url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/site"

payload = {}
headers = {
    'x-auth-token': token,
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers, verify=False).json()

print(json.dumps(response, indent=2))
