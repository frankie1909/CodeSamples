import requests
import csv

# API Details
base_url = 'https://hp-api.onrender.com/api'
endpoint = '/characters'
headers = {'Accept': 'application/json'}

# API-Anfrage
response = requests.get(url=f"{base_url}{endpoint}", headers=headers)

# Prüfen, ob die Anfrage erfolgreich war
if response.status_code == 200:

    characters = response.json()

    # CSV-Datei zum Schreiben öffnen
    with open('/slu_HP_characters_from_api.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # CSV-Header schreiben
        writer.writerow(['id', 'name', 'alternate_names', 'species', 'gender', 'house', 'dateOfBirth', 'yearOfBirth',
                         'wizard', 'ancestry', 'eyeColour', 'hairColour', 'wand_wood', 'wand_core', 'wand_length',
                         'patronus', 'hogwartsStudent', 'hogwartsStaff', 'actor', 'alternate_actors', 'alive', 'image'])

        # Für jeden Charakter in der von der API zurückgegebenen Liste
        for character in characters:
            # Zauberstabdetails extrahieren
            wand = character.get('wand', {})
            wand_wood = wand.get('wood', '')
            wand_core = wand.get('core', '')
            # Umwandlung in String für die CSV
            wand_length = str(wand.get('length', ''))

            # Liste der alternativen Namen und Schauspieler in Strings umwandeln
            alternate_names = '; '.join(character.get('alternate_names', []))
            alternate_actors = '; '.join(character.get('alternate_actors', []))

            # Charakterdaten in die CSV-Datei schreiben
            writer.writerow([
                character.get('id', ''), character.get(
                    'name', ''), alternate_names, character.get('species', ''),
                character.get('gender', ''), character.get(
                    'house', ''), character.get('dateOfBirth', ''),
                character.get('yearOfBirth', ''), character.get(
                    'wizard', ''), character.get('ancestry', ''),
                character.get('eyeColour', ''), character.get(
                    'hairColour', ''), wand_wood, wand_core, wand_length,
                character.get('patronus', ''), character.get(
                    'hogwartsStudent', ''), character.get('hogwartsStaff', ''),
                character.get('actor', ''), alternate_actors, character.get(
                    'alive', ''), character.get('image', '')
            ])
else:
    print("Fehler beim Abrufen der Daten:", response.status_code)

# Pfad zur erstellten CSV-Datei
'/mnt/data/slu_HP_characters_from_api.csv'
