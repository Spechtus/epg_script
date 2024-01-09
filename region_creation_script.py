from pathlib import Path
import os
import requests
import json
import csv

ENV = "prod"

# Set path to working directory, as we use relative paths
new_path = Path(__file__).parent
os.chdir(new_path)

# Load token into file
with open("secret/secret.txt", encoding="UTF-8") as bearer_token:
    sportworld_API_token = bearer_token.read()

# Define header, URL and query
header = {
    "Authorization": "Bearer " + sportworld_API_token,
    "Content-Type": "application/json",
}


DEV_PATH = "https://sportworld.api.dev.b1smarttv.com/v3/console/regions"
PROD_PATH = "https://sportworld.api.b1smarttv.com/v3/console/regions"

# Static List of JSON values
# TODO: parse these from csv file based on "Country & Region handling" tab in Global Sports Channel List v1
region_list_mp1 = [
    # Belgium
    {
        "id": "belgium",
        "name": "Belgium",
        "localizedNames": [{"value": "Belgien", "locales": ["de"]}],
        "countryCodes": ["BE"],
        "locale": "en",
    },
    # Bulgaria
    {
        "id": "bulgaria",
        "name": "Bulgaria",
        "localizedNames": [{"value": "Bulgarien", "locales": ["de"]}],
        "countryCodes": ["BG"],
        "locale": "en",
    },
    # Croatia
    {
        "id": "croatia",
        "name": "Croatia",
        "localizedNames": [{"value": "Kroatien", "locales": ["de"]}],
        "countryCodes": ["HR"],
        "locale": "en",
    },
    # Czechia
    {
        "id": "czechia",
        "name": "Czechia",
        "localizedNames": [{"value": "Tschechien", "locales": ["de"]}],
        "countryCodes": ["CZ"],
        "locale": "en",
    },
    # Denmark
    {
        "id": "denmark",
        "name": "Denmark",
        "localizedNames": [{"value": "Dänemark", "locales": ["de"]}],
        "countryCodes": ["DK"],
        "locale": "en",
    },
    # Estonia
    {
        "id": "estonia",
        "name": "Estonia",
        "localizedNames": [{"value": "Estland", "locales": ["de"]}],
        "countryCodes": ["EE"],
        "locale": "en",
    },
    # Finland
    {
        "id": "finland",
        "name": "Finland",
        "localizedNames": [{"value": "Finland", "locales": ["de"]}],
        "countryCodes": ["FI"],
        "locale": "en",
    },
    # France
    {
        "id": "france",
        "name": "France",
        "localizedNames": [{"value": "Frankreich", "locales": ["de"]}],
        "countryCodes": ["FR"],
        "locale": "en",
    },
    # Greece
    {
        "id": "greece",
        "name": "Greece",
        "localizedNames": [{"value": "Griechenland", "locales": ["de"]}],
        "countryCodes": ["GR"],
        "locale": "en",
    },
    # Hungary
    {
        "id": "hungary",
        "name": "Hungary",
        "localizedNames": [{"value": "Ungarn", "locales": ["de"]}],
        "countryCodes": ["HU"],
        "locale": "en",
    },
    # Italy
    {
        "id": "italy",
        "name": "Italy",
        "localizedNames": [{"value": "Italien", "locales": ["de"]}],
        "countryCodes": ["IT"],
        "locale": "en",
    },
    # Latvia
    {
        "id": "latvia",
        "name": "Latvia",
        "localizedNames": [{"value": "Litauen", "locales": ["de"]}],
        "countryCodes": ["LV"],
        "locale": "en",
    },
    # Lithuania
    {
        "id": "lithuania",
        "name": "Lithuania",
        "localizedNames": [{"value": "Litauen", "locales": ["de"]}],
        "countryCodes": ["LT"],
        "locale": "en",
    },
    # Malta
    {
        "id": "malta",
        "name": "Malta",
        "localizedNames": [{"value": "Malta", "locales": ["de"]}],
        "countryCodes": ["MT"],
        "locale": "en",
    },
    # Netherlands
    {
        "id": "netherlands",
        "name": "Netherlands",
        "localizedNames": [{"value": "Niederlande", "locales": ["de"]}],
        "countryCodes": ["NL"],
        "locale": "en",
    },
    # Portugal
    {
        "id": "portugal",
        "name": "Portugal",
        "localizedNames": [{"value": "Portugal", "locales": ["de"]}],
        "countryCodes": ["PT"],
        "locale": "en",
    },
    # Romania
    {
        "id": "romania",
        "name": "Romania",
        "localizedNames": [{"value": "Rumänien", "locales": ["de"]}],
        "countryCodes": ["RO"],
        "locale": "en",
    },
    # Slovakia
    {
        "id": "slovakia",
        "name": "Slovakia",
        "localizedNames": [{"value": "Slowakai", "locales": ["de"]}],
        "countryCodes": ["SK"],
        "locale": "en",
    },
    # Slovenia
    {
        "id": "slovenia",
        "name": "Slovenia",
        "localizedNames": [{"value": "Slowenien", "locales": ["de"]}],
        "countryCodes": ["SI"],
        "locale": "en",
    },
    # Spain
    {
        "id": "spain",
        "name": "Spain",
        "localizedNames": [{"value": "Spanien", "locales": ["de"]}],
        "countryCodes": ["ES"],
        "locale": "en",
    },
    # Sweden
    {
        "id": "sweden",
        "name": "Sweden",
        "localizedNames": [{"value": "Schweden", "locales": ["de"]}],
        "countryCodes": ["SE"],
        "locale": "en",
    },
]

region_list_mp2 = [
    # Albania
    {
        "id": "albania",
        "name": "Albania",
        "localizedNames": [{"value": "Albanien", "locales": ["de"]}],
        "countryCodes": ["AL"],
        "locale": "en",
    },
    # Australia
    {
        "id": "australia",
        "name": "Australien",
        "localizedNames": [{"value": "Australien", "locales": ["de"]}],
        "countryCodes": ["AU"],
        "locale": "en",
    },
    # Bahrain
    {
        "id": "bahrain",
        "name": "Bahrain",
        "localizedNames": [{"value": "Bahrain", "locales": ["de"]}],
        "countryCodes": ["BH"],
        "locale": "en",
    },
    # Brazil
    {
        "id": "brazil",
        "name": "Brazil",
        "localizedNames": [{"value": "Brasilien", "locales": ["de"]}],
        "countryCodes": ["BR"],
        "locale": "en",
    },
    # Canada
    {
        "id": "canada",
        "name": "Canada",
        "localizedNames": [{"value": "Kanada", "locales": ["de"]}],
        "countryCodes": ["CA"],
        "locale": "en",
    },
    # Colombia
    {
        "id": "colombia",
        "name": "Colombia",
        "localizedNames": [{"value": "Kolumbien", "locales": ["de"]}],
        "countryCodes": ["CO"],
        "locale": "en",
    },
    # Ecuador
    {
        "id": "ecuador",
        "name": "Ecuador",
        "localizedNames": [{"value": "Ecuador", "locales": ["de"]}],
        "countryCodes": ["EC"],
        "locale": "en",
    },
    # Georgia
    {
        "id": "georgia",
        "name": "Georgia",
        "localizedNames": [{"value": "Georgien", "locales": ["de"]}],
        "countryCodes": ["GE"],
        "locale": "en",
    },
    # Guatemala
    {
        "id": "guatemala",
        "name": "Guatemala",
        "localizedNames": [{"value": "Guatemala", "locales": ["de"]}],
        "countryCodes": ["GT"],
        "locale": "en",
    },
    # Iceland
    {
        "id": "iceland",
        "name": "Iceland",
        "localizedNames": [{"value": "Island", "locales": ["de"]}],
        "countryCodes": ["IS"],
        "locale": "en",
    },
    # Indonesia
    {
        "id": "indonesia",
        "name": "Indonesia",
        "localizedNames": [{"value": "Indonesien", "locales": ["de"]}],
        "countryCodes": ["ID"],
        "locale": "en",
    },
    # Israel
    {
        "id": "israel",
        "name": "Israel",
        "localizedNames": [{"value": "Israel", "locales": ["de"]}],
        "countryCodes": ["IL"],
        "locale": "en",
    },
    # Jamaica
    {
        "id": "jamaica",
        "name": "Jamaica",
        "localizedNames": [{"value": "Jamaica", "locales": ["de"]}],
        "countryCodes": ["JM"],
        "locale": "en",
    },
    # Korea
    {
        "id": "korea",
        "name": "Korea",
        "localizedNames": [{"value": "Korea", "locales": ["de"]}],
        "countryCodes": ["KR"],
        "locale": "en",
    },
    # North Macedonia
    {
        "id": "north-macedonia",
        "name": "North Macedonia",
        "localizedNames": [{"value": "Nord Mazedonien", "locales": ["de"]}],
        "countryCodes": ["MK"],
        "locale": "en",
    },
    # Montenegro
    {
        "id": "montenegro",
        "name": "Montenegro",
        "localizedNames": [{"value": "Montenegro", "locales": ["de"]}],
        "countryCodes": ["ME"],
        "locale": "en",
    },
    # New Zealand
    {
        "id": "new-zealand",
        "name": "New Zealand",
        "localizedNames": [{"value": "Neuseeland", "locales": ["de"]}],
        "countryCodes": ["NZ"],
        "locale": "en",
    },
    # Nicaragua
    {
        "id": "nicaragua",
        "name": "Nicaragua",
        "localizedNames": [{"value": "Nicaragua", "locales": ["de"]}],
        "countryCodes": ["NI"],
        "locale": "en",
    },
    # Norway
    {
        "id": "norway",
        "name": "Norway",
        "localizedNames": [{"value": "Norwegen", "locales": ["de"]}],
        "countryCodes": ["NO"],
        "locale": "en",
    },
    # Panama
    {
        "id": "panama",
        "name": "Panama",
        "localizedNames": [{"value": "Panama", "locales": ["de"]}],
        "countryCodes": ["PA"],
        "locale": "en",
    },
    # Peru
    {
        "id": "peru",
        "name": "Peru",
        "localizedNames": [{"value": "Peru", "locales": ["de"]}],
        "countryCodes": ["PE"],
        "locale": "en",
    },
    # Philippines
    {
        "id": "philippines",
        "name": "Philippines",
        "localizedNames": [{"value": "Philipinen", "locales": ["de"]}],
        "countryCodes": ["PH"],
        "locale": "en",
    },
    # Serbia
    {
        "id": "serbia",
        "name": "Serbia",
        "localizedNames": [{"value": "Serbien", "locales": ["de"]}],
        "countryCodes": ["RS"],
        "locale": "en",
    },
    # South Africa
    {
        "id": "south-africa",
        "name": "South Africa",
        "localizedNames": [{"value": "Süd Afrika", "locales": ["de"]}],
        "countryCodes": ["ZA"],
        "locale": "en",
    },
    # Togo
    {
        "id": "togo",
        "name": "Togo",
        "localizedNames": [{"value": "Togo", "locales": ["de"]}],
        "countryCodes": ["TG"],
        "locale": "en",
    },
    # Türkiye
    {
        "id": "turkiye",
        "name": "Turkiye",
        "localizedNames": [{"value": "Türkei", "locales": ["de"]}],
        "countryCodes": ["TR"],
        "locale": "en",
    },
    # Ukraine
    {
        "id": "ukraine",
        "name": "Ukraine",
        "localizedNames": [{"value": "Ukraine", "locales": ["de"]}],
        "countryCodes": ["UA"],
        "locale": "en",
    },
    # UK
    {
        "id": "united-kingdom",
        "name": "United Kingdom",
        "localizedNames": [{"value": "Großbritannien", "locales": ["de"]}],
        "countryCodes": ["GB"],
        "locale": "en",
    },
    # US
    {
        "id": "united-states",
        "name": "United States of America",
        "localizedNames": [
            {"value": "Vereinigte Staaten von Amerika", "locales": ["de"]}
        ],
        "countryCodes": ["US"],
        "locale": "en",
    },
    # Venezuela
    {
        "id": "venecuela",
        "name": "Venecuela",
        "localizedNames": [{"value": "Venezuela", "locales": ["de"]}],
        "countryCodes": ["VE"],
        "locale": "en",
    },
]


# Function to make network request with bearer token
# TODO: print results in csv, etc as for channels
def make_network_request(data, env):
    url = PROD_PATH if env == "prod" else DEV_PATH
    print("URL = " + url)
    response = requests.post(url, headers=header, json=data)

    # Perform any necessary processing on response
    # ...

    return response


# Iterate over each JSON value and make network request
for item in region_list_mp2:
    id = item.get("id")
    print("Process for {0}".format(id))
    response = make_network_request(item, env=ENV)
    try:
        print(
            "Response for item: {0}".format(id) + response.json()
        )  # Print response JSON (optional)
    except:
        print("Cannot parse body for item: {0}".format(id))
    print(
        "Response for item: {0} = {1}".format(id, response.status_code)
    )  # Print response status code (optional)
