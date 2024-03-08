
# import response
import meraki
import json

API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
dashboard = meraki.DashboardAPI(API_KEY)
organizations = dashboard.organizations.getOrganizations()

formatted_response = json.dumps(organizations, indent=4, ensure_ascii=False)
# print(formatted_response)

# Organisation ID
organization_id = "575334852396585125"


# Netzwerkname
network_name = "slu_test"

# Netzwerktyp
# Dies ist ein Beispiel; passen Sie den Typ nach Bedarf an (z.B. 'wireless', 'switch', 'appliance', etc.)
network_type = 'wireless'

try:
    # Ein neues Netzwerk erstellen
    network_response = dashboard.organizations.createOrganizationNetwork(
        organization_id,
        name=network_name,
        productTypes=[network_type]
    )

    # Die Antwort formatieren und ausgeben
    formatted_response = json.dumps(
        network_response, indent=4, ensure_ascii=False)
    print(formatted_response)

except meraki.APIError as e:
    print(f"Ein API-Fehler ist aufgetreten: {e}")
except Exception as e:
    print(f"Ein allgemeiner Fehler ist aufgetreten: {e}")
