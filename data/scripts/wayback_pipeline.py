#libraries import
import requests
import json
import os

#list of universities
universities = [
    {"name": "Università degli Studi 'Gabriele d'Annunzio'", "open_science_url": None},
    {"name": "Università degli Studi dell'Aquila", "open_science_url": "https://www.univaq.it/section.php?id=2265"},
    {"name": "Università degli Studi di Teramo", "open_science_url": None},
    {"name": "Università degli Studi della Basilicata", "open_science_url": None},
    {"name": "Università degli Studi Magna Græcia di Catanzaro", "open_science_url": None},
    {"name": "Università della Calabria", "open_science_url": None},
    {"name": "Università degli Studi 'Mediterranea' di Reggio Calabria", "open_science_url": None},
    {"name": "Università degli Studi di Napoli 'Federico II'", "open_science_url": "https://www.sba.unina.it/index.php/open-access-open-science/"},
    {"name": "Scuola Superiore Meridionale", "open_science_url": None},
    {"name": "Università degli Studi di Napoli 'L'Orientale'", "open_science_url": None},
    {"name": "Università degli Studi di Napoli 'Parthenope'", "open_science_url": None},
    {"name": "Università degli Studi della Campania Luigi Vanvitelli", "open_science_url": None},
    {"name": "Università degli Studi di Salerno", "open_science_url": None},
    {"name": "Università degli Studi del Sannio", "open_science_url": None},
    {"name": "Alma Mater Studiorum - Università di Bologna", "open_science_url": "https://www.unibo.it/it/ricerca/open-science"},
    {"name": "Università degli Studi di Ferrara", "open_science_url": "https://openscience.unife.it/menu/open-science"},
    {"name": "Università degli Studi di Modena e Reggio Emilia", "open_science_url": "https://www.unimore.it/it/ricerca/scienza-aperta"},
    {"name": "Università degli Studi di Parma", "open_science_url": "https://biblioteche.unipr.it/notizie/unipr-lopen-access"},
    {"name": "Università degli Studi di Trieste", "open_science_url": "https://portale.units.it/it/ricerca/open-science"},
    {"name": "Università degli Studi di Udine", "open_science_url": "https://www.uniud.it/it/ricerca/scienza-aperta/accesso-aperto-pubblicazioni/valorizzazione-e-promozione-open-access/documenti/open-access-informazioni-generali"},
    {"name": "Università degli Studi di Cassino e del Lazio Meridionale", "open_science_url": "https://www.unicas.it/ricerca/open-science/"},
    {"name": "Università degli Studi di Roma 'Foro Italico'", "open_science_url": "https://www.fondazioneuniroma4.it/index.php/cosa-facciamo/riviste-open-access"},
    {"name": "Università degli Studi di Roma 'La Sapienza'", "open_science_url": "https://www.uniroma1.it/it/pagina/sapienza-lopen-access"},
    {"name": "Università degli Studi di Roma Tor Vergata", "open_science_url": "https://web.uniroma2.it/it/percorso/ricerca_internazionale/sezione/open_access"},
    {"name": "Università degli Studi Roma Tre", "open_science_url": "https://romatrepress.uniroma3.it/open-science/"},
    {"name": "Università degli Studi della Tuscia", "open_science_url": "https://dspace.unitus.it/"},
    {"name": "Università degli Studi di Genova", "open_science_url": "https://openscience.unige.it/"},
    {"name": "Università degli Studi di Bergamo", "open_science_url": "https://www.unibg.it/rubrica/bibliometria-ranking-e-open-science"},
    {"name": "Università degli Studi di Brescia", "open_science_url": "https://www.unibs.it/it/node/9192"},
    {"name": "Politecnico di Milano", "open_science_url": "https://www2.polimi.it/en/research/research-at-the-politecnico/publications-and-open-access.html"},
    {"name": "Università degli Studi di Milano", "open_science_url": "https://openscience.unimi.it/"},
    {"name": "Università degli Studi di Milano-Bicocca", "open_science_url": "https://www.unimib.it/ricerca/scienza-aperta"},
    {"name": "Istituto Universitario di Studi Superiori", "open_science_url": None},
    {"name": "Università degli Studi di Pavia", "open_science_url": "https://portale.unipv.it/it/ricerca/open-science"},
    {"name": "Università degli Studi dell'Insubria", "open_science_url": "https://www.uninsubria.it/ricerca/ricerca-insubria/open-access-e-open-science"},
    {"name": "Università Politecnica delle Marche", "open_science_url": "https://cad.univpm.it/SebinaOpac/article/open-access/oa-info_autori_new"},
    {"name": "Università degli Studi di Camerino", "open_science_url": "https://www.unicam.it/eventi/2023/open-science-open-innovation"},
    {"name": "Università degli Studi di Macerata", "open_science_url": "https://unimc.it/it/ricerca/policy/open-science"},
    {"name": "Università degli Studi di Urbino", "open_science_url": "https://uup.uniurb.it/open-science"},
    {"name": "Università degli Studi del Molise", "open_science_url": None},
    {"name": "Università degli Studi del Piemonte Orientale 'Amedeo Avogadro'", "open_science_url": None},
    {"name": "Università degli Studi di Torino", "open_science_url": "https://www.unito.it/ricerca-e-innovazione/fare-ricerca-unito/open-science"},
    {"name": "Politecnico di Torino", "open_science_url": "https://www.polito.it/en/social-impact/polito-libraries/open-science"},
    {"name": "Politecnico di Bari", "open_science_url": "https://www.poliba.it/it/biblioteca-digitale/open-access-agevolazioni-i-docenti-del-politecnico-di-bari"},
    {"name": "Università degli Studi di Bari", "open_science_url": "https://www.uniba.it/it/ricerca/ricerca/policy-ricerca/open-science"},
    {"name": "Università degli Studi di Foggia", "open_science_url": "https://www.unifg.it/sites/default/files/normative/2021-06/regolamento-open-access-policy.pdf"},
    {"name": "Università del Salento", "open_science_url": "https://www.unisalento.it/-/universita-open-science-e-terza-missione"},
    {"name": "Università degli Studi di Cagliari", "open_science_url": "https://en.unica.it/en/research/research-evaluation/open-science"},
    {"name": "Università degli Studi di Sassari", "open_science_url": None},
    {"name": "Università degli Studi di Catania", "open_science_url": None},
    {"name": "Università degli Studi di Messina", "open_science_url": "https://www.unime.it/terza-missione/open-science-unime"},
    {"name": "Università degli Studi di Palermo", "open_science_url": "https://www.unipa.it/Open-science/"},
    {"name": "Università degli Studi di Firenze", "open_science_url": "https://www.unifi.it/en/research-and-innovation/research/open-science"},
    {"name": "IMT - Scuola IMT Alti Studi Lucca", "open_science_url": None},
    {"name": "Scuola Normale Superiore", "open_science_url": "https://www.sns.it/it/open-science-come-fare"},
    {"name": "Scuola superiore di studi universitari e di perfezionamento Sant'Anna", "open_science_url": "https://www.innovazione.santannapisa.it/it/biblioteca/open-access-pratica"},
    {"name": "Università di Pisa", "open_science_url": "https://www.unipi.it/index.php/open-science"},
    {"name": "Università degli Studi di Siena", "open_science_url": "https://www.sba.unisi.it/scrivere-e-pubblicare/open-access"},
    {"name": "Università per stranieri di Siena", "open_science_url": None},
    {"name": "Università degli Studi di Trento", "open_science_url": "https://www.openscience.unitn.it/scienza-aperta-unitrento"},
    {"name": "Università degli Studi di Perugia", "open_science_url": "https://csb.unipg.it/servizi/per-chi-pubblica/open-science-e-open-access"},
    {"name": "Università per stranieri di Perugia", "open_science_url": "https://www.unistrapg.it/it/vivere-il-campus/biblioteca-d-ateneo-e-laboratori/biblioteca/fondo-gallenga-stuart-schunk/biblioteca-digitale"},
    {"name": "Università degli Studi di Padova", "open_science_url": "https://www.unipd.it/open-science"},
    {"name": "Università Ca' Foscari Venezia", "open_science_url": "https://unive.it/pag/10537/"},
    {"name": "Università Iuav di Venezia", "open_science_url": "https://www.iuav.it/it/esiti-della-ricerca/open-science"},
    {"name": "Università degli Studi di Verona", "open_science_url": "https://www.univr.it/it/agevolazioni-per-pubblicare-in-open-access"},
    {"name": "Università della Valle d'Aosta", "open_science_url": "https://univda.iris.cineca.it/sr/cineca/files/Regolamento_di_Ateneo_Open_Access_Univda.pdf"}
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
from_year = 2000
to_year = 2024
output_file = "data/raw/wayback_snapshots.json"
    

# Fetch and save snapshots
fetch_and_save_snapshots(universities, from_year, to_year, output_file)




