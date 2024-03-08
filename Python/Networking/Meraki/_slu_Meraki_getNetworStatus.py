import meraki
import json

API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
dashboard = meraki.DashboardAPI(API_KEY)


def get_network_status(network_id):
    try:
        # Netzwerkinformationen abrufen
        network = dashboard.networks.getNetwork(network_id)
        # Formatieren und Ausgeben der Netzwerkinformationen
        formatted_response = json.dumps(network, indent=4, ensure_ascii=False)
        print(formatted_response)
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")


def delete_network(network_id):
    try:
        # Löscht das angegebene Netzwerk
        dashboard.networks.deleteNetwork(network_id)
        print(f"Netzwerk {network_id} wurde erfolgreich gelöscht.")
    except Exception as e:
        print(
            f"Ein Fehler ist aufgetreten beim Versuch, das Netzwerk {network_id} zu löschen: {e}")


# Netzwerk-ID
network_id = "N_575334852396775991"

# Rufen Sie die Methode mit der spezifischen Netzwerk-ID auf
get_network_status(network_id)
# Netzwerk im Dashboard löschen
delete_network(network_id)
# noch einmal den Status abrufen
get_network_status(network_id)
