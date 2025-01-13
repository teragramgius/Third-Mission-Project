#libraries import
import requests
import json
import os

#list of universities
universities = [
    {"name": "Università degli Studi 'Gabriele d'Annunzio'", "open_science_url": None},
    {"name": "Università degli Studi dell'Aquila", "open_science_url": "https://www.univaq.it/"},
    {"name": "Università degli Studi di Teramo", "open_science_url": None},
    {"name": "Università degli Studi della Basilicata", "open_science_url": None},
    {"name": "Università degli Studi Magna Græcia di Catanzaro", "open_science_url": None},
    {"name": "Università della Calabria", "open_science_url": None},
    {"name": "Università degli Studi 'Mediterranea' di Reggio Calabria", "open_science_url": None},
    {"name": "Università degli Studi di Napoli 'Federico II'", "open_science_url": "https://www.sba.unina.it/"},
    {"name": "Scuola Superiore Meridionale", "open_science_url": None},
    {"name": "Università degli Studi di Napoli 'L'Orientale'", "open_science_url": None},
    {"name": "Università degli Studi di Napoli 'Parthenope'", "open_science_url": None},
    {"name": "Università degli Studi della Campania Luigi Vanvitelli", "open_science_url": None},
    {"name": "Università degli Studi di Salerno", "open_science_url": None},
    {"name": "Università degli Studi del Sannio", "open_science_url": None},
    {"name": "Alma Mater Studiorum - Università di Bologna", "open_science_url": "https://www.unibo.it/"},
    {"name": "Università degli Studi di Ferrara", "open_science_url": "https://openscience.unife.it"},
    {"name": "Università degli Studi di Modena e Reggio Emilia", "open_science_url": "https://www.unimore.it"},
    {"name": "Università degli Studi di Parma", "open_science_url": "https://biblioteche.unipr.it/"},
    {"name": "Università degli Studi di Trieste", "open_science_url": "https://portale.units.it/"},
    {"name": "Università degli Studi di Udine", "open_science_url": "https://www.uniud.it/"},
    {"name": "Università degli Studi di Cassino e del Lazio Meridionale", "open_science_url": "https://www.unicas.it"},
    {"name": "Università degli Studi di Roma 'Foro Italico'", "open_science_url": "https://www.fondazioneuniroma4.it"},
    {"name": "Università degli Studi di Roma 'La Sapienza'", "open_science_url": "https://www.uniroma1.it"},
    {"name": "Università degli Studi di Roma Tor Vergata", "open_science_url": "https://web.uniroma2.it"},
    {"name": "Università degli Studi Roma Tre", "open_science_url": "https://romatrepress.uniroma3.it"},
    {"name": "Università degli Studi della Tuscia", "open_science_url": "https://dspace.unitus.it/"},
    {"name": "Università degli Studi di Genova", "open_science_url": "https://openscience.unige.it/"},
    {"name": "Università degli Studi di Bergamo", "open_science_url": "https://www.unibg.it"},
    {"name": "Università degli Studi di Brescia", "open_science_url": "https://www.unibs.it/"},
    {"name": "Politecnico di Milano", "open_science_url": "https://www2.polimi.it"},
    {"name": "Università degli Studi di Milano", "open_science_url": "https://openscience.unimi.it/"},
    {"name": "Università degli Studi di Milano-Bicocca", "open_science_url": "https://www.unimib.it"},
    {"name": "Istituto Universitario di Studi Superiori", "open_science_url": None},
    {"name": "Università degli Studi di Pavia", "open_science_url": "https://portale.unipv.it"},
    {"name": "Università degli Studi dell'Insubria", "open_science_url": "https://www.uninsubria.it"},
    {"name": "Università Politecnica delle Marche", "open_science_url": "https://cad.univpm.it"},
    {"name": "Università degli Studi di Camerino", "open_science_url": "https://www.unicam.it"},
    {"name": "Università degli Studi di Macerata", "open_science_url": "https://unimc.it/it"},
    {"name": "Università degli Studi di Urbino", "open_science_url": "https://uup.uniurb.it"},
    {"name": "Università degli Studi del Molise", "open_science_url": None},
    {"name": "Università degli Studi del Piemonte Orientale 'Amedeo Avogadro'", "open_science_url": None},
    {"name": "Università degli Studi di Torino", "open_science_url": "https://www.unito.it"},
    {"name": "Politecnico di Torino", "open_science_url": "https://www.polito.it"},
    {"name": "Politecnico di Bari", "open_science_url": "https://www.poliba.it"},
    {"name": "Università degli Studi di Bari", "open_science_url": "https://www.uniba.it"},
    {"name": "Università degli Studi di Foggia", "open_science_url": "https://www.unifg.it"},
    {"name": "Università del Salento", "open_science_url": "https://www.unisalento.it"},
    {"name": "Università degli Studi di Cagliari", "open_science_url": "https://en.unica.it"},
    {"name": "Università degli Studi di Sassari", "open_science_url": None},
    {"name": "Università degli Studi di Catania", "open_science_url": None},
    {"name": "Università degli Studi di Messina", "open_science_url": "https://www.unime.it"},
    {"name": "Università degli Studi di Palermo", "open_science_url": "https://www.unipa.it"},
    {"name": "Università degli Studi di Firenze", "open_science_url": "https://www.unifi.it"},
    {"name": "IMT - Scuola IMT Alti Studi Lucca", "open_science_url": None},
    {"name": "Scuola Normale Superiore", "open_science_url": "https://www.sns.it"},
    {"name": "Scuola superiore di studi universitari e di perfezionamento Sant'Anna", "open_science_url": "https://www.innovazione.santannapisa.it"},
    {"name": "Università di Pisa", "open_science_url": "https://www.unipi.it/index.php/open-science"},
    {"name": "Università degli Studi di Siena", "open_science_url": "https://www.sba.unisi.it/scrivere-e-pubblicare/open-access"},
    {"name": "Università per stranieri di Siena", "open_science_url": None},
    {"name": "Università degli Studi di Trento", "open_science_url": "https://www.openscience.unitn.it"},
    {"name": "Università degli Studi di Perugia", "open_science_url": "https://csb.unipg.it"},
    {"name": "Università per stranieri di Perugia", "open_science_url": "https://www.unistrapg.it"},
    {"name": "Università degli Studi di Padova", "open_science_url": "https://www.unipd.it"},
    {"name": "Università Ca' Foscari Venezia", "open_science_url": "https://unive.it"},
    {"name": "Università Iuav di Venezia", "open_science_url": "https://www.iuav.it"},
    {"name": "Università degli Studi di Verona", "open_science_url": "https://www.univr.it"},
    {"name": "Università della Valle d'Aosta", "open_science_url": "https://univda.iris.cineca.it"}
]
    
import requests
import json

# Function to fetch Wayback Machine snapshots
def fetch_wayback_snapshots(url, from_year, to_year):
    snapshots = []
    for year in range(from_year, to_year + 1):
        api_url = f"http://archive.org/wayback/available?url={url}&timestamp={year}0101"
        response = requests.get(api_url).json()
        snapshot = response.get('archived_snapshots', {}).get('closest')
        if snapshot:
            snapshots.append({
                "timestamp": snapshot.get("timestamp"),
                "archived_url": snapshot.get("open_science_url"),
                "original_url": url
            })
    return snapshots

# Main function to fetch snapshots and save them to a JSON file
def fetch_and_save_snapshots(universities, from_year, to_year, output_file):
    all_snapshots = []
    for uni in universities:
        snapshots = fetch_wayback_snapshots(uni['open_science_url'], from_year, to_year)
        for snapshot in snapshots:
            snapshot["university"] = uni["name"]
            all_snapshots.append(snapshot)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_snapshots, f, ensure_ascii=False, indent=4)
    print(f"Wayback snapshots successfully saved to {output_file}")


#variables
from_year = 1995
to_year = 1996
output_file = "data/raw/wayback_snapshots.json"
    

# Fetch and save snapshots
fetch_and_save_snapshots(universities, from_year, to_year, output_file)



#then parse subpages
