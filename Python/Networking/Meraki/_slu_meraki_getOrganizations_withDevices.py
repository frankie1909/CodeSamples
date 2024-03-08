import meraki
import json

API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
dashboard = meraki.DashboardAPI(API_KEY, output_log=False)


def get_organizations_with_devices(dashboard):
    orgs_with_devices = []

    # Schritt 1: Abrufen aller Organisationen
    organizations = dashboard.organizations.getOrganizations()
    for org in organizations:
        org_id = org['id']
        org_name = org['name']
        total_devices = 0

        # Schritt 2: Netzwerke für die Organisation abrufen
        networks = dashboard.organizations.getOrganizationNetworks(org_id)
        for network in networks:
            network_id = network['id']

            # Schritt 3: Geräte für das Netzwerk abrufen
            devices = dashboard.networks.getNetworkDevices(network_id)
            if devices:
                total_devices += len(devices)

        # Schritt 4: Organisationen und Geräteanzahl ausgeben, wenn mindestens ein Gerät vorhanden ist
        if total_devices > 0:
            orgs_with_devices.append(
                {"organization": org_name, "id": org_id, "total_devices": total_devices})

    return orgs_with_devices


# Starten der Funktion und Ausgabe der Ergebnisse
orgs_with_devices = get_organizations_with_devices(dashboard)
print(json.dumps(orgs_with_devices, indent=4))
