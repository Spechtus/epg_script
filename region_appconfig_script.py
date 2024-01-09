from pathlib import Path
import os
import requests
import json
import csv

# Set env to prod, test, dev
ENV = "prod"

# Set path to working directory, as we use relative paths
new_path = Path(__file__).parent
os.chdir(new_path)

# Login if credentials provided
PROD_IDENTITY_PATH = "https://identity.api.b1smarttv.com/tenants/b1smarttv/basic/developers/login"
# TODO: TEST_PATH missing
DEV_IDENTITY_PATH = "https://identity.api.dev.b1smarttv.com/tenants/b1smarttv/basic/developers/login"

if ENV == "prod":
    identity_path = PROD_IDENTITY_PATH
    with open("secret/credentials_prod.txt", encoding="UTF-8") as file:
        username = file.readline().strip()
        password = file.readline().strip()
else:
    identity_path = DEV_IDENTITY_PATH
    with open("secret/credentials_dev.txt", encoding="UTF-8") as file:
        username = file.readline().strip()
        password = file.readline().strip()

identity_payload = json.dumps({
  "refreshable": True,
  "expiresAfter": 47215073
})
identity_headers = {
  'Content-Type': 'application/json',
  'Accept': 'text/plain',
}
identity_response = requests.request("POST", PROD_IDENTITY_PATH, auth=(username,password), headers=identity_headers, data=identity_payload)

sportworld_API_token = ''
if identity_response.status_code == 200:
    sportworld_API_token = identity_response.json()['accessToken']
    print('Successfully logged in with credentials')
else:
    print('Could not log in with credentials')

# Load token into file
if not sportworld_API_token:
    print('sportworld_API_token == null; try to read directly from file')
    if ENV == "prod":
        with open("secret/sportworldAPI_key_prod.txt", encoding="UTF-8") as bearer_token:
            sportworld_API_token = bearer_token.read()
    else:
        with open("secret/sportworldAPI_key_dev.txt", encoding="UTF-8") as bearer_token:
            sportworld_API_token = bearer_token.read()

# Define header, URL and query
header = {
    "Authorization": "Bearer " + sportworld_API_token,
    "Content-Type": "application/json",
}

DEV_PATH = (
    "https://sportworld.api.dev.b1smarttv.com/v3/console/regions/{regionId}/appconfig"
)
DEV_PATH_LEGAL_PRIVACY = "https://sportworld.api.dev.b1smarttv.com/v3/console/regions/{regionId}/legal/privacy"
DEV_PATH_LEGAL_IMPRINT = "https://sportworld.api.dev.b1smarttv.com/v3/console/regions/{regionId}/legal/imprint"
DEV_PATH_LEGAL_TERMS = (
    "https://sportworld.api.dev.b1smarttv.com/v3/console/regions/{regionId}/legal/terms"
)

# TODO: TEST_PATH missing

PROD_PATH = (
    "https://sportworld.api.b1smarttv.com/v3/console/regions/{regionId}/appconfig"
)
PROD_PATH_LEGAL_PRIVACY = (
    "https://sportworld.api.b1smarttv.com/v3/console/regions/{regionId}/legal/privacy"
)
PROD_PATH_LEGAL_IMPRINT = (
    "https://sportworld.api.b1smarttv.com/v3/console/regions/{regionId}/legal/imprint"
)
PROD_PATH_LEGAL_TERMS = (
    "https://sportworld.api.b1smarttv.com/v3/console/regions/{regionId}/legal/terms"
)

# List of JSON values based on "Bundle Region"
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

id_list_mp1 = []
for id in region_list_mp1:
    id = id.get("id")
    id_list_mp1.append(id)
print("MP1")
print('"' + '","'.join(id_list_mp1) + '"')

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

id_list_mp2 = []
for id in region_list_mp2:
    id = id.get("id")
    id_list_mp2.append(id)
print("MP2")
print('"' + '","'.join(id_list_mp2) + '"')

# Prepare data to set for selected bundle region
# dev
appconfig_dev = {
    "homePageId": "sw$dc9f47012f1b49d89",
    "selectedPageId": "sw$bcd7c35dcf20412b8",
    "cataloguePageIds": ["sw$ff70c892b2c14a86a"],
    "welcomeScreenCounter": 5,
    "limitTilesPerLine": 20,
    "cacheDuration": 60,
    "channelsLimit": 40,
    "channelEventsLimit": 50,
    "catalogPagesLimit": 0,
    "refreshInterval": 900,
    "disabledMenuItems": ["sports", "calendar"],
}

# prod - should be the same for mp1 and mp2 (only dach is different)
appconfig_prod_international = {
    "homePageId": "sw$e1e1686b2ea0438a9",
    "selectedPageId": "sw$f8966e5fbd124b62a",
    "cataloguePageIds": [
        "sw$0ef2d4a8ed7b4f6a8",
        "sw$a796be1a70d74b08b",
        "sw$114902eee3fa4a518",
        "sw$049bb30432d54252b",
        "sw$db37e119d19741d19",
        "sw$f6ae4291ca924a4f8",
        "sw$e9a71299f8ea4dcf8",
        "sw$20c8fdc5baad44659",
        "sw$5770e727ead848a19",
        "sw$7a76c6a56e034c799",
        "sw$e3badf46b385471d8",
        "sw$11c64c013df845319",
        "sw$9ade365576c94f429",
        "sw$92281776434240728",
        "sw$39f68a76c0f24cec9",
        "sw$c859f79e592b4ef2a",
        "sw$4d6eb7a32abe480db",
        "sw$4d3f8a00563e43acb",
        "sw$90f82581deb74a48a",
        "sw$ee5a2d009efc4fecb",
        "sw$a4f68c8d75dd420eb"
    ],
    "welcomeScreenCounter": 5,
    "limitTilesPerLine": 20,
    "cacheDuration": 60,
    "channelsLimit": 400,
    "channelEventsLimit": 5,
    "catalogPagesLimit": 0,
    "refreshInterval": 900,
    "disabledMenuItems": [],
}

# For legal requests:
# 1. Convert word into html
legal_privacy = {
    "html": [
        {
            "locales": ["de-DE"],
            "value": """<p>Datenschutzerkl&auml;rung</p>
<p>&nbsp;</p>
<p>Der Schutz deiner personenbezogenen Daten ist uns sehr wichtig. Nachfolgend m&ouml;chten wir dich daher dar&uuml;ber informieren, welche Daten wir auf welche Weise verarbeiten, wenn du unser Angebot nutzt.</p>
<p>&nbsp;</p>
<p>1.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Wie erreichst du uns?</p>
<p>&nbsp;</p>
<p>Die datenverarbeitende Stelle und datenschutzrechtlich f&uuml;r die Verarbeitung deiner Daten verantwortlich sind wir, die:</p>
<p>&nbsp;</p>
<p>B1 SmartTV GmbH</p>
<p>Ainmillerstr. 28</p>
<p>80801 München</p>
<p>E-Mail: info@b1smarttv.com</p>
<p>&nbsp;</p>
<p>2.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Wie&nbsp;erreichst du unseren&nbsp;Datenschutzbeauftragten?</p>
<p>&nbsp;</p>
<p>Gerne kannst du dich bei Fragen zum Datenschutz auch jederzeit an unseren Datenschutzbeauftragten wenden:</p>
<p>&nbsp;</p>
<p>Dr. Georg F. Schr&ouml;der, LL.M.</p>
<p>legal data Schr&ouml;der Rechtsanwaltsgesellschaft mbH</p>
<p>Prannerstr. 1</p>
<p>80333 M&uuml;nchen</p>
<p>Tel.: +49 89 954 597 520</p>
<p>E-Mail: datenschutz@legaldata.law</p>
<p>&nbsp;</p>
<p>3.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Welche Datenkategorien verwenden wir?</p>
<p>&nbsp;</p>
<p>Wir verarbeiten die folgenden Datenkategorien, wenn du unsere Apps und Services nutzt:</p>
<p>&nbsp;</p>
<p>Technisch erforderliche Daten</p>
<p>Um unsere Apps und Services bereitstellen zu k&ouml;nnen, verarbeiten wir eine Reihe technischer Daten. Diese sind vor allem daf&uuml;r erforderlich, zwischen deinem Endger&auml;t und unseren Servern eine Verbindung herzustellen. Dies betrifft unter anderem deine IP-Adresse, die innerhalb unserer Apps und Services aufgerufene Seite, Datum und Zeit des Aufrufs sowie ggf. weitere ger&auml;tebezogene Daten wie z.B. die Art des Smartphones / Smart-TV oder Spracheinstellungen.</p>
<p>&nbsp;</p>
<p>Account-Daten</p>
<p>Wir verarbeiten vor allem deine Zugangsdaten, insbesondere den Account-Namen, die Account-ID, die E-Mail-Adressen sowie die Anschrift und ggf. Zahlungsinformationen wie Konto- oder Kreditkartennummer und den Zahlungsverlauf, um dir den Zugang zu unseren Apps und Services bereitstellen zu k&ouml;nnen.</p>
<p>&nbsp;</p>
<p>Nutzungsdaten</p>
<p>Wenn du einen Account bei uns er&ouml;ffnest, k&ouml;nnen wir dir anhand deines Verlaufs Empfehlungen anzeigen, die auf deine Interessen zugeschnitten sind. Dies betrifft insbesondere die aufgerufenen Inhalte, die Dauer des Aufrufs und den Suchverlauf. Zudem verarbeiten wir die von dir abgegebenen Bewertungen und Rezensionen.</p>
<p>&nbsp;</p>
<p>Marketingdaten</p>
<p>Dies beinhaltet vor allem deine Werbeeinstellungen, Cookie-Einstellungen und damit zusammenh&auml;ngende Ger&auml;te-, Werbe- und Cookie-IDs. Zudem verarbeiten wir die in den Abschnitten 10 und 11 dieser Datenschutzerkl&auml;rung genannten Datenkategorien.</p>
<p>&nbsp;</p>
<p>Statistische Daten</p>
<p>Daneben erheben wir statistische Daten zur Nutzung unserer Apps und Services. Dies umfasst z.B. die Art des Endger&auml;ts, mit dem du unsere Apps und Services verwendest, das Betriebssystem und Spracheinstellungen. Hierf&uuml;r werden personenbezogene Daten unserer Nutzer anonymisiert und flie&szlig;en in ein statistisches Gesamtergebnis ein. Von diesem ausgehend sind keine R&uuml;ckschl&uuml;sse auf einzelne Nutzer m&ouml;glich.</p>
<p>&nbsp;</p>
<p>4.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Woher stammen diese Daten?</p>
<p>&nbsp;</p>
<p>Die meisten Daten, die wir &uuml;ber dich verarbeiten, gibst du uns im Rahmen einer Account-Er&ouml;ffnung oder der Nutzung unserer Apps und Services an. Dies betrifft bspw. deine Account-Informationen, Zahlungsangaben oder deine Werbeeinstellungen.</p>
<p>&nbsp;</p>
<p>Bestimmte technische Daten, die f&uuml;r die Bereitstellung unserer Apps und Services erforderlich sind, erfassen wir durch automatische &Uuml;bermittlung durch dein Endger&auml;t oder deinen Internetanbieter (z.B. IP-Adresse).</p>
<p>&nbsp;</p>
<p>Zudem k&ouml;nnen bestimmte Daten von unseren Kooperationspartnern &uuml;bermittelt werden, deren Angebot wir in unsere Apps und Services einbinden. Hierdurch wird sichergestellt, dass du die Produkte unserer Partner nutzen kannst, ohne unsere Apps und Services zu verlassen (z.B. Best&auml;tigung einer Produktbuchung, Zahlungsabwicklung).</p>
<p>&nbsp;</p>
<p>5.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Zu welchen Zwecken verwenden wir deine Daten?</p>
<p>&nbsp;</p>
<p>Wir verarbeiten deine Daten</p>
<ul class="decimal_type">
    <li>auf der Grundlage einer ausdr&uuml;cklichen Einwilligung von dir (Art. 6 Abs. 1 lit. a) DS-GVO) &ndash; z.B. pseudonyme Cookie-IDs zur personalisierten werblichen Ansprache, E-Mail-Adressen zur Zusendung von Newslettern,</li>
    <li>zur Erf&uuml;llung eines Vertragsverh&auml;ltnisses mit dir (Art. 6 Abs. 1 lit. b) DS-GVO) &ndash; z.B. Abrechnungs- und Zahlungsdaten, gebuchte Leistungen (auch unserer Kooperationspartner),</li>
    <li>zur Erf&uuml;llung rechtlicher Verpflichtungen (Art. 6 Abs. 1 lit. c) DS-GVO) &ndash; z.B. Bestellbest&auml;tigungen und Rechnungen,</li>
    <li>zur Wahrnehmung unserer sog. berechtigten Interessen (Art. 6 Abs. 1 lit. f) DS-GVO); in diesem Fall teilen wir dir jeweils mit, worin unser berechtigtes Interesse an der Datenverarbeitung besteht &ndash; z.B. technische Daten zur Gew&auml;hrleistung der Systemsicherheit.</li>
</ul>
<p>&nbsp;</p>
<p>6.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Wer erh&auml;lt deine Daten?</p>
<p>&nbsp;</p>
<p>Deine personenbezogenen Daten k&ouml;nnen wir an Dienstleister weitergeben, welche wir mit der Verarbeitung von Daten beauftragen. Diese sog. Auftragsverarbeiter unterliegen unseren Weisungen und sind verpflichtet, die ihnen bereitgestellten Daten ausschlie&szlig;lich wie von uns angewiesen zu verwenden (d.h. zur Bereitstellung unserer App und der damit zusammenh&auml;ngenden Services). Wir schlie&szlig;en mit Auftragsverarbeitern einen Vertrag nach Art. 28 DS-GVO, in welchem wir diese insbesondere dazu verpflichten, mit den ihnen anvertrauten Daten vertraulich umzugehen, diese angemessen zu sch&uuml;tzen und nur f&uuml;r die vereinbarten Zwecke zu verwenden. Wir setzen Auftragsverarbeiter bspw. in folgenden Bereichen ein: IT, Finanzen, Recht, Kundenservice, Marketing, Vertrieb, Logistik.</p>
<p>&nbsp;</p>
<p>Um dir das Angebot unserer Partner innerhalb unserer Apps und Services bereitstellen zu k&ouml;nnen, m&uuml;ssen wir bestimmte Daten an diese &uuml;bermitteln. Auf diese Weise erhalten unsere Partner die Best&auml;tigung, dass du ein bestimmtes Produkt gebucht hast und liefern uns im Anschluss den gew&uuml;nschten Content, z.B. indem dieser f&uuml;r dich freigeschaltet wird. Diese Partner handeln in eigener Verantwortung und erhalten solche Daten, welche zur Bereitstellung der gebuchten Inhalte in unseren Apps und Services erforderlich sind. Daneben k&ouml;nnen unsere Partner selbst&auml;ndige Messungen vornehmen, wie ihr Angebot auf unseren Apps und Services genutzt wird.</p>
<p>&nbsp;</p>
<p>Sofern unsere Dienstleister oder Partner ihren Sitz au&szlig;erhalb der Europ&auml;ischen Union (EU) bzw. des Europ&auml;ischen Wirtschaftsraums (EWR) haben (in einem sog. Drittland), treffen wir geeignete Vorkehrungen, damit diese auf einen Datenschutzstandard verpflichtet sind, der dem europ&auml;ischen im Wesentlichen entspricht. Hierf&uuml;r k&ouml;nnen wir insbesondere sog. EU-Standarddatenschutzklauseln mit unseren Partnern abschlie&szlig;en, um diese auf den Datenschutz zu verpflichten. Daneben kann auch die Europ&auml;ische Kommission den Beschluss fassen, dass der Datenschutz in einem Drittland ausreichend ist und keine weiteren Ma&szlig;nahmen zur Absicherung erforderlich sind. Eine dritte M&ouml;glichkeit zur Wahrung des Datenschutzes bei Empf&auml;ngern in Drittl&auml;ndern ist die Selbstverpflichtung des Empf&auml;ngers auf sog. verbindliche interne Datenschutzvorschriften, die zuvor von einer EU-Datenschutzaufsichtsbeh&ouml;rde freigegeben wurden.</p>
<p>&nbsp;</p>
<p>Eine Weitergabe ist zudem an unsere Berater m&ouml;glich, wenn dies zur Erf&uuml;llung unserer Gesch&auml;ftszwecke erforderlich ist (z.B. Wirtschaftspr&uuml;fer, Steuerberater, Rechtsanw&auml;lte). Diese Berater sind kraft Gesetzes zur Geheimhaltung verpflichtet.</p>
<p>&nbsp;</p>
<p>Erfolgt eine Restrukturierung, Ver&auml;u&szlig;erung, Verschmelzung oder sonstige Reorganisation unseres Unternehmens, k&ouml;nnen wir die von uns verarbeiteten personenbezogenen Daten an das erwerbende Unternehmen weitergeben.</p>
<p>&nbsp;</p>
<p>Daneben k&ouml;nnen wir Daten an staatliche Stellen, z.B. Gerichte, Strafverfolgungsbeh&ouml;rden oder Finanzaufsichtsbeh&ouml;rden, weitergeben, wenn dies der Geltendmachung, Aus&uuml;bung oder Verteidigung von Rechtsanspr&uuml;chen oder der Pr&auml;vention von rechtswidrigem Verhalten dient (z.B. Betrug oder Geldw&auml;sche) oder wir zur Weitergabe aufgrund gesetzlicher, beh&ouml;rdlicher oder gerichtlicher Anordnung verpflichtet sind.</p>
<p>&nbsp;</p>
<p>7.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Wie lange werden deine Daten gespeichert?</p>
<p>&nbsp;</p>
<p>Wir speichern deine personenbezogenen Daten nur so lange, wie es f&uuml;r die Erreichung des urspr&uuml;nglich damit verfolgten Zwecks erforderlich ist. Dies umfasst vor allem die Bereitstellung unserer Apps und Services sowie der ggf. darin gebuchten Angebote unserer Kooperationspartner.</p>
<p>&nbsp;</p>
<p>Daneben k&ouml;nnen gesetzliche Aufbewahrungsfristen bestehen (z.B. nach Handelsgesetzbuch und Abgabenordnung). Diese betreffen vor allem die buchhaltungsrelevanten Daten, z.B. Bestellbest&auml;tigungen und Rechnungen und betragen bis zu 10 Jahre.</p>
<p>&nbsp;</p>
<p>8.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Kontaktformular</p>
<p>&nbsp;</p>
<p>Auf unserer Firmenwebseite b1smarttv.com binden wir ein Formular ein, um dir eine unkomplizierte Kontaktaufnahme mit uns zu erm&ouml;glichen.</p>
<p>&nbsp;</p>
<p>Wenn du dieses Kontaktformular verwendest, k&ouml;nnen dar&uuml;ber die folgenden personenbezogenen Daten von dir verarbeitet werden:</p>
<ul>
    <li>Vorname, Nachname</li>
    <li>E-Mail-Adresse</li>
    <li>Telefonnummer (optional)</li>
    <li>Inhalt der Nachricht</li>
</ul>
<p>&nbsp;</p>
<p>Die Angabe deiner Kontaktdaten dient dem Zweck, dir auf deine Anfrage antworten zu k&ouml;nnen. Rechtsgrundlage f&uuml;r die Verarbeitung ist deine Einwilligung nach Art. 6 Abs. 1 lit. a) DS-GVO, welche du jederzeit f&uuml;r die Zukunft widerrufen kannst.</p>
<p>&nbsp;</p>
<p>Die von dir im Kontaktformular eingegebenen Daten verbleiben bei uns, bis du uns zur L&ouml;schung aufforderst, deine Einwilligung zur Speicherung widerrufst oder der Zweck f&uuml;r die Datenspeicherung entf&auml;llt (z.B. nach abgeschlossener Bearbeitung deiner Anfrage). Hiervon bleiben zwingende gesetzliche Bestimmungen &ndash; insbesondere Aufbewahrungsfristen nach dem Handelsgesetzbuch (HGB) oder der Abgabenordnung (AO) &ndash; unber&uuml;hrt.</p>
<p>&nbsp;</p>
<p>9.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Newsletter</p>
<p>&nbsp;</p>
<p>In unseren Apps und Services besteht die M&ouml;glichkeit, einen kostenfreien regelm&auml;&szlig;igen E-Mail Newsletter zu abonnieren. Um dir regelmä&szlig;ig den Newsletter zusenden zu können, benötigen wir deine E-Mail-Adresse. Im Zusammenhang mit dem Newsletterversand erfolgt eine Weitergabe deiner Daten an unseren Newsletter-Dienstleister.</p>
<p>&nbsp;</p>
<p>Für den Newsletterversand verwenden wir das sog. Double Opt-In-Verfahren. Dies bedeutet, dass wir dir erst dann einen E-Mail-Newsletter zuschicken werden, wenn du uns ausdr&uuml;cklich best&auml;tigt hast, dass du in den Versand des Newsletters einwilligst. Wir schicken dir hierf&uuml;r nach deiner Anmeldung zum Newsletter eine Best&auml;tigungs-E-Mail. In dieser wirst du gebeten, durch Anklicken eines entsprechenden Links zu best&auml;tigen, dass du k&uuml;nftig Newsletter von uns erhalten m&ouml;chtest.</p>
<p>&nbsp;</p>
<p>Dies dient der Sicherstellung, dass nur du selbst dich als Inhaber der angegebenen E-Mail-Adresse zum Newsletter anmelden kannst. Deine Bestätigung muss zeitnah nach Erhalt der Bestätigungs-E-Mail erfolgen, da andernfalls deine Newsletter-Anmeldung automatisch aus unserer Datenbank gelöscht wird.</p>
<p>&nbsp;</p>
<p>Wenn du den Newsletter abonnierst, erheben und speichern wir die Daten, welche du in das Newsletter-Formular eingibst (z.B. Nachname, Vorname, E-Mail-Adresse).</p>
<p>&nbsp;</p>
<p>Bei der Anmeldung zum Newsletter speichern wir zudem deine vom Internet Service-Provider (ISP) vergebene IP-Adresse sowie das Datum und die Uhrzeit der Anmeldung, um einen m&ouml;glichen Missbrauch deiner E-Mail- Adresse zu einem sp&auml;teren Zeitpunkt nachvollziehen zu k&ouml;nnen. Bei der zu Kontrollzwecken ausgesandten Best&auml;tigungs-E-Mail (Double-Opt in) speichern wir ebenfalls das Datum und die Uhrzeit des Klicks auf den Best&auml;tigungslink und die vom Internet Service-Provider (ISP) vergebene IP-Adresse.</p>
<p>&nbsp;</p>
<p>Die von uns bei der Anmeldung zum Newsletter erhobenen Daten werden ausschlie&szlig;lich zum Zwecke der werblichen Ansprache im Wege des Newsletters benutzt. Die Verarbeitung deiner E-Mail-Adresse für den Newsletterversand beruht nach Art. 6 Abs. 1 lit. a) DS-GVO und &sect; 7 Abs. 2 Nr. 3 UWG auf der von dir freiwillig abgegebenen und jederzeit f&uuml;r die Zukunft widerrufbaren Einwilligungserklärung. Zudem beruht die Verarbeitung nach Art. 6 Abs. 1 lit f) DS-GVO auf unserem berechtigten Interesse, den Nachweis der erforderlichen Einwilligung zu dokumentieren.</p>
<p>&nbsp;</p>
<p>Wenn du uns deine E-Mail-Adresse bei der Nutzung unserer Apps und Services zur Verf&uuml;gung gestellt hast, behalten wir uns vor, dir regelm&auml;&szlig;ig Angebote zu unseren Apps und Services, wie den bereits genutzten, aus unserem Angebot per E-Mail zuzusenden. Die Datenverarbeitung erfolgt insoweit allein auf Grundlage unseres berechtigten Interesses an personalisierter Direktwerbung gem&auml;&szlig; Art. 6 Abs. 1 lit. f) DS-GVO, &sect; 7 Abs. 3 UWG. Hast du der Nutzung deiner E-Mail-Adresse zu diesem Zweck anf&auml;nglich widersprochen, findet ein Mailversand unsererseits nicht statt. Du kannst der Nutzung deiner E-Mail-Adresse zu Werbezwecken jederzeit widersprechen, ohne dass hierf&uuml;r andere als die &Uuml;bermittlungskosten nach den Basistarifen entstehen.</p>
<p>&nbsp;</p>
<p>Deine E-Mail-Adresse wird solange gespeichert, wie du den Newsletter abonniert hast. Nach einer Abmeldung vom Newsletterversand wird deine E-Mail-Adresse gelöscht, soweit du nicht in eine weitere Nutzung deiner Daten eingewilligt hast oder eine anderweitige Rechtsgrundlage f&uuml;r eine Verarbeitung besteht.</p>
<p>&nbsp;</p>
<p>10.&nbsp; &nbsp; &nbsp; &nbsp;Welche weiteren Tools von Drittanbietern setzen wir ein?</p>
<p>&nbsp;</p>
<p>Kategorien von Tools</p>
<p>&nbsp;</p>
<p>Wir m&ouml;chten unsere Apps und Services so benutzerfreundlich wie m&ouml;glich gestalten, damit unsere Nutzer diese gerne verwenden. Hierf&uuml;r analysieren wir die Nutzung unserer Apps und Services auf anonymisierte oder pseudonymisierte Weise. Sofern wir hierf&uuml;r externe Dienstleister einsetzen, werden diese als sog. Auftragsverarbeiter f&uuml;r uns t&auml;tig. Dies bedeutet, dass sich diese Dienstleister vertraglich dazu verpflichten, personenbezogene Daten unserer Nutzer nur auf unsere Anweisung hin zu verarbeiten sowie einen angemessenen Datenschutzstandard einzuhalten. Diese Tools verwenden wir auf der Grundlage deiner ausdr&uuml;cklichen Einwilligung (Art. 6 Abs. 1 lit. a) DS-GVO). Tools, welche wir zu diesen Zwecken einsetzen, geh&ouml;ren zur Kategorie &bdquo;Analyse&ldquo;.</p>
<p>&nbsp;</p>
<p>Marketing-Tools k&ouml;nnen verwendet werden, um den Nutzern unserer Apps und Services interessenbasierte Werbung anzuzeigen und die Effektivit&auml;t von Werbekampagnen zu messen. Mithilfe dieser Cookies k&ouml;nnen Besucher auf externen Webseiten wiedererkannt und ihnen dort personalisierte Anzeigen eingeblendet werden. Zudem k&ouml;nnen wir aufgrund deines Nutzungsverhaltens innerhalb der Apps und Services f&uuml;r dich relevante Produkte anzeigen. Auch solche Tools setzen wir auf der Grundlage deiner ausdr&uuml;cklichen Einwilligung ein (Art. 6 Abs. 1 lit. a) DS-GVO).</p>
<p>&nbsp;</p>
<p>Wiederum andere Kategorien von Tools sind f&uuml;r den Betrieb unserer Apps und Services erforderlich. Es besteht insoweit keine Opt-out-M&ouml;glichkeit (z.B. im Falle von Content-Delivery-Networks oder Tools zur Gew&auml;hrleistung der App-Sicherheit). Die Rechtsgrundlage ist unser berechtigtes Interesse an der Bereitstellung unserer Apps und Services (Art. 6 Abs. 1 lit. f DS-GVO). Diese Tools sind in der Kategorie &bdquo;Erforderlich&ldquo; genannt.</p>
<p>&nbsp;</p>
<p>Kategorien von Cookies</p>
<p>&nbsp;</p>
<p>Soweit wir f&uuml;r den Einsatz solcher Tools sog. Cookies einsetzen, erfolgt dies auf folgende Weise:</p>
<p>&nbsp;</p>
<p>Cookies sind kleine Dateien, die auf deinem Endger&auml;t abgelegt werden und von unseren Apps und Services gespeichert werden. Einige Funktionen unserer Apps und Services k&ouml;nnen ohne den Einsatz technisch notwendiger Cookies nicht angeboten werden. Andere Cookies erm&ouml;glichen uns dagegen verschiedene Analysen (vgl. die o.g. Zwecke f&uuml;r den Einsatz von Drittanbieter-Tools). So k&ouml;nnen einige Cookies das von dir verwendete App-Profil bei einem erneuten Besuch wiedererkennen und verschiedene Informationen an uns &uuml;bermitteln. Cookies richten auf deinem Endger&auml;t keinen Schaden an. Sie k&ouml;nnen keine Programme ausf&uuml;hren und keine Viren enthalten. In unseren Apps und Services werden verschiedene Arten von Cookies verwendet, deren Art und Funktion wir gerne im Folgenden erl&auml;utern m&ouml;chten.</p>
<p>&nbsp;</p>
<p>Tempor&auml;re Cookies / Session-Cookies</p>
<p>In unseren Apps und Services werden sog. tempor&auml;re Cookies bzw. Session-Cookies&nbsp;verwendet, welche automatisch gel&ouml;scht werden, sobald du die App oder den Service schlie&szlig;t. Mithilfe dieser Art von Cookies ist es m&ouml;glich, deine Sitzungs-ID (&bdquo;Session-ID&ldquo;) zu erfassen. Dadurch lassen sich verschiedene Anfragen aus der App oder dem Service einer gemeinsamen Sitzung zuordnen und es ist m&ouml;glich, dein Endger&auml;t bei sp&auml;teren Webseitenbesuchen wiederzuerkennen. Diese Session-Cookies verfallen nach Ablauf der Sitzung.</p>
<p>&nbsp;</p>
<p>Dauerhafte Cookies</p>
<p>Zudem setzen wir sog. permanente oder dauerhafte Cookies ein. Dauerhafte Cookies sind Cookies, welche &uuml;ber einen l&auml;ngeren Zeitraum in der App oder dem Service gespeichert werden und Informationen &uuml;bermitteln k&ouml;nnen. Die jeweilige Speicherdauer unterscheidet sich je nach Cookie.</p>
<p>&nbsp;</p>
<p>Eine Liste der in unseren Apps und Services zu den o.g. Zwecken verwendeten Drittanbietertools finden Sie in der Anlage zu dieser Datenschutzerkl&auml;rung.</p>
<p>&nbsp;</p>
<p>11.&nbsp; &nbsp; &nbsp; &nbsp;Google Analytics 4</p>
<p>&nbsp;</p>
<p>Wir setzen in unseren Apps und Services das Tracking-Tool &bdquo;Google Analytics 4&ldquo; der Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland, Tel: +353 1 543 1000, Fax: +353 1 686 5660, E-Mail: support-deutschland@google.com (&bdquo;Google&ldquo;) ein.</p>
<p>&nbsp;</p>
<p>Google Analytics 4 verwendet JavaScript und Pixel, um Informationen auf deinem Endger&auml;t auszulesen, sowie Cookies, um Informationen auf deinem Endger&auml;t zu speichern. Dies dient dazu, dein Nutzungsverhalten zu analysieren und unsere Apps und Services zu verbessern. Die Zugriffsdaten werden von Google in unserem Auftrag zu pseudonymen Nutzungsprofilen zusammengefasst und an einen Google-Server in den USA &uuml;bertragen. Google wird diese Informationen benutzen, um deine Nutzung unserer Apps und Services systematisch auszuwerten und um Reports &uuml;ber die Aktivit&auml;ten auf unseren unserer Apps und Services zusammenzustellen.</p>
<p>&nbsp;</p>
<p>Im Rahmen der Auswertung nutzt Google Analytics 4 auch k&uuml;nstliche Intelligenz wie maschinelles Lernen, um die Daten automatisch zu analysieren und zu optimieren. Zum Beispiel werden Conversions modelliert, wenn nicht gen&uuml;gend Daten vorhanden sind. Du findest weitere Informationen dazu in der entsprechenden Google-Dokumentation. Die Datenauswertungen erfolgen automatisiert durch k&uuml;nstliche Intelligenz oder anhand von individuell festgelegten Kriterien.</p>
<p>&nbsp;</p>
<p>Im Rahmen der Nutzungsanalyse von Google Analytics 4 werden die erhobenen Daten mit Informationen aus der Google Search Console angereichert und mit den Daten von Google Ads verkn&uuml;pft. Dies erm&ouml;glicht uns insbesondere die Messung des Erfolgs unserer Werbekampagnen, auch bekannt als Conversions.</p>
<p>&nbsp;</p>
<p>Es k&ouml;nnen folgende Daten verarbeitet werden:</p>
<ul>
    <li>IP-Adresse;</li>
    <li>Referrer-URL (zuvor besuchte Seite);</li>
    <li>aufgerufene Seiten (Datum, Uhrzeit, URL, Titel, Verweildauer);</li>
    <li>heruntergeladene Dateien;</li>
    <li>angeklickte Links zu anderen Websites;</li>
    <li>Erreichung von bestimmten Zielen (Conversions);</li>
    <li>technische Informationen (Betriebssystem; Browsertyp, -version und -sprache; Ger&auml;tetyp, -marke, -modell und -aufl&ouml;sung);</li>
    <li>ungef&auml;hrer Standort (Land, Region und ggf. Stadt, ausgehend von anonymisierter IP-Adresse).</li>
</ul>
<p>&nbsp;</p>
<p>Wir nutzen Google Analytics 4 mit aktivierter IP-Anonymisierung. Damit werden die IP-Adressen um das letzte Oktett gek&uuml;rzt (Bsp: 192.168.79.***; sog. IP-Masking). Eine Zuordnung der gek&uuml;rzten IP-Adresse zum aufrufenden Rechner bzw. Endger&auml;ts des Nutzers ist nicht mehr m&ouml;glich.</p>
<p>&nbsp;</p>
<p>Die erzeugten Informationen &uuml;ber deine Benutzung unserer Apps und Services werden in der Regel an einen Server von Google in den USA &uuml;bertragen und dort gespeichert. Google ist aufgrund von sog. EU-Standarddatenschutzklauseln zur Einhaltung eines Datenschutzstandards verpflichtet, welches dem europ&auml;ischen im Wesentlichen entspricht.</p>
<p>&nbsp;</p>
<p>Der Dienst Google Analytics 4 dient der Analyse des Nutzungsverhaltens unserer Apps und Services. Rechtsgrundlage ist deine Einwilligung nach Art. 6 Abs. 1 lit. a) DS-GVO.&nbsp;Die gespeicherten Daten werden von uns gel&ouml;scht, sobald sie f&uuml;r die Analysezwecke nicht mehr ben&ouml;tigt werden. In unserem Fall betr&auml;gt die Speicherdauer maximal 24 Monate.</p>
<p>&nbsp;</p>
<p>N&auml;here Informationen zu den Nutzungsbedingungen von Google Analytics 4:</p>
<p>www.google.com/analytics/terms/de.html</p>
<p>&nbsp;</p>
<p>N&auml;here Informationen zum Datenschutz von Google Analytics 4:</p>
<p>https://support.google.com/analytics/answer/6004245?hl=de</p>
<p>&nbsp;</p>
<p>12.&nbsp; &nbsp; &nbsp; &nbsp;Youtube</p>
<p>&nbsp;</p>
<p>Wir binden YouTube-Videos in unsere Apps und Services ein, welche unter&nbsp;<a href="http://www.youtube.com">http://www.youtube.com</a>&nbsp;gespeichert sind und von unseren Apps aus direkt abspielbar sind. YouTube ist ein Dienst des Unternehmens Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland, Tel: +353 1 543 1000, Fax: +353 1 686 5660, E-Mail:&nbsp;<a href="mailto:support-deutschland@google.com">support-deutschland@google.com</a>&nbsp;(&quot;Google&quot;).</p>
<p>&nbsp;</p>
<p>YouTube erhebt Ihre IP-Adresse, das Datum nebst Uhrzeit sowie Informationen zur von Ihnen besuchten Internetseite und dem aufgerufenen Video. Dies erfolgt unabh&auml;ngig davon, ob YouTube ein Nutzerkonto bereitstellt, &uuml;ber das Sie eingeloggt sind, oder ob kein Nutzerkonto besteht. Au&szlig;erdem wird eine Verbindung zu dem Werbenetzwerk von Google hergestellt.</p>
<p>&nbsp;</p>
<p>Solange ein von uns eingebundenes YouTube-Video in unseren Apps angezeigt wird, ohne dass das Video abgespielt wird, werden aufgrund der YouTube-Funktion &bdquo;Erweiterter Datenschutzmodus&ldquo; noch keine Daten an YouTube &uuml;bermittelt. Eine &Uuml;bermittlung erfolgt erst, wenn Sie das Video tats&auml;chlich starten.</p>
<p>&nbsp;</p>
<p>Um die von Ihnen gew&uuml;nschte Einstellung hinsichtlich der Wiedergabe von Videos und der Daten&uuml;bermittlung an YouTube zu speichern, wird von uns ein Cookie gesetzt. Diese Cookies enthalten keine personenbezogenen Daten, sie enthalten lediglich anonymisierte Daten zur Anpassung in unserer App.</p>
<p>&nbsp;</p>
<p>Sollten Sie gleichzeitig bei YouTube eingeloggt sein, kann YouTube die Verbindungsinformationen Ihrem YouTube-Konto zuordnen und diese zum Zweck der personalisierten Werbung verwenden.</p>
<p>&nbsp;</p>
<p>Weitere Informationen erhalten Sie in der Datenschutzerkl&auml;rung von Google:&nbsp;<a href="http://www.google.de/intl/de/policies/privacy/">http://www.google.de/intl/de/policies/privacy/</a></p>
<p>&nbsp;</p>
<p>Wir nutzen YouTube, um Ihnen Videos in unseren Apps und Services anzeigen zu k&ouml;nnen. Rechtsgrundlage der Verarbeitung ist Ihre Einwilligung nach Art. 6 Abs. 1 lit. a DS-GVO.</p>
<p>&nbsp;</p>
<p>13.&nbsp; &nbsp; &nbsp; &nbsp;Welche gesetzlichen Rechte hast du?</p>
<p>&nbsp;</p>
<p>Du hast folgende gesetzliche Rechte zum Datenschutz:</p>
<p>&nbsp;</p>
<p>Recht auf Widerruf einer datenschutzrechtlichen Einwilligung f&uuml;r die Zukunft (Art. 7 Abs. 3 DS-GVO)</p>
<p>Immer dann, wenn eine Verarbeitung deiner Daten auf einer ausdr&uuml;cklichen Einwilligung von dir beruht, kannst du diese Einwilligung jederzeit mit Wirkung f&uuml;r die Zukunft widerrufen. Bereits auf der Grundlage einer Einwilligung erfolgte Datenverarbeitungen bleiben jedoch rechtm&auml;&szlig;ig.</p>
<p>&nbsp;</p>
<p>Recht auf Auskunft &uuml;ber die Verarbeitung Ihrer Daten (Art. 15 DS-GVO)</p>
<p>Du hast das Recht, von uns eine Best&auml;tigung dar&uuml;ber zu verlangen, ob wir personenbezogene Daten von dir verarbeiten. Wenn dies der Fall ist, hast du Anspruch auf Mitteilung der weiteren Umst&auml;nde dieser Verarbeitung, darunter deren Zweck, die verarbeiteten Datenkategorien, die Empf&auml;nger der Daten, die Speicherdauer der Daten sowie die Herkunft der Daten.</p>
<p>&nbsp;</p>
<p>Recht auf Berichtigung Ihrer Daten (Art. 16 DS-GVO)</p>
<p>Du hast das Recht auf Berichtigung unrichtiger Daten. Daneben hast du ein Recht auf Vervollst&auml;ndigung unvollst&auml;ndiger Daten, sofern dies f&uuml;r die Verarbeitung erforderlich ist.</p>
<p>&nbsp;</p>
<p>Recht auf L&ouml;schung Ihrer Daten (Art. 17 DS-GVO)</p>
<p>Du hast das Recht auf L&ouml;schung deiner Daten, wenn</p>
<ul>
    <li>diese f&uuml;r die urspr&uuml;nglichen Verarbeitungszwecke nicht mehr notwendig sind,</li>
    <li>du deine Einwilligung in die Verarbeitung der Daten widerrufen hast,</li>
    <li>du einen Widerspruch gegen die Verarbeitung Ihrer Daten erkl&auml;rt hast,</li>
    <li>die Daten unrechtm&auml;&szlig;ig verarbeitet wurden, oder</li>
    <li>eine gesetzliche Pflicht zur L&ouml;schung besteht.</li>
</ul>
<p>&nbsp;</p>
<p>Haben wir solche Daten zuvor &ouml;ffentlich gemacht, dann hast du auch einen Anspruch darauf, dass wir die weiteren Datenverantwortlichen, welche deine Daten verarbeiten, &uuml;ber dein L&ouml;schverlangen informieren.</p>
<p>&nbsp;</p>
<p>In bestimmten F&auml;llen ist das Recht auf L&ouml;schung jedoch ausgeschlossen, z.B. wenn die Daten aufgrund einer rechtlichen Verpflichtung verarbeitet werden m&uuml;ssen, oder f&uuml;r die Geltendmachung, Aus&uuml;bung oder Verteidigung von Rechtsanspr&uuml;chen erforderlich sind.</p>
<p>&nbsp;</p>
<p>Recht auf Einschr&auml;nkung der Verarbeitung Ihrer Daten (Art. 18 DS-GVO)</p>
<p>Du hast das Recht, die Verarbeitung deiner Daten einschr&auml;nken zu lassen (= diese zu sperren), wenn</p>
<ul>
    <li>du deren Richtigkeit bestreitest und solange wir dies nachpr&uuml;fen,</li>
    <li>die Daten unrechtm&auml;&szlig;ig verarbeitet wurden,</li>
    <li>du die Daten zur Geltendmachung, Aus&uuml;bung oder Verteidigung von Rechtsanspr&uuml;chen ben&ouml;tigst oder</li>
    <li>du Widerspruch gegen die Verarbeitung der Daten eingelegt hast und solange wir diesen pr&uuml;fen.</li>
</ul>
<p>&nbsp;</p>
<p>Recht auf &Uuml;bertragbarkeit Ihrer Daten (Art. 20 DS-GVO)</p>
<p>Du hast das Recht, solche personenbezogenen Daten, die du uns bereitgestellt hast, in einem strukturierten, g&auml;ngigen und maschinenlesbaren Format zu erhalten.</p>
<p>&nbsp;</p>
<p>Du hast zudem das Recht, solche Daten einem anderen Datenverantwortlichen zu &uuml;bermitteln, wenn die Verarbeitung durch uns zuvor auf deiner Einwilligung oder auf einem Vertragsverh&auml;ltnis beruhte und die Verarbeitung mithilfe automatisierter Verfahren erfolgte.</p>
<p>&nbsp;</p>
<p>Du hast auch einen Anspruch darauf, dass wir solche Daten direkt an einen anderen Datenverantwortlichen &uuml;bermitteln, wenn dies technisch machbar ist.</p>
<p>&nbsp;</p>
<p>Recht auf Widerspruch gegen die Verarbeitung Ihrer Daten (Art. 21 DS-GVO)</p>
<p>Du hast das Recht, aus pers&ouml;nlichen Gr&uuml;nden einer Verarbeitung deiner Daten zu widersprechen, wenn wir diese auf der Grundlage unserer sog. berechtigter Interessen (nach Art. 6 Abs. 1 lit. f) DS-GVO) verarbeiten. In diesem Fall verarbeiten wir deine Daten nicht mehr, es sei denn, wir k&ouml;nnen zwingende Gr&uuml;nde f&uuml;r eine weitere Verarbeitung nachweisen, die die von dir angef&uuml;hrten Gr&uuml;nde &uuml;berwiegen.</p>
<p>&nbsp;</p>
<p>Daneben hast du das Recht, jederzeit einer Verwendung deiner Daten zum Zweck der Direktwerbung zu widersprechen.</p>
<p>&nbsp;</p>
<p>Recht auf nicht ausschlie&szlig;lich automatisierte Entscheidungsfindung (Art. 22 DS-GVO)</p>
<p>Du hast das Recht, nicht von einer ausschlie&szlig;lich automatisierten Entscheidungsfindung betroffen zu sein, wenn von dieser Verarbeitung rechtliche oder &auml;hnlich belastende Wirkungen ausgehen. Dies gilt nicht, wenn die automatisierte Entscheidungsfindung f&uuml;r den Abschluss oder die Durchf&uuml;hrung eines Vertrags mit uns erforderlich ist, gesetzlich erlaubt ist oder mit deiner ausdr&uuml;cklichen Einwilligung erfolgt.</p>
<p>&nbsp;</p>
<p>Erfolgt hiernach eine automatisierte Entscheidungsfindung, hast du das Recht auf ein Eingreifen in die automatisierte Verarbeitung durch eine Person, auf Darlegung deines Standpunkts und auf Anfechtung der automatisiert getroffenen Entscheidung.</p>
<p>&nbsp;</p>
<p>Beschwerderecht</p>
<p>Daneben kannst du auch eine Beschwerde bei der Datenschutz-Aufsichtsbeh&ouml;rde einlegen, wenn du der Auffassung bist, eine Verarbeitung versto&szlig;e gegen gesetzliche Vorschriften.</p>
<p>&nbsp;</p>
<p>14. Datenschutz auf dem Schweizer Markt gem&auml;&szlig; DSGVO</p>
<p>&nbsp;</p>
<p>Wir legen gro&szlig;en Wert auf den Schutz personenbezogener Daten und befolgen die Bestimmungen der Datenschutz-Grundverordnung (DSGVO) der Europ&auml;ischen Union, um den Schutz der Privatsph&auml;re und der Rechte der Kunden sicherzustellen. Diese strengeren Datenschutzstandards gelten nicht nur f&uuml;r unsere Kunden innerhalb der EU, sondern auch f&uuml;r Kunden auf dem Schweizer Markt. So gew&auml;hrleisten wir gleichzeitig die Einhaltung des schweizerischen Datenschutzgesetzes.</p>
<p>&nbsp;</p>
<p>15.&nbsp; &nbsp; &nbsp; &nbsp;&Auml;nderung dieser Datenschutzerkl&auml;rung</p>
<p>&nbsp;</p>
<p>Diese Datenschutzerkl&auml;rung k&ouml;nnen wir mit der Zeit aktualisieren, z.B. um sie an &Auml;nderungen der Rechtslage oder neue Funktionen der Apps und Services anzupassen. Im Falle wesentlicher &Auml;nderungen werden wir dich hierauf gesondert aufmerksam machen, z.B. per E-Mail oder per In-App-Benachrichtigung.</p>
<p>&nbsp;</p>
<p>Stand: 26.10.2023</p>
<p><br>&nbsp;</p>
<p>&nbsp;</p>
<p>Anlage: In den Apps und Services verwendete Drittanbieter-Tools / Cookies</p>
<p>&nbsp;</p>
<table>
    <tbody>
        <tr>
            <td style="width: 103.2pt;border: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Tool</p>
            </td>
            <td style="width: 114.75pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Zweck</p>
            </td>
            <td style="width: 112.4pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Speicherdauer</p>
            </td>
            <td style="width: 122.75pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Datenarten</p>
            </td>
        </tr>
        <tr>
            <td style="width: 103.2pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Google Analytics&nbsp;4</p>
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>&nbsp;</p>
            </td>
            <td style="width: 114.75pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Analyse</p>
            </td>
            <td style="width: 112.4pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Bis zu 24 Monate</p>
            </td>
            <td style="width: 122.75pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Analysedaten (vgl. oben Abschnitt 11)</p>
            </td>
        </tr>
        <tr>
            <td style="width: 103.2pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Youtube</p>
            </td>
            <td style="width: 114.75pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Einbindung Video</p>
            </td>
            <td style="width: 112.4pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Bis zu 24 Monate</p>
            </td>
            <td style="width: 122.75pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Analysedaten (vgl. oben Abschnitt 12)</p>
            </td>
        </tr>
        <tr>
            <td style="width: 103.2pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Plenigo, Stripe, PayPal</p>
            </td>
            <td style="width: 114.75pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Erforderlich:</p>
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Account Management und Zahlungsdienstleister</p>
            </td>
            <td style="width: 112.4pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Zahlungsabwicklung + ggf. gesetzliche Fristen</p>
            </td>
            <td style="width: 122.75pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Name, Anschrift, E-Mail-Adresse, Kunden-ID, Buchungs- und Transaktionsdaten, Zahlungsinformationen</p>
            </td>
        </tr>
    </tbody>
</table>
<p>&nbsp;</p>
<p>Die Datenschutzerkl&auml;rungen der jeweiligen Anbieter kannst du abrufen unter:</p>
<p>&nbsp;</p>
<table>
    <tbody>
        <tr>
            <td style="width: 113.15pt;border: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Anbieter</p>
            </td>
            <td style="width: 290.6pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Datenschutzerkl&auml;rung</p>
            </td>
        </tr>
        <tr>
            <td style="width: 113.15pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Google</p>
            </td>
            <td style="width: 290.6pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'><a href="https://policies.google.com/privacy?hl=de">https://policies.google.com/privacy?hl=de</a>&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td style="width: 113.15pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Plenigo</p>
            </td>
            <td style="width: 290.6pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'><a href="https://www.plenigo.com/datenschutz/">https://www.plenigo.com/datenschutz/</a>&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td style="width: 113.15pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Stripe</p>
            </td>
            <td style="width: 290.6pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'><a href="https://stripe.com/de/privacy">https://stripe.com/de/privacy</a>&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td style="width: 113.15pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'>Paypal</p>
            </td>
            <td style="width: 290.6pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-right:0cm;margin-left:0cm;font-size:16px;font-family:"Calibri",sans-serif;margin-top:0cm;margin-bottom:0cm;font-size:11.0pt;text-align:justify;line-height:  150%;'><a href="https://www.paypal.com/de/webapps/mpp/ua/privacy-full">https://www.paypal.com/de/webapps/mpp/ua/privacy-full</a>&nbsp;</p>
            </td>
        </tr>
    </tbody>
</table>
<p>&nbsp;</p>
            """,
        },
        {
            "locales": ["en-US"],
            "value": """<p>Privacy Policy</p>
<p>&nbsp;</p>
<p>The protection of your personal data is very important to us. Below, we would like to inform you about the data we process and how we process it when you use our services.</p>
<p>&nbsp;</p>
<p>1.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;How to contact us?</p>
<p>&nbsp;</p>
<p>The data processing entity and the party responsible for processing your data in terms of data protection is:</p>
<p>&nbsp;</p>
<p>B1 SmartTV GmbH</p>
<p>Ainmillerstr. 28</p>
<p>80801 München</p>
<p>E-Mail: info@b1smarttv.com</p>
<p>&nbsp;</p>
<p>2.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;How do you reach our data protection officer?</p>
<p>&nbsp;</p>
<p>You are welcome to contact our data protection officer at any time if you have any questions regarding data protection:</p>
<p>&nbsp;</p>
<p>Dr. Georg F. Schr&ouml;der, LL.M.</p>
<p>legal data Schr&ouml;der Rechtsanwaltsgesellschaft mbH</p>
<p>Prannerstr. 1</p>
<p>80333 M&uuml;nchen</p>
<p>Tel.: +49 89 954 597 520</p>
<p>E-Mail: datenschutz@legaldata.law</p>
<p>&nbsp;</p>
<p>3.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Which categories of data do we use?</p>
<p>&nbsp;</p>
<p>We process the following categories of data when you use our apps and services:</p>
<p>&nbsp;</p>
<p>Technically required data</p>
<p>To be able to provide our apps and services, we process a range of technical data. These are mainly necessary to establish a connection between your device and our servers. This includes your IP address, the page accessed within our apps and services, date and time of access, and potentially additional device-related data such as the type of smartphone/smart TV or language settings.</p>
<p>&nbsp;</p>
<p>Account-Data</p>
<p>We primarily process your login credentials, including the account name, account ID, email addresses, and address, and potentially payment information such as account or credit card numbers, and payment history, to provide you with access to our apps and services.</p>
<p>&nbsp;</p>
<p>Usage Data</p>
<p>When you create an account with us, we may display recommendations tailored to your interests based on your activity history. This includes the accessed content, duration of access, and search history. Additionally, we process the ratings and reviews you submit.</p>
<p>&nbsp;</p>
<p>Marketing Data</p>
<p>This mainly includes your advertising preferences, cookie settings, and related device, advertising, and cookie IDs. We also process the data categories mentioned in sections 10 and 11 of this privacy policy.</p>
<p>&nbsp;</p>
<p>Statistical Data</p>
<p>Furthermore, we collect statistical data on the usage of our apps and services. This includes, for example, the type of device you use to access our apps and services, the operating system, and language settings. Personal data of our users is anonymized for this purpose and contributes to an overall statistical analysis. Based on this, no conclusions can be drawn about individual users.</p>
<p>&nbsp;</p>
<p>4.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Where these data come from?</p>
<p>&nbsp;</p>
<p>Most of the data we process about you is provided by you when you open an account or use our apps and services. This includes, for example, your account information, payment details, or advertising preferences.</p>
<p>&nbsp;</p>
<p>Certain technical data necessary for the provision of our apps and services are automatically collected from your device or internet provider (e.g., IP address).</p>
<p>&nbsp;</p>
<p>In addition, certain data may be transmitted to us by our cooperation partners whose offerings are integrated into our apps and services. This ensures that you can use our partners&apos; products without leaving our apps and services (e.g., confirmation of a product booking, payment processing).</p>
<p>&nbsp;</p>
<p>5.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;For what purposes do we use your data?</p>
<p>&nbsp;</p>
<p>We process your data:</p>
<ul class="decimal_type">
    <li>based on your explicit consent (Art. 6(1)(a) GDPR) &ndash; e.g., pseudonymous cookie IDs for personalized advertising, email addresses for sending newsletters,</li>
    <li>for the performance of a contract with you (Art. 6(1)(b) GDPR) &ndash; e.g., billing and payment data, booked services (including those of our cooperation partners),</li>
    <li>to comply with legal obligations (Art. 6(1)(c) GDPR) &ndash; e.g., order confirmations and invoices,</li>
    <li>to pursue our legitimate interests (Art. 6(1)(f) GDPR); in such cases, we will inform you of our legitimate interests in processing the data &ndash; e.g., technical data to ensure system security.</li>
</ul>
<p>&nbsp;</p>
<p>6.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Who receives your data?</p>
<p>&nbsp;</p>
<p>We may disclose your personal data to service providers who process data on our behalf. These processors are contractually obligated to follow our instructions and are only permitted to use the data provided to them for the purposes of providing our app and related services. We enter into contracts with processors in accordance with Art. 28 GDPR, in which we particularly oblige them to handle the entrusted data confidentially, protect it adequately, and only use it for the agreed purposes. We use processors, for example, in the following areas: IT, finance, legal, customer service, marketing, sales, and logistics.</p>
<p>&nbsp;</p>
<p>To provide you with the offerings of our partners within our apps and services, we may need to transmit certain data to them. This way, our partners receive confirmation that you have booked a specific product and subsequently provide us with the desired content, such as unlocking it for you. These partners act independently and receive only the data necessary to provide the booked content in our apps and services. Additionally, our partners may conduct independent measurements to analyze how their offerings are used within our apps and services.</p>
<p>&nbsp;</p>
<p>If our service providers or partners are located outside the European Union (EU) or the European Economic Area (EEA) (in a so-called third country), we take appropriate measures to ensure that they are subject to a level of data protection that is essentially equivalent to European standards. We can achieve this by entering into EU standard data protection clauses with our partners, thereby binding them to data protection obligations. Furthermore, the European Commission may adopt a decision stating that the data protection in a third country is adequate, and no further safeguards are required. Another means of ensuring data protection when transferring data to recipients in third countries is the recipient&apos;s commitment to binding corporate rules on data protection, which have been approved by an EU data protection supervisory authority.</p>
<p>&nbsp;</p>
<p>Furthermore, disclosure to our advisors is possible if it is necessary to fulfill our business purposes (e.g., auditors, tax consultants, lawyers). These advisors are legally bound to confidentiality.</p>
<p>&nbsp;</p>
<p>In the event of restructuring, sale, merger, or other reorganization of our company, we may transfer the personal data processed by us to the acquiring company.</p>
<p>&nbsp;</p>
<p>Furthermore, we may disclose data to governmental authorities, such as courts, law enforcement agencies, or financial supervisory authorities, if necessary for the establishment, exercise, or defense of legal claims or for the prevention of illegal activities (e.g., fraud or money laundering), or if we are required to do so by law, authorities, or court orders.</p>
<p>&nbsp;</p>
<p>7.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;How long will your data be stored?</p>
<p>&nbsp;</p>
<p>We only store your personal data for as long as it is necessary to achieve the originally intended purpose. This includes primarily the provision of our apps and services, as well as any offers from our cooperation partners that you may have booked through them.</p>
<p>&nbsp;</p>
<p>In addition, there may be legal retention periods (e.g., according to the Commercial Code and the Fiscal Code). These mainly concern accounting-related data such as order confirmations and invoices and can last up to 10 years.</p>
<p>&nbsp;</p>
<p>8.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Contact Form</p>
<p>&nbsp;</p>
<p>On our company website b1smarttv.com, we include a form to enable easy contact with us.</p>
<p>&nbsp;</p>
<p>If you use this contact form, the following personal data may be processed:</p>
<ul>
    <li>First name, last name</li>
    <li>Email address</li>
    <li>Telephone number (optional)</li>
    <li>Content of the message</li>
</ul>
<p>&nbsp;</p>
<p>Providing your contact details is necessary to respond to your inquiry. The legal basis for processing is your consent according to Art. 6(1)(a) of the GDPR, which you can revoke at any time for the future.</p>
<p>&nbsp;</p>
<p>The data you enter in the contact form will remain with us until you request deletion, revoke your consent to storage, or the purpose for data storage no longer applies (e.g., after completing the processing of your request). Mandatory legal provisions, especially retention periods under the Commercial Code (HGB) or the Fiscal Code (AO), remain unaffected.</p>
<p>&nbsp;</p>
<p>9.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Newsletter</p>
<p>&nbsp;</p>
<p>In our apps and services, there is an option to subscribe to a free regular email newsletter. To regularly send you the newsletter, we need your email address. In connection with the newsletter dispatch, your data will be transferred to our newsletter service provider.</p>
<p>&nbsp;</p>
<p>For newsletter distribution, we use the double opt-in procedure. This means that we will only send you an email newsletter if you have explicitly confirmed that you consent to receiving the newsletter. After registering for the newsletter, you will receive a confirmation email asking you to confirm your desire to receive newsletters from us by clicking on a corresponding link.</p>
<p>&nbsp;</p>
<p>This is done to ensure that only you, as the owner of the provided email address, can subscribe to the newsletter. Your confirmation must be made promptly upon receipt of the confirmation email; otherwise, your newsletter registration will be automatically deleted from our database.</p>
<p>&nbsp;</p>
<p>When you subscribe to the newsletter, we collect and store the data you enter in the newsletter form (e.g., last name, first name, email address).</p>
<p>&nbsp;</p>
<p>During newsletter registration, we also store your IP address assigned by the Internet service provider (ISP), as well as the date and time of registration, to be able to trace any potential misuse of your email address at a later point. When the confirmation email (double opt-in) is sent for control purposes, we also store the date and time of clicking on the confirmation link, as well as the IP address assigned by the Internet service provider (ISP).</p>
<p>&nbsp;</p>
<p>The data collected during newsletter registration is used exclusively for the purpose of sending advertising material via newsletters. The processing of your email address for newsletter delivery is based on your voluntarily given and revocable consent according to Art. 6(1)(a) of the GDPR and &sect; 7(2)(3) of the German Act Against Unfair Competition (UWG). Furthermore, the processing is based on our legitimate interest in documenting the necessary consent according to Art. 6(1)(f) of the GDPR.</p>
<p>&nbsp;</p>
<p>When subscribing to the newsletter, we also store your IP address assigned by the Internet Service Provider (ISP), as well as the date and time of registration, in order to trace any potential misuse of your email address at a later point. In the confirmation email sent for verification purposes (double opt-in), we also store the date and time of clicking the confirmation link, as well as the IP address assigned by the ISP.</p>
<p>&nbsp;</p>
<p>The data collected from you during the newsletter registration is exclusively used for the purpose of sending promotional content through the newsletter. The processing of your email address for the purpose of newsletter delivery is based on your voluntarily given consent according to Art. 6(1)(a) of the General Data Protection Regulation (DS-GVO) and &sect; 7(2) No. 3 of the German Unfair Competition Act (UWG), which can be revoked by you at any time for the future. Furthermore, the processing is based on our legitimate interest in documenting the necessary consent according to Art. 6(1)(f) DS-GVO.</p>
<p>&nbsp;</p>
<p>If you have provided us with your email address while using our apps and services, we reserve the right to regularly send you offers regarding our apps and services, including those you have already used, via email. The data processing for this purpose is solely based on our legitimate interest in personalized direct advertising according to Art. 6(1)(f) DS-GVO and &sect; 7(3) UWG. If you initially objected to the use of your email address for this purpose, we will not send you any emails. You can object to the use of your email address for advertising purposes at any time without incurring any costs other than the transmission costs according to the basic tariffs.</p>
<p>&nbsp;</p>
<p>Your email address will be stored for as long as you have subscribed to the newsletter. After unsubscribing from the newsletter, your email address will be deleted unless you have given consent for further use of your data or there is another legal basis for processing.</p>
<p>&nbsp;</p>
<p>10.&nbsp; &nbsp; &nbsp; &nbsp;Which other third-party tools do we use?</p>
<p>&nbsp;</p>
<p>Categories of Tools</p>
<p>&nbsp;</p>
<p>We aim to make our apps and services as user-friendly as possible so that our users enjoy using them. To achieve this, we analyze the usage of our apps and services in an anonymized or pseudonymized manner. If we engage external service providers for this purpose, they act as processors on our behalf. This means that these service providers are contractually obligated to process personal data of our users only according to our instructions and to maintain an adequate level of data protection. We use these tools based on your explicit consent (Art. 6(1)(a) of the General Data Protection Regulation (DS-GVO)). The tools we use for these purposes fall under the category of &quot;Analytics.&quot;</p>
<p>&nbsp;</p>
<p>Marketing tools may be used to display interest-based advertisements to users of our apps and services and measure the effectiveness of advertising campaigns. With the help of these cookies, visitors can be recognized on external websites, and personalized ads can be displayed to them there. Additionally, based on your usage behavior within the apps and services, we can show you relevant products. We also use such tools based on your explicit consent (Art. 6(1)(a) DS-GVO).</p>
<p>&nbsp;</p>
<p>There are other categories of tools that are necessary for the operation of our apps and services. In these cases, there is no opt-out option (e.g., in the case of content delivery networks or tools to ensure app security). The legal basis is our legitimate interest in providing our apps and services (Art. 6(1)(f) DS-GVO). These tools are mentioned in the &quot;Required&quot; category.</p>
<p>&nbsp;</p>
<p>Categories of Cookies</p>
<p>&nbsp;</p>
<p>If we use so-called cookies for the implementation of such tools, we do so in the following manner:</p>
<p>&nbsp;</p>
<p>Cookies are small files that are stored on your device by our apps and services. Some features of our apps and services cannot be offered without the use of technically necessary cookies. Other cookies, however, enable us to perform various analyses (as mentioned above for the use of third-party tools). For example, some cookies can recognize your app profile during a subsequent visit and transmit various information to us. Cookies do not cause any harm to your device. They cannot execute programs or contain viruses. Various types of cookies are used in our apps and services, and we would like to explain their types and functions below.</p>
<p>&nbsp;</p>
<p>Temporary Cookies / Session Cookies</p>
<p>Our apps and services use so-called temporary cookies or session cookies, which are automatically deleted once you close the app or the service. These types of cookies allow us to capture your session ID. As a result, different requests from the app or the service can be assigned to a common session, and it is possible to recognize your device during future website visits. These session cookies expire at the end of the session.</p>
<p>&nbsp;</p>
<p>Persistent Cookies</p>
<p>We also use so-called persistent cookies, which are stored in the app or the service for an extended period and can transmit information. The respective storage duration varies depending on the cookie.</p>
<p>&nbsp;</p>
<p>A list of third-party tools used in our apps and services for the aforementioned purposes can be found in the appendix to this privacy policy.</p>
<p>&nbsp;</p>
<p>11.&nbsp; &nbsp; &nbsp; &nbsp;Google Analytics 4</p>
<p>&nbsp;</p>
<p>We use the tracking tool &quot;Google Analytics 4&quot; provided by Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Ireland, Tel: +353 1 543 1000, Fax: +353 1 686 5660, Email: support-deutschland@google.com (&quot;Google&quot;) in our apps and services.</p>
<p>&nbsp;</p>
<p>Google Analytics 4 uses JavaScript and pixels to read information on your device, as well as cookies to store information on your device. This is used to analyze your usage behavior and improve our apps and services. The access data is aggregated by Google on our behalf to create pseudonymous user profiles and transmitted to a Google server in the United States. Google will use this information to systematically evaluate your use of our apps and services and compile reports on the activities on our apps and services.</p>
<p>&nbsp;</p>
<p>As part of the analysis, Google Analytics 4 also uses artificial intelligence such as machine learning to automatically analyze and optimize the data. For example, conversions are modeled when there is insufficient data available. You can find more information in the relevant Google documentation. The data evaluations are automated through artificial intelligence or based on individually defined criteria.</p>
<p>&nbsp;</p>
<p>As part of the usage analysis of Google Analytics 4, the collected data is enriched with information from the Google Search Console and linked to Google Ads data. This allows us to measure the success of our advertising campaigns, also known as conversions.</p>
<p>&nbsp;</p>
<p>The following data may be processed:</p>
<ul>
    <li>IP address;</li>
    <li>Referrer URL (previously visited page);</li>
    <li>Visited pages (date, time, URL, title, duration);</li>
    <li>Downloaded files;</li>
    <li>Clicked links to other websites;</li>
    <li>Achievement of specific goals (conversions);</li>
    <li>Technical information (operating system; browser type, version, and language; device type, brand, model, and resolution);</li>
    <li>Approximate location (country, region, and possibly city, based on anonymized IP address).</li>
</ul>
<p>&nbsp;</p>
<p>We use Google Analytics 4 with IP anonymization enabled. This means that IP addresses are truncated by the last octet (e.g., 192.168.79.***; so-called IP masking). It is no longer possible to associate the truncated IP address with the accessing computer or user&apos;s device.</p>
<p>&nbsp;</p>
<p>The generated information about your use of our apps and services is usually transmitted to a Google server in the United States and stored there. Due to EU Standard Contractual Clauses, Google is obligated to comply with a level of data protection that is essentially equivalent to European standards.</p>
<p>&nbsp;</p>
<p>The Google Analytics 4 service is used for analyzing the user behavior of our apps and services. The legal basis is your consent under Art. 6(1)(a) of the General Data Protection Regulation (DS-GVO). The stored data will be deleted by us as soon as it is no longer needed for analytical purposes. In our case, the maximum storage period is 24 months.</p>
<p>&nbsp;</p>
<p>For more information on the terms of use of Google Analytics 4:</p>
<p>www.google.com/analytics/terms/de.html</p>
<p>&nbsp;</p>
<p>For more information on the privacy of Google Analytics 4:</p>
<p>https://support.google.com/analytics/answer/6004245?hl=en</p>
<p>12.&nbsp; &nbsp; &nbsp; &nbsp;Youtube</p>
<p>&nbsp;</p>
<p>We integrate YouTube videos into our apps and services, which are stored at http://www.youtube.com and can be played directly from our apps. YouTube is a service provided by Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Ireland, Tel: +353 1 543 1000, Fax: +353 1 686 5660, Email: support-deutschland@google.com (&quot;Google&quot;).</p>
<p>&nbsp;</p>
<p>YouTube collects your IP address, the date and time as well as information about the website you visited and the video you viewed. This takes place regardless of whether YouTube provides a user account via which you are logged in or whether no user account exists. In addition, a connection to the Google advertising network is established.</p>
<p>&nbsp;</p>
<p>As long as a YouTube video embedded by us is displayed in our apps without the video being played, no data is transmitted to YouTube due to YouTube&apos;s &quot;Extended data protection mode&quot; function. Transmission only takes place when you actually start the video.</p>
<p>&nbsp;</p>
<p>In order to save your desired setting regarding the playback of videos and the transmission of data to YouTube, we set a cookie. These cookies do not contain any personal data, they only contain anonymised data for customisation in our app.</p>
<p>&nbsp;</p>
<p>If you are logged into YouTube at the same time, YouTube can assign the connection information to your YouTube account and use it for the purpose of personalised advertising.</p>
<p>&nbsp;</p>
<p>For more information, please see Google&apos;s privacy policy: http://www.google.de/intl/de/policies/privacy/</p>
<p>&nbsp;</p>
<p>We use YouTube to show you videos in our apps and services. The legal basis for the processing is your consent in accordance with Art. 6 (1) lit. a DS-GVO.</p>
<p>&nbsp;</p>
<p>13.&nbsp; &nbsp; &nbsp; &nbsp;What legal rights do you have?</p>
<p>&nbsp;</p>
<p>You have the following legal rights regarding data protection:</p>
<p>&nbsp;</p>
<p>Right to withdraw consent for future processing (Art. 7(3) of the GDPR)</p>
<p>Whenever the processing of your data is based on your explicit consent, you can withdraw this consent at any time with future effect. However, any data processing that has already occurred based on your consent remains lawful.</p>
<p>&nbsp;</p>
<p>Right to information about the processing of your data (Art. 15 of the GDPR)</p>
<p>You have the right to request confirmation from us as to whether we are processing personal data about you. If this is the case, you are entitled to be informed of the further circumstances of this processing, including its purpose, the categories of data processed, the recipients of the data, the storage duration of the data, and the source of the data.</p>
<p>&nbsp;</p>
<p>Right to rectification of your data (Art. 16 of the GDPR)</p>
<p>You have the right to have incorrect data corrected. In addition, you have the right to have incomplete data completed if this is necessary for the processing.</p>
<p>&nbsp;</p>
<p>Right to erasure of your data (Art. 17 of the GDPR)</p>
<p>You have the right to have your data erased if:</p>
<ul>
    <li>It is no longer necessary for the original purposes of processing,</li>
    <li>You have revoked your consent to the processing of the data,</li>
    <li>You have objected to the processing of your data,</li>
    <li>The data has been processed unlawfully, or</li>
    <li>There is a legal obligation to delete the data.</li>
    <li>&nbsp;</li>
</ul>
<p>If we have previously made such data public, you also have the right to request that we inform other data controllers who process your data about your request for erasure.</p>
<p>&nbsp;</p>
<p>In certain cases, the right to erasure is excluded, for example, if the data must be processed due to a legal obligation or is necessary for the establishment, exercise, or defense of legal claims.</p>
<p>&nbsp;</p>
<p>Right to restriction of processing of your data (Art. 18 of the GDPR)</p>
<p>You have the right to request the restriction of the processing of your data (= to block it) if:</p>
<ul>
    <li>You dispute its accuracy, and we need to verify this,</li>
    <li>The data has been unlawfully processed,</li>
    <li>You need the data for the establishment, exercise, or defense of legal claims, or</li>
    <li>You have objected to the processing of the data, and we are currently examining this objection.</li>
</ul>
<p>&nbsp;</p>
<p>Right to data portability (Art. 20 of the GDPR)</p>
<p>You have the right to receive the personal data you have provided to us in a structured, commonly used, and machine-readable format.</p>
<p>&nbsp;</p>
<p>You also have the right to transmit such data to another data controller if the processing was based on your consent or on a contract, and the processing was carried out using automated procedures.</p>
<p>&nbsp;</p>
<p>You also have the right to have such data transmitted directly to another data controller, if technically feasible.</p>
<p>&nbsp;</p>
<p>Right to object to the processing of your data (Art. 21 of the GDPR)</p>
<p>You have the right to object to the processing of your data for personal reasons when we process it based on our legitimate interests (under Art. 6(1)(f) of the GDPR). In this case, we will no longer process your data unless we can demonstrate compelling legitimate grounds for the processing that override your interests, rights, and freedoms.</p>
<p>&nbsp;</p>
<p>Additionally, you have the right to object at any time to the use of your data for direct marketing purposes.</p>
<p>&nbsp;</p>
<p>Right to not be subject to solely automated decision-making (Art. 22 of the GDPR)</p>
<p>You have the right not to be affected by a decision based solely on automated processing if this processing has legal or similarly significant effects. However, this does not apply if the automated decision-making is necessary for the conclusion or performance of a contract with us, is permitted by law, or is based on your explicit consent.</p>
<p>&nbsp;</p>
<p>If automated decision-making takes place as a result, you have the right to intervene in the automated processing by a person, to state your point of view, and to contest the decision made through automated means.</p>
<p>&nbsp;</p>
<p>Right to lodge a complaint</p>
<p>In addition, you have the right to lodge a complaint with the data protection supervisory authority if you believe that a processing activity violates legal regulations.</p>
<p>&nbsp;</p>
<p>14.&nbsp; &nbsp; &nbsp; &nbsp;Data protection in the Swiss market according to the GDPR</p>
<p>&nbsp;</p>
<p>We attach great importance to the protection of personal data and comply with the provisions of the General Data Protection Regulation (GDPR) of the European Union to ensure the protection of privacy and customer rights. These stricter data protection standards apply not only to our customers within the EU but also to customers in the Swiss market. This ensures compliance with Swiss data protection laws.</p>
<p>&nbsp;</p>
<p>15.&nbsp; &nbsp; &nbsp; &nbsp;Amendment to this privacy policy</p>
<p>&nbsp;</p>
<p>We may update this privacy policy over time to, for example, adapt it to changes in legal requirements or new features of the apps and services. In the event of significant changes, we will notify you separately, such as by email or in-app notification.</p>
<p>&nbsp;</p>
<p>As of: 26.10.2023</p>
<p><br>&nbsp;</p>
<p>&nbsp;</p>
<p>Attachment: Third-party tools / cookies used in the apps and services</p>
<p>&nbsp;</p>
<table>
    <tbody>
        <tr>
            <td style="width: 112.75pt;border: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Tool</p>
            </td>
            <td style="width: 114.75pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Purpose</p>
            </td>
            <td style="width: 112.75pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Storage duration</p>
            </td>
            <td style="width: 112.85pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Data types</p>
            </td>
        </tr>
        <tr>
            <td style="width: 112.75pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Google Analytics&nbsp;4</p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>&nbsp;</p>
            </td>
            <td style="width: 114.75pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Analysis</p>
            </td>
            <td style="width: 112.75pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Up to 24 months</p>
            </td>
            <td style="width: 112.85pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Analysis data (see above section 11)</p>
            </td>
        </tr>
        <tr>
            <td style="width: 112.75pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Youtube</p>
            </td>
            <td style="width: 114.75pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Video integration</p>
            </td>
            <td style="width: 112.75pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Up to 24 months</p>
            </td>
            <td style="width: 112.85pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Analysis data (see above section 12)</p>
            </td>
        </tr>
        <tr>
            <td style="width: 112.75pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Plenigo, Stripe, PayPal</p>
            </td>
            <td style="width: 114.75pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Required:</p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Account management and payment service providers</p>
            </td>
            <td style="width: 112.75pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Payment processing + legal deadlines, if applicable</p>
            </td>
            <td style="width: 112.85pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Name, address, email address, customer ID, booking and transaction data, payment information.</p>
            </td>
        </tr>
    </tbody>
</table>
<p>&nbsp;</p>
<p>You can access the privacy statements of the respective providers at:</p>
<p>&nbsp;</p>
<table>
    <tbody>
        <tr>
            <td style="width: 113.15pt;border: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Provider</p>
            </td>
            <td style="width: 290.6pt;border-top: 1pt solid windowtext;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-image: initial;border-left: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Privacy Policy</p>
            </td>
        </tr>
        <tr>
            <td style="width: 113.15pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Google</p>
            </td>
            <td style="width: 290.6pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'><a href="https://policies.google.com/privacy?hl=de">https://policies.google.com/privacy?hl=de</a>&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td style="width: 113.15pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Plenigo</p>
            </td>
            <td style="width: 290.6pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'><a href="https://www.plenigo.com/datenschutz/">https://www.plenigo.com/datenschutz/</a>&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td style="width: 113.15pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Stripe</p>
            </td>
            <td style="width: 290.6pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'><a href="https://stripe.com/de/privacy">https://stripe.com/de/privacy</a>&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td style="width: 113.15pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'>Paypal</p>
            </td>
            <td style="width: 290.6pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:  150%;'><a href="https://www.paypal.com/de/webapps/mpp/ua/privacy-full">https://www.paypal.com/de/webapps/mpp/ua/privacy-full</a>&nbsp;</p>
            </td>
        </tr>
    </tbody>
</table>
<p>&nbsp;</p>
""",
        },
    ],
    "url": "https://sportworld.tv/privacy",
}

legal_imprint = {
    "html": [
        {
            "locales": ["de-DE"],
            "value": """<p>PFLICHTANGABEN ZUM DIENSTEANBIETER GEM&Auml;SS &sect; 5 ABS. 1 TMG (TELEMEDIENGESETZ</p>
<p>B1 SmartTV GmbH</p>
<p>Ainmillerstr. 28</p>
<p>80801 M&uuml;nchen</p>
<p>&nbsp;</p>
<p>Handelsregister: Amtsgericht M&uuml;nchen HRB 235921</p>
<p>&nbsp;</p>
<p>Vertreten durch:</p>
<p>Gerd Weiner (Gesch&auml;ftsf&uuml;hrer)</p>
<p>Dr. Robert Niemann (Gesch&auml;ftsf&uuml;hrer)</p>
<p>&nbsp;</p>
<p>Kontakt</p>
<p>E-Mail: info@b1smarttv.com</p>
<p>&nbsp;</p>
<p>UMSATZSTEUER-ID</p>
<p>Umsatzsteuer-Identifikationsnummer gem&auml;&szlig; &sect; 27 a Umsatzsteuergesetz:</p>
<p>DE 313837648</p>
<p>&nbsp;</p>
<p>INHALTLICH VERANTWORTLICH F&Uuml;R JOURNALISTISCH-REDAKTIONELL GESTALTETE ANGEBOTE I.S.V. &sect;18 ABS. 2 MSTV (MEDIENSTAATSVERTRAG):</p>
<p>Stephan Zurawski</p>
<p>B1SmartTV GmbH</p>
<p>Ainmillerstr. 28</p>
<p>80801 M&uuml;nchen</p>
<p>DATENSCHUTZBEAUFTRAGTER</p>
<p>Dr. Georg Schr&ouml;der, LL.M.</p>
<p>&nbsp;</p>
<p>c/o legal data Schr&ouml;der Rechtsanwaltsgesellschaft mbH</p>
<p>Prannerstr. 1</p>
<p>80333 M&uuml;nchen</p>
<p>Tel.: +49 (0)89 954 597 520</p>
<p>Fax: +49 (0)89 954 597 522</p>
<p>E-Mail: datenschutz@legaldata.law</p>
<p>AUFSICHTSBEH&Ouml;RDE</p>
<p>Bayerische Landeszentrale f&uuml;r neue Medien (BLM)</p>
<p>Heinrich-L&uuml;bke-Str. 27</p>
<p>81737 M&uuml;nchen</p>
<p>Tel.: +49 (0)89 63 808 - 0</p>
<p>Fax: +49 (0)89 63 808 - 140</p>
<p>E-Mail: info@blm.de</p>
<p>EU-STREITSCHLICHTUNG</p>
<p>Die Europ&auml;ische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit: https://ec.europa.eu/consumers/odr/. Unsere E-Mail-Adresse finden Sie weiter oben im Impressum.</p>
<p>&nbsp;</p>
<p>VERBRAUCHERSTREITBEILEGUNG/UNIVERSALSCHLICHTUNGSSTELLE</p>
<p>Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle oder einer etwaigen anderen Verbraucherschlichtungsstelle im Sinne des Verbraucherstreitbeilegungsgesetzes teilzunehmen.</p>
<p>&nbsp;</p>
<p>FOTOAGENTUREN</p>
<p>Getty Images Deutschland GmbH, Auenstra&szlig;e 5, 80469 M&uuml;nchen</p>
<p>Imago Sportfotodienst GmbH, Berliner Str. 16, 13127 Berlin, www.imago-images.de</p>
<p>Shutterstock Netherlands BV Herengracht 495 1017 BT, Shutterstock.com</p>
<p>&nbsp;</p>
<p>Stand: 06/2023</p>
""",
        },
        {
            "locales": ["en-US"],
            "value": """<p>Mandatory information about the service provider according to &sect; 5 para. 1 TMG (Telemedia Act)<br>B1 SmartTV GmbH<br>Ainmillerstr. 28<br>80801 Munich<br>&nbsp;<br>Commercial Register: Munich District Court HRB 235921<br>&nbsp;<br>&nbsp;Represented by:<br>&nbsp;Gerd Weiner (Managing Director)</p>
<p>Dr. Robert Niemann (Managing Director)<br>&nbsp;<br>&nbsp;Contact<br> E-mail: <a href="mailto:info@b1smarttv.com">info@b1smarttv.com</a><br>&nbsp;<br>&nbsp;Sales tax ID<br>&nbsp;Sales tax identification number according to &sect; 27 a Sales Tax Act:<br>&nbsp;DE 313837648<br>&nbsp;<br>&nbsp;Responsible for the content of journalistic and editorial offers in the sense of &sect;18 para. 2 MStV (Media State Treaty):<br>&nbsp;Stephan Zurawski<br>&nbsp;B1 SmartTV GmbH<br>&nbsp;Ainmillerstr. 28<br>&nbsp;80801 Munich</p>
<p><br>&nbsp;Data Protection Officer<br>&nbsp;Dr. Georg Schr&ouml;der, LL.M.<br>&nbsp;c/o legal data Schr&ouml;der Rechtsanwaltsgesellschaft mbH<br>&nbsp;Prannerstr.&nbsp;1<br>&nbsp;80333 Munich<br>&nbsp;Phone: +49 (0)89 954 597 520<br>&nbsp;Fax: +49 (0)89 954 597 522<br>&nbsp;E-mail:&nbsp;<a href="mailto:datenschutz@legaldata.law">datenschutz@legaldata.law</a></p>
<p>Supervisory authority<br>&nbsp;Bavarian Regulatory Authority for Commercial Broadcasting (BLM)<br>&nbsp;Heinrich-L&uuml;bke-Str. 27<br>&nbsp;81737 Munich<br>&nbsp;Tel.: +49 (0)89 63 808 - 0<br>&nbsp;Fax: +49 (0)89 63 808 - 140<br>&nbsp;E-mail:&nbsp;<a href="mailto:info@blm.de">info@blm.de</a></p>
<p>EU dispute settlement<br>&nbsp;The European Commission provides a platform for online dispute settlement (OS):&nbsp;<a href="https://ec.europa.eu/consumers/odr/">https://ec.europa.eu/consumers/odr/</a>. You will find our e-mail address further up in the imprint.<br>&nbsp;<br>&nbsp;Consumer dispute resolution/universal arbitration board<br>&nbsp;We are not willing or obliged to participate in dispute resolution proceedings before a consumer arbitration board or any other consumer arbitration board within the meaning of the Consumer Dispute Resolution Act.<br>&nbsp;<br>&nbsp;Photo agencies<br>&nbsp;Getty Images Deutschland GmbH, Auenstra&szlig;e 5, 80469 Munich, Germany<br>&nbsp;Imago Sportfotodienst GmbH, Berliner Str. 16, 13127 Berlin,&nbsp;<a href="http://www.imago-images.de/">www.imago-images.de</a><br>&nbsp;Shutterstock Netherlands BV Herengracht 495 1017 BT,&nbsp;<a href="http://shutterstock.com/">Shutterstock.com</a></p>
<p>Status: 06/2023</p>
""",
        },
    ],
    "url": "https://sportworld.tv/imprint",
}

legal_terms_mp1 = {
    "html": [
        {
            "locales": ["de-DE"],
            "value": """<p>Nutzungsbedingungen</p>
<div>
    <ol>
        <li>Geltungsbereich</li>
    </ol>
</div>
<p>Diese Nutzungsbedingungen gelten f&uuml;r die Registrierung und Nutzung s&auml;mtlicher von der B1SmartTV GmbH mit Sitz in M&uuml;nchen, Ainmillerstra&szlig;e 28, 80801 M&uuml;nchen (Amtsgericht M&uuml;nchen, HRB 235921) (nachfolgend &quot;B1&quot; genannt) in der Sportworld App, &uuml;ber die Sportworld Webseite oder &uuml;ber sonstige Verbreitungswege (nachfolgend &quot;Sportworld&quot; genannt) zur Verf&uuml;gung gestellte kostenlosen, registrierungspflichtigen oder auf Grund eines Abonnements kostenpflichtig zur Verf&uuml;gung gestellte Inhalte (z.B. &uuml;ber entgeltpflichtige P&auml;sse, Programmpakete und Paketkombinationen) (nachfolgend &quot;Inhalte&quot; genannt), die Nutzung einer gegebenenfalls zur Verf&uuml;gung gestellte Plattform zum Erwerb von sog. Non-Fungible Token (NFT) sowie Funktionen und sonstige Services durch den Kunden (nachfolgend &quot;Nutzer&quot; genannt).</p>
<p>F&uuml;r bestimmte Funktionen und sonstige Services (nachfolgend &quot;Dienste&quot; genannt) gelten gegebenenfalls zus&auml;tzliche oder abweichende Bedingungen (nachfolgend &bdquo;Besondere Bedingungen&ldquo; genannt, wobei Besondere Bedingungen zusammen mit diesen Nutzungsbedingungen auch &bdquo;Nutzungsbedingungen&ldquo; genannt werden), denen der Nutzer zustimmen muss und auf die B1 den Nutzer rechtzeitig vor der Nutzung solcher Dienste hinweisen wird. Wenn und soweit Besondere Bedingungen diesen Nutzungsbedingungen widersprechen, gehen die Besonderen Bedingungen vor.&nbsp;</p>
<p>Soweit f&uuml;r die Nutzung bestimmter Dienste der Nutzer dar&uuml;ber hinaus Drittanbieter einschalten wird, wird B1 den Nutzer auf diese vor der Nutzung solcher Dienste hinweisen. Unabh&auml;ngig davon, ob Dienste und/oder Services Dritter in die Sportworld integriert sind oder nicht, werden diese Dienste/Services von Drittanbietern unter deren alleiniger Verantwortung unter den Nutzungsbedingungen und der Datenschutzrichtlinie des jeweiligen Drittanbieters bereitgestellt. Wenn der Nutzer diese Drittanbieter-Bedingungen nicht akzeptiert, kann der Nutzer solche Dienste nicht nutzen, wodurch auch die Nutzung der von B1 angebotenen Leistungen eingeschr&auml;nkt sein kann. F&uuml;r Drittanbieter &uuml;bernimmt B1 keine Haftung.</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>Allgemeine Bedingungen zur Nutzung der Sportworld</li>
    </ol>
</div>
<p>Einmalige Registrierung und Nutzerkonto</p>
<p>Der Zugang, der Empfang und die Nutzung der Inhalte und Dienste ist dem Nutzer &uuml;ber die Sportworld, die auf geeigneten internetf&auml;higen Endger&auml;ten, wie SmartTV, Smartphones, Tablets, TV-Sticks und gegebenenfalls anderen Entertainment Systemen (nachfolgend zusammen &quot;Verbreitungswege&quot; genannt) zur Verf&uuml;gung steht und m&ouml;glicherweise installiert werden muss, m&ouml;glich.</p>
<p>Um die kostenpflichtigen und/oder registrierungspflichtigen Inhalte und Dienste nutzen zu k&ouml;nnen, muss sich der Nutzer in der Sportworld erstmalig registrieren und einen Sportworld Account (&bdquo;Nutzerkonto&ldquo;) anlegen, &uuml;ber den auch Abonnements gebucht werden k&ouml;nnen. Mit Abschluss der Registrierung wird f&uuml;r den Kunden zun&auml;chst ein kostenloses Nutzerkonto eingerichtet und der Nutzer erh&auml;lt eine Best&auml;tigung der Registrierung per E-Mail. Der Nutzer kann in seinem Nutzerkonto jederzeit uneingeschr&auml;nkt verf&uuml;gen. Ohne Registrierung steht dem Nutzer nur ein eingeschr&auml;nktes Angebot in der Sportworld zur Verf&uuml;gung. Eine Zahlungspflicht des Nutzers besteht erst, wenn der Nutzer kostenpflichtige Inhalte oder Dienste &uuml;ber die Sportworld bestellt hat.</p>
<p>Der Nutzer ist verpflichtet, die f&uuml;r die Registrierung erforderlichen Daten, d.h. insbesondere Namen, E-Mail-Adresse und Zahlungsdaten, korrekt und vollst&auml;ndig anzugeben und im Fall von &Auml;nderungen unverz&uuml;glich zu aktualisieren. Nur vollj&auml;hrige Personen sind zur Registrierung und Er&ouml;ffnung eines Nutzerkontos berechtigt.&nbsp;</p>
<p>Vor Nutzung der kostenpflichtigen und/oder registrierungspflichtigen Inhalte und Dienste ist die Eingabe der Kundennummer oder E-Mail sowie des Passworts durch den Nutzer erforderlich (Login-Daten). Eine Weitergabe der Login-Daten ist nur an im selben Haushalt lebende Personen gestattet. Der Nutzer darf Kindern und Jugendlichen den Zugang zu den Inhalten nur erm&ouml;glichen, wenn der Inhalt nach dem jeweils anwendbaren Jugendschutzrecht f&uuml;r deren Alter freigegeben ist und nicht aus anderen zwingenden rechtlichen Gr&uuml;nden von der Nutzung ausgeschlossen sind.&nbsp;</p>
<p>Nutzungsvertrag&nbsp;</p>
<p>Zur Nutzung kostenpflichtiger Inhalte w&auml;hrend eines Bezugszeitraums bedarf es zus&auml;tzlicher individueller Bestellungen des Nutzers von Sportworld Angeboten, wie Monats- oder Jahresp&auml;sse, (&bdquo;Abonnement&ldquo;), die im Nutzerkonto get&auml;tigt und verwaltet werden k&ouml;nnen.&nbsp;</p>
<p>Mit der Bestellung kostenpflichtiger Inhalte kommt jeweils ein Nutzungsvertrag zwischen B1 und dem Nutzer zu Stande und gew&auml;hrt dem Nutzer Zugriff auf das ausgew&auml;hlte und gebuchte Abonnement f&uuml;r den jeweils vereinbarten Bezugszeitraum und die vereinbarten Kosten. Die Dauer der Leistungserbringung sowie die Kosten werden dem Nutzer jeweils vor der Bestellung in der Sportworld mitgeteilt. Nach erfolgter Bestellung erh&auml;lt der Nutzer eine Best&auml;tigung per E-Mail mit allen Informationen zum Abonnement. Der Nutzer kann nach Bestellung eine &Uuml;bersicht und Einzelheiten seiner Abonnements &uuml;ber sein Nutzerkonto abrufen.</p>
<p>Die Abonnements in der Sportworld sind freibleibend und stellen noch kein rechtlich verbindliches Angebot der B1 dar. Der Nutzer gibt durch Aktivierung des Bestellbuttons eine verbindliche Anfrage auf Bestellung eines Abonnements ab. Die Eingaben k&ouml;nnen vom Nutzer w&auml;hrend des Bestellvorgangs grunds&auml;tzlich jederzeit &uuml;berpr&uuml;ft und korrigiert werden. Die verbindliche Sprache f&uuml;r Bestellungen ist deutsch und f&uuml;r Angebote der Sportworld au&szlig;erhalb von Deutschland oder &Ouml;sterreich englisch, soweit die jeweilige Landessprache nicht angeboten wird. Die f&uuml;r den Vertragsschluss erforderliche Annahme der Bestellung liegt im Ermessen von B1 und kann insbesondere bei Vorliegen sachlicher Gr&uuml;nde (z.B. unzureichender Altersnachweis) von B1 abgelehnt werden. Das Abonnement kommt durch Freischaltung des Abonnements zustande und der Nutzer erh&auml;lt eine Bestellbest&auml;tigung per E-Mail. Eine gesonderte Speicherung des Vertragstextes durch B1 ist nicht vorgesehen. Der Inhalt des Abonnements ergibt sich jeweils aus den Details der per E-Mail &uuml;bermittelten Bestellbest&auml;tigung (einschlie&szlig;lich der zum Bestellzeitpunkt g&uuml;ltigen Angebotsbeschreibung und Preisangaben, welche Bestandteil des Nutzungsvertrags werden) und den Nutzungsbedingungen. Die entsprechenden Angaben k&ouml;nnen im Nutzerkonto eingesehen werden.&nbsp;</p>
<p>B1 beh&auml;lt sich vor, die Bereitstellung oder Nutzung von Angeboten in der Sportworld davon abh&auml;ngig zu machen, dass der Nutzer seine f&uuml;r die Bestellung genutzte E-Mail-Adresse &uuml;ber einen per E-Mail zugesandten Best&auml;tigungslink best&auml;tigt.</p>
<p>Die verschiedenen Abonnements k&ouml;nnen einzeln gebucht und einzeln gek&uuml;ndigt werden. Im Falle der Hinzubuchung eines oder mehrerer weiterer Programmpakete (Upgrade) gelten jeweils die Laufzeiten der gebuchten Abonnements, die m&ouml;glicherweise untereinander nicht synchronisiert sind.</p>
<p>Nach Zustandekommen des Abonnements stellt B1 dem Nutzer den kostenpflichtigen Inhalt zum Streaming Live oder OnDemand bereit. Eine dauerhafte Kopie wird auf dem Endger&auml;t des Nutzers nicht erstellt.</p>
<p>Programmangebot</p>
<p>Die Gestaltung und Verf&uuml;gbarkeit von Inhalten k&ouml;nnen mit der Zeit variieren und unterliegen gew&ouml;hnlich gewissen Beschr&auml;nkungen. Die Inhalte k&ouml;nnen in jedem Land abgerufen werden, in dem diese verf&uuml;gbar sind, wenngleich Inhalte (und die ggf. verf&uuml;gbare Sprache) von Land zu Land variieren. Die Inhalte d&uuml;rfen nur innerhalb des vereinbarten Gebietes, in denen B1 die jeweiligen Inhalte lizenziert hat und dem Nutzer konkret anbietet, genutzt werden. Soweit B1 hierzu technische Ma&szlig;nahmen einsetzt (z.B. Geolokalisierung anhand der IP-Adresse des genutzten Internetanschlusses), darf der Nutzer diese nicht umgehen oder st&ouml;ren. Der Nutzer darf im Rahmen der Verordnung des Europ&auml;ischen Parlaments und des Rates zur Gew&auml;hrleistung der grenz&uuml;berschreitenden Portabilit&auml;t von Online-Inhaltediensten im Binnenmarkt auf den Online-Inhaltedienst zugreifen und ihn nutzen, solange er sich vor&uuml;bergehend in einem anderen EU-Mitgliedstaat aufh&auml;lt.</p>
<p>B1 ist mit angemessener Ank&uuml;ndigung zu lediglich geringf&uuml;gigen &Auml;nderungen des Programmangebotes in Abonnements berechtigt, sofern diese in Relation zum gesamten vereinbarten Programmangebot bei verst&auml;ndiger W&uuml;rdigung der beiderseitigen Interessen ohne weiteren Nachteilsausgleich nach Treu und Glauben vom Nutzer noch hinzunehmen ist. Dies ist gegeben, wenn B1 dem Nutzer weiterhin im Wesentlichen gleichwertige (&bdquo;vergleichbare&ldquo;), den Gesamtcharakter des Abonnements wahrende Inhalte zur Verf&uuml;gung stellt und die Anpassungen auf Grund von Umst&auml;nden notwendig werden, die nach Vertragsschluss eingetreten sind. Solche eine &Auml;nderung rechtfertigenden Umst&auml;nde k&ouml;nnen zum Beispiel der Wegfall von befristeten oder der unverschuldete Wegfall von unbefristeten Lizenzrechten f&uuml;r vertragsgegenst&auml;ndliche Abonnements (Rechteverluste), oder auch von B1 oder deren Erf&uuml;llungsgehilfen nicht verschuldete technische Gr&uuml;nde (z.B. Wegfall von Kabeldurchleitungsrechten, ge&auml;nderte Anforderungen an die Verschl&uuml;sselung) sein.&nbsp;</p>
<p>Technischer Betrieb</p>
<p>Der Nutzer hat keinen Anspruch auf Bereitstellung der Inhalte in einem bestimmten Format. Die Inhalte stehen in der Sportworld in den jeweils verf&uuml;gbaren Formaten in Standardaufl&ouml;sung und der maximal ausspielbaren Bildqualit&auml;t zur Verf&uuml;gung. Nicht alle Inhalte sind in allen Formaten wie HD, Ultra-HD und HDR verf&uuml;gbar und nicht alle Abonnements erlauben den Empfang von Inhalten in allen Formaten.</p>
<p>Die &Uuml;bertragungsqualit&auml;t der Inhalte kann variieren und unterliegt verschiedenen Faktoren, wie etwa Standort, der verf&uuml;gbaren Bandbreite und/oder der Geschwindigkeit der Internetverbindung, auf die B1 keinen Einfluss hat. Es obliegt dem Nutzer, auf eigene Kosten die f&uuml;r die Nutzung der Sportworld erforderlichen Systemanforderungen zu erf&uuml;llen sowie f&uuml;r ausreichende und konstante Daten&uuml;bertragung zu sorgen.</p>
<p>B1 unternimmt angemessene technische Anstrengungen, um sicherzustellen, dass die Inhalte zur vereinbarten Zeit m&ouml;glichst st&ouml;rungsfrei zur Verf&uuml;gung stehen. B1 kann jedoch nicht garantieren, dass die Inhalte abrufbar sind. Insbesondere durch h&ouml;here Gewalt verursachte Ausf&auml;lle der Technik k&ouml;nnen zu einer Unterbrechung der Abrufbarkeit f&uuml;hren. Ferner ist B1 nicht verantwortlich f&uuml;r die Absage oder den Abbruch eines Ereignisses oder daf&uuml;r, dass ein Ereignis wie geplant oder beworben gezeigt werden kann, noch dass es m&ouml;glich ist, ein Ereignis auf einem bestimmten Ger&auml;t anzusehen.</p>
<p>Gelegentlich kann es vorkommen, dass B1 die Sportworld f&uuml;r Updates oder Wartungsarbeiten unterbrechen muss. B1 ist jedoch bem&uuml;ht, solche Unterbrechungen minimal zu halten.</p>
<p>B1 ist nicht daf&uuml;r verantwortlich, wenn bestimmte vom Nutzer genutzte TV-Ger&auml;te, mobile Endger&auml;te oder Applikationen und deren Konfigurationen nicht funktionieren bzw. Auswirkungen auf die Nutzung der Inhalte oder die Wiedergabequalit&auml;t haben. Die Nutzung von Proxyservern kann zu &Uuml;bertragungsproblemen f&uuml;hren. Die Verdeckung oder Verschleierung des Aufenthaltsorts &uuml;ber andere IP-Adressen oder sonstige technische Methoden ist untersagt. Der Nutzer ist gehalten, auftretende M&auml;ngel unter Protokollierung gegebenenfalls angezeigter Fehlermeldungen zu melden.&nbsp;</p>
<p>F&uuml;r den Fall, dass Anwendungen von Drittanbietern (einschlie&szlig;lich Webseiten, Widgets, Software oder andere Softwaredienstprogramme) mit dem Sportworld Service interagieren, kann die Nutzung der Services dieser Drittanbieter m&ouml;glicherweise den Nutzungsbedingungen von Drittanbietern unterliegen, zu deren Einhaltung der Nutzer verpflichtet bist.</p>
<p>Nutzungsbeschr&auml;nkungen</p>
<p>Der Nutzer ist nur befugt, die Inhalte &uuml;ber die von B1 autorisierten Verbreitungswege zu nutzen. Der Nutzer ist berechtigt, die Abonnements auf h&ouml;chstens zwei (2) TV-Ger&auml;ten und h&ouml;chstens vier (4) mobilen Endger&auml;ten (wie z.B. Tablet, in-Car-Entertainment System) von zum selben Haushalt geh&ouml;renden Personen gleichzeitig zu nutzen. B1 beh&auml;lt sich vor, weitere Ger&auml;te vorr&uuml;bergehend zuzulassen.</p>
<p>Die Inhalte sind rechtlich gesch&uuml;tzt, insbesondere durch Urheber- und Leistungsschutzrechte. Es ist dem Nutzer nicht gestattet, etwaige Zugangstechnologien, Kennzeichnungen und sonstige Schutzsysteme, wie z.B. einem digitalen Rechte-Management (DRM), die zum Schutz der Inhalte verwendet werden, oder eine Geolokalisierung zu deaktivieren, zu umgehen, zu ver&auml;ndern oder anderweitig zu unterlaufen.</p>
<p>Die Inhalte sind innerhalb der vertraglich vorgesehenen zeitlichen Grenzen ausschlie&szlig;lich f&uuml;r private Zwecke zu verwenden und d&uuml;rfen nicht f&uuml;r kommerzielle Zwecke verwendet werden. Insbesondere d&uuml;rfen die Inhalte nicht in irgendeiner Weise bearbeitet, ver&auml;ndert, kopiert, gespeichert oder Dritten bzw. der &Ouml;ffentlichkeit zug&auml;nglich gemacht werden (z.B. durch Upload in sog. File- bzw. Streaming-Sharing Systeme).&nbsp;</p>
<p>Der Nutzer hat lediglich ein beschr&auml;nktes, nicht ausschlie&szlig;liches, nicht &uuml;bertragbares und r&auml;umlich beschr&auml;nktes Recht, die Inhalte nur im Rahmen und f&uuml;r die Dauer eines bestehenden Abonnements abzurufen und zu nutzen. Mit Ausnahme des vorstehenden beschr&auml;nkten Nutzungsrechts werden dem Nutzer keinerlei Rechte, Eigentum oder Anspr&uuml;che an Inhalten und/oder zur Verf&uuml;gung gestellten Inhalte oder Materialien einger&auml;umt oder &uuml;bertragen. Mit Beendigung des Abonnements ist der Nutzer nicht mehr berechtigt, auf die Abonnements zuzugreifen.</p>
<p>B1 beh&auml;lt sich die Sperrung des Nutzerkontos vor, sollte der Nutzer die Nutzungsbedingungen missachten.</p>
<p>Preise und Zahlungsweise</p>
<p>Der Produktpreis ergibt sich aus der vor Abschluss des Bestellvorgangs aufgef&uuml;hrten Preisangabe. S&auml;mtliche Preisangaben verstehen sich einschlie&szlig;lich der jeweils geltenden gesetzlichen Mehrwertsteuer. Die festgelegten monatlichen Geb&uuml;hren und sonstigen Zahlungen werden zu dem im Nutzerkonto f&uuml;r das gebuchte Abonnement aufgef&uuml;hrten Zahltag f&auml;llig. F&uuml;r Abonnements werden die Zahlungen monatlich jeweils zu Beginn eines Bezugszeitraums in Rechnung gestellt und sind sofort f&auml;llig. Der erste Abrechnungszeitraum beginnt am Tag des Vertragsschlusses und endet mit Ablauf des letzten Tages des Bezugszeitraums. Die Geb&uuml;hren f&uuml;r Tagestickets und Eventtickets werden zum Bestellzeitpunkt des jeweiligen Angebots zur Zahlung f&auml;llig und abgebucht. Wenn ein kostenloser Testzeitraum vereinbart wird, beginnt der kostenpflichtige Abrechnungszeitraum mit dem vereinbarten Tag, wenn der Nutzer ein Abonnement bestellt hat. Andernfalls endet der kostenlose Testzeitraum mit dem letzten Tag des vereinbarten Testzeitraums.</p>
<p>Die Zahlungen im Rahmen der Gesch&auml;ftsbeziehung erfolgen, soweit nicht abweichend festgelegt, je nach Vereinbarung &uuml;ber Kreditkartenzahlung, PayPal oder einem sonstigen angebotenen Zahlungsmittel. Eine Barzahlung ist in keinem Fall m&ouml;glich.&nbsp;</p>
<p>F&uuml;r die Zahlung mit bestimmten Zahlungsarten, wie z.B. PayPal, ApplePay, Amazon Pay, muss der Nutzer bei dem jeweiligen Anbieter registriert sein oder sich registrieren. Nachdem Nutzer ihre Zugangsdaten f&uuml;r ihr Konto auf der Seite des konkreten Anbieters eingegeben haben, muss der Nutzer die Zahlungsanweisung mittels der hinterlegten Zahlungsmethode an B1 best&auml;tigen. Schlie&szlig;lich wird der Nutzer zur Sportworld zur&uuml;ckgeleitet, wo der Nutzer den Bestellvorgang abschlie&szlig;t. Die Zahlung wird unmittelbar nach Abgabe der Bestellung durchgef&uuml;hrt.</p>
<p>Die Abrechnungen f&uuml;r die gebuchten Abonnements werden dem Nutzer im Kundenkonto oder per E-Mail zur Verf&uuml;gung gestellt.</p>
<p>Preisanpassungen</p>
<p>B1 kann die mit dem Nutzer vereinbarten Geb&uuml;hren nach Ma&szlig;gabe der folgenden Regelungen nach billigem Ermessen anpassen, wenn sich die dem Abonnement zu Grunde liegenden Beschaffungs- oder Bereitstellungskosten, wie z.B. Entgelte f&uuml;r Programmlizenzen, Entgelte f&uuml;r Technikleistungen, Kundenservice- und sonstige Umsatzkosten, allgemeine Verwaltungskosten (&bdquo;Gesamtkosten&ldquo;) nach Vertragsschluss auf Grund von Umst&auml;nden ver&auml;ndern, die bei Vertragsschluss nicht vorhersehbar waren und die nicht im Belieben von B1 stehen.</p>
<p>Eine Geb&uuml;hrenerh&ouml;hung kann B1 h&ouml;chstens einmal innerhalb eines Kalenderjahres vornehmen. Der Nutzer wird mindestens acht Wochen vor dem Inkrafttreten &uuml;ber eine anstehende Preiserh&ouml;hung informiert. B1 wird den Nutzer im Rahmen der Mitteilung &uuml;ber die Preiserh&ouml;hung auf ein etwaiges K&uuml;ndigungsrecht und die K&uuml;ndigungsfrist sowie auf die Folgen einer nicht fristgerecht eingegangenen K&uuml;ndigung besonders hinweisen.</p>
<p>Das K&uuml;ndigungsrecht gilt nur f&uuml;r das von der Preiserh&ouml;hung betroffene Abonnement. Ist das von der Preiserh&ouml;hung betroffene Abonnement Voraussetzung f&uuml;r ein anderes Abonnement, gilt eine K&uuml;ndigung jedoch auch f&uuml;r dieses. K&uuml;ndigt der Nutzer nicht oder nicht fristgem&auml;&szlig;, wird das Abonnement zu dem in der Mitteilung genannten Zeitpunkt mit den neuen Geb&uuml;hren fortgesetzt.</p>
<p>Unabh&auml;ngig von den vorstehenden Regelungen ist B1 f&uuml;r den Fall einer Erh&ouml;hung der gesetzlichen Geb&uuml;hren, Beitr&auml;ge, Steuern und Abgaben, wie z.B. Mehrwertsteuer, berechtigt, f&uuml;r den Fall einer Senkung verpflichtet, die Geb&uuml;hren entsprechend anzupassen.&nbsp;</p>
<p>Laufzeit und Beendigung von Abonnements</p>
<p>Die Abonnements haben die in der jeweiligen Leistungsbeschreibung bestimmte Laufzeit (&bdquo;Bezugszeitraum&ldquo;). Der Nutzer ist jederzeit berechtigt, ein Abonnement zum Ende der vereinbarten Laufzeit zu k&uuml;ndigen. Der Nutzer kann in seinem Nutzerkonto die Laufzeit und den n&auml;chstm&ouml;glichen K&uuml;ndigungszeitpunkt einsehen. F&uuml;r eine K&uuml;ndigung kann der Nutzer den Anweisungen im Nutzerkonto folgen. Der Angabe von Gr&uuml;nden bedarf es dabei nicht.&nbsp;</p>
<p>Der Nutzungsvertrag &uuml;ber die zeitlich befristete &Uuml;berlassung von Inhalten (VoD-Streaming) oder &uuml;ber nur einmalig abrufbare Live-Streams endet mit Ablauf der zeitlich befristeten &Uuml;berlassung oder des Live-Streams automatisch, ohne dass es einer K&uuml;ndigung bedarf.</p>
<p>Ist der Nutzer mit der Zahlung der Geb&uuml;hren nicht nur geringf&uuml;gig im Zahlungsverzug, so kann B1 bei Fortdauer der Zahlungsverpflichtung den Zugang zu den betroffenen Inhalten f&uuml;r die Dauer des Zahlungsverzuges entziehen und/oder die Inanspruchnahme weiterer Leistungen verweigern. Weitere Bestellungen von Abonnements sind bis zum Ende des Zahlungsverzuges nicht m&ouml;glich.&nbsp;</p>
<p>Ferner beh&auml;lt sich B1 das Recht vor, offensichtlich &uuml;ber einen Zeitraum von mehr als 12 Monaten nicht mehr genutzte Nutzerkonten zu l&ouml;schen. Nach Aufl&ouml;sung des Nutzerkontos ist B1 berechtigt, einen vom Nutzer verwendeten Alias (Nutzer-/Benutzername) an andere Nutzer zu vergeben.&nbsp;</p>
<p>Der Nutzer ist auch nach Aufl&ouml;sung des Kundenkontos und Beendigung von Abonnements berechtigt, kostenlose Inhalte zu nutzen.</p>
<p>Ist B1 aufgrund von lizenzrechtlichen bzw. technischen Gr&uuml;nden nicht mehr in der Lage, dem Nutzer einzelne Inhalte, Abonnements/Tickets oder Programmkombinationen zur Verf&uuml;gung zu stellen, ist B1 mit einer angemessenen K&uuml;ndigungsfrist berechtigt, das betroffene Abonnement zu k&uuml;ndigen.&nbsp;</p>
<p>Das Recht zur K&uuml;ndigung aus wichtigem Grund bleibt f&uuml;r beide Parteien unber&uuml;hrt.</p>
<p>Widerrufsrecht</p>
<p>Verbrauchern steht ein Widerrufsrecht f&uuml;r Abonnements nach Ma&szlig;gabe der Widerrufsbelehrung zu. Die aktuelle Widerrufsbelehrung nebst Widerrufsformular kann sich der Nutzer in der Sportworld anschauen und herunterladen.</p>
<p>Der Widerruf eines Abonnements kann m&uuml;ndlich, telefonisch oder in Textform erfolgen.</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>ALLGEMEINE GESCHÄFTSBEDINGUNGEN FÜR DEN KAUF VON NFT</li>
    </ol>
</div>
<p>NFT-Plattform, Verf&uuml;gbarkeit und Definitionen</p>
<p>Um NFTs &uuml;ber die Sportworld erwerben zu k&ouml;nnen, muss sich der Nutzer in der Sportworld registrieren und einen Nutzerkonto anlegen, &uuml;ber den auch Abonnements gebucht werden k&ouml;nnen. Mit Abschluss der Registrierung wird f&uuml;r den Kunden zun&auml;chst ein kostenloses Nutzerkonto eingerichtet und der Nutzer erh&auml;lt eine Best&auml;tigung der Registrierung per E-Mail. Der Nutzer kann in seinem Nutzerkonto jederzeit uneingeschr&auml;nkt verf&uuml;gen. Eine Zahlungspflicht des Nutzers besteht erst, wenn der Nutzer kostenpflichtige Inhalte oder Dienste &uuml;ber die Sportworld bestellt hat. F&uuml;r die Er&ouml;ffnung und Nutzung eines Sportworld Accounts gelten diese Nutzungsbedingungen. B1 beh&auml;lt sich die vorr&uuml;bergehende oder endg&uuml;ltige Sperrung des Nutzerkontos vor, bei verd&auml;chtigen Aktivit&auml;ten und wenn der Nutzer im Verdacht steht, gegen die Nutzungsbedingungen oder Besondere Bedingungen versto&szlig;en zu haben oder tats&auml;chlich verletzt hat.</p>
<p>Vor Nutzung der NFT-Plattform ist die Eingabe der Kundennummer oder E-Mail sowie des Passworts durch den Nutzer erforderlich (Login-Daten).</p>
<p>Die NFT-Plattform ist nicht in allen L&auml;ndern, in denen die Sportworld zur Verf&uuml;gung steht, verf&uuml;gbar, sondern nur in ausgew&auml;hlten L&auml;ndern. Eine Verf&uuml;gbarkeit der NFT-Plattform ist im Nutzerkonto angezeigt.</p>
<p>Es ist Ihnen untersagt, auf die Sportworld (oder einen unserer anderen Dienste) an, von oder &uuml;ber einen Ort zuzugreifen oder zu nutzen, an dem die Nutzung nicht verf&uuml;gbar ist oder gegen geltendes Recht verst&ouml;&szlig;t. Durch die Nutzung der Sportworld erkl&auml;rt der Nutzer und garantiert, weder B&uuml;rger oder Einwohner einer solchen Gerichtsbarkeit zu sein, noch wird der Nutzer die Sportworld verwenden, w&auml;hrend er sich in einer solchen Gerichtsbarkeit befindet oder wohnt.</p>
<p>NFT wird definiert als digitales Kunstwerk eines auf einem Blockchain-Netzwerk registrierten kryptografischen Tokens, der nicht austauschbar und ein nicht replizierbares Unikat ist, der von B1 in der Sportworld verkauft wird, gegenw&auml;rtig basierend auf der Polygon-Blockchain (https://polygon.technology/). NFT sind keine Wertpapiere im Sinne des Wertpapierhandelsgesetzes (WpHG) oder Finanzinstrumente im Sinne des Kreditwesengesetzes (KWG) oder andere anwendbare Gesetze und sind rechtlich nicht als solche zu behandeln. Die NFT werden nicht zu Anlagezwecken erworben oder verwendet. Content wird definiert als alle Inhalte, Dateien und Materialien, die durch das gekaufte NFT repr&auml;sentiert werden oder in ihm enthalten sind und die im Rahmen des Erwerbs des NFT lizenziert werden, einschlie&szlig;lich, aber nicht beschr&auml;nkt auf Grafiken, Videos, Texte, Marken, Logos, Bilder und Fotos.&nbsp;</p>
<p>Kauf von NFT</p>
<p>Der Nutzer kann, vorbehaltlich des Abschlusses eines individuellen Kaufvertrags mit&nbsp;B1, NFTs gegen eine festgelegte Vergütung nach dem unten beschriebenen Verfahren erwerben.&nbsp;Die Er&ouml;ffnung eines Nutzerkontos alleine, d.h. ohne den Kauf eines NFT, f&uuml;hrt nicht zu einer Kauf- und/oder Zahlungsverpflichtung des Nutzers. Die Berechtigung zum Kauf von NFTs, zum Beispiel aus bestimmten NFT-Collections, kann von bestimmten Kriterien abh&auml;ngig gemacht werden.</p>
<div>
    <ol>
        <li>Digital Wallet</li>
    </ol>
</div>
<p>&nbsp;</p>
<p>Voraussetzung f&uuml;r den Erwerb von NFT ist, dass der Nutzer Inhaber einer Polygon-Blockchain kompatiblen Digital Wallet zum Empfangen, Speichern, &Uuml;bertragen, Tauschen oder Ausgeben von NFTs ist. Die Adresse dieser Digital Wallet muss mitgeteilt und mit dem Nutzerkonto verkn&uuml;pft werden. Dazu nutzt B1 den &bdquo;Wallet-connect&ldquo; &ndash; Service unter&nbsp;<a href="https://walletconnect.com/">https://walletconnect.com/</a>&nbsp;mit folgenden Nutzungsbedingungen (<a href="https://walletconnect.com/terms">https://walletconnect.com/terms</a>) und Datenschutzbestimmungen (<a href="https://walletconnect.com/privacy">https://walletconnect.com/privacy</a>).</p>
<p>&nbsp;</p>
<p>Derzeit bietet dieser Dienst die M&ouml;glichkeit, eine Digital Wallet von Metamask, Coinbase oder eine andere mit Wallet Connect kompatiblen Digital Wallet zu verkn&uuml;pfen. Werden NFT auf eine nicht kompatible Digital Wallet &uuml;bertragen, kann es zur dauerhaften Unbrauchbarkeit des NFT f&uuml;hren. B1 bietet selbst keine Digital Wallet an und ist hierzu auch nicht verpflichtet.&nbsp;</p>
<p>&nbsp;</p>
<p>F&uuml;r die Er&ouml;ffnung oder Nutzung einer Digital Wallet k&ouml;nnen weitere Kosten anfallen, die von dem Nutzer selbst zu tragen sind.</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>Auswahl von NFT</li>
    </ol>
</div>
<p>&nbsp;</p>
<p>Der Nutzer kann aus bestehenden und gegebenenfalls auf die genannte Anzahl limitierte NFT sein NFT ausw&auml;hlen oder &uuml;ber &bdquo;My Moment&ldquo; seinen pers&ouml;nlichen Moment in einem einzigartigen, digitalen Sammlerst&uuml;ck festhalten und hierzu in Echtzeit eine begrenzte Anzahl Highlight Szenen aus einem Spiel, z.B. der European League of Football, mit einer von B1 vorgegebenen L&auml;nge von wenigen Sekunden definieren, um das endg&uuml;ltige Erscheinungsbild des dem NFT zugrunde liegenden Contents anzupassen/zu beeinflussen, z.B. als einen 3D-animierten W&uuml;rfel als NFT gestalten. Es liegt im alleinigen Ermessen von B1, solche Anpassungsoptionen anzubieten.</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>Erwerb und Hinterlegung von Credits</li>
    </ol>
</div>
<p>&nbsp;</p>
<p>Nach der Auswahl eines NFT erh&auml;lt der Nutzer einen &Uuml;berblick &uuml;ber das ausgew&auml;hlte NFT und den Gesamtbetrag der Verg&uuml;tung. Ein NFT kann nur durch die Einl&ouml;sung von zuvor in der Sportworld erworbenen Credits erworben werden. Die Anzahl der erforderlichen Credits sowie deren Wert in Euro zum Erwerb des NFTs wird in dem Bestellvorgang angezeigt. Verf&uuml;gt der Nutzer nicht &uuml;ber die ausreichende Anzahl an Credits, muss er diese zun&auml;chst in der Sportworld erwerben.</p>
<p>&nbsp;</p>
<p>Der Nutzer kann aus den zur Verf&uuml;gung stehenden Credits die zu erwerbende Anzahl Credits ausw&auml;hlen. Der Nutzer nimmt das Angebot zum Erwerb des ausgew&auml;hlten Credits an, indem er den Button &bdquo;Kaufen&ldquo; oder eine &auml;hnliche Formulierung anklickt und anschlie&szlig;end best&auml;tigt. Mit der Best&auml;tigung wird die entsprechende genannte Anzahl Credits erworben und mit Abschluss der Bezahlung dem Nutzerkonto gutgeschrieben.</p>
<p>&nbsp;</p>
<p>Sofern dem Nutzer im Rahmen einer Marketingaktion von einem Partner vom B1 ein Credit gew&auml;hrt wurde, kann dieser durch Eingabe eines erhaltenen Codes eingel&ouml;st und der Credit in dem Nutzerkonto hinterlegt werden.&nbsp;</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>Erwerb und &Uuml;bertragung von NFTs&nbsp;</li>
    </ol>
</div>
<p>&nbsp;</p>
<p>Der Nutzer nimmt das Angebot zum Erwerb des ausgew&auml;hlten NFT an, indem er den Button &bdquo;Kaufen&ldquo; oder eine &auml;hnliche Formulierung anklickt und anschlie&szlig;end best&auml;tigt. Mit der Best&auml;tigung wird die entsprechende genannte Anzahl Credits vom Konto des Nutzers abgezogen und das limitierte NFT in die hinterlegte Digitale Wallet &uuml;bertragen. Sofern &uuml;ber &bdquo;My Moment&ldquo; ein konfiguriertes NFT, z.B. 3D-animierter W&uuml;rfel als NFT, ausgew&auml;hlt und gestaltet wurde, beginnt mit der Best&auml;tigung das Minting, d.h. das NFT wird in der Blockchain erstellt und ver&ouml;ffentlicht, und anschlie&szlig;end in die hinterlegte Digitale Wallet des Nutzers &uuml;bertragen. Das Minting erfolgt &uuml;ber eine eigene Anwendung von B1 oder &uuml;ber g&auml;ngige Plattformen f&uuml;r das Minting von NFT.</p>
<p>&nbsp;</p>
<p>Die Übertragung des NFT gilt als erfolgt, wenn der NFT in der Digital&nbsp;Wallet des&nbsp;Nutzers&nbsp;erscheint, womit&nbsp;der Vorgang in der Blockchain vollständig dokumentiert wurde.</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>&Auml;nderungen im Bestellvorgang</li>
    </ol>
</div>
<p>&nbsp;</p>
<p>Mit der Best&auml;tigung sendet &nbsp;der Nutzer die verbindliche Bestellung an B1. Ab diesem Zeitpunkt ist eine &Auml;nderung der Bestellung oder Daten leider nicht mehr m&ouml;glich.&nbsp;Der Nutzer kann&nbsp;vor Anklicken der Best&auml;tigung den Bestellvorgang jederzeit beenden oder&nbsp;zu den vorherigen Seiten zurückkehren, um eventuelle Fehler zu korrigieren oder den Kauf zu ändern.</p>
<p>&nbsp;</p>
<p>F&uuml;r Erwerb und &Uuml;bertragung der NFT ist ein Internetzugang erforderlich. Der Nutzer ist allein verantwortlich f&uuml;r jegliche Hardware, Systeme und/oder Softwareprogramme, die f&uuml;r den Erwerb oder &Uuml;bertragung der NFT erforderlich sind.</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>Best&auml;tigung&nbsp;</li>
    </ol>
</div>
<p>&nbsp;</p>
<p>Nach Abschluss des Kaufes erh&auml;lt der Nutzer von B1 eine Bestell- und Auftragsbest&auml;tigung mit allen Bestelldaten und dem gesamten Vertragstext zu per E-Mail.&nbsp;</p>
<p>F&uuml;r den Vertragsschluss steht ausschlie&szlig;lich die deutsche und englische Sprache in der Sportworld zur Verf&uuml;gung.&nbsp;</p>
<p>Urheberrechte und Inhaber des NFT</p>
<p>Inhaber&nbsp;des NFT&nbsp;ist derjenige, der&nbsp;ein&nbsp;NFT gemä&szlig; diesen&nbsp;Bedingungen&nbsp;erwirbt. Diese Inhaberschaft wird durch ein bestimmtes Protokoll (Smart Contract) sichergestellt und überprüft.&nbsp;B1&nbsp;gibt keine Garantien oder Versprechen in Bezug auf Smart Contracts ab, insbesondere hat B1&nbsp;keine Kontrolle über die Inhaberschaft des Nutzers an dem NFT und kann diese nicht ändern.</p>
<p>Alle geistigen Eigentumsrechte, insbesondere Urheber- und Markenrechte, an der NFT-Plattform sowie s&auml;mtlichen Content, die &uuml;ber die NFT-Plattform zur Verf&uuml;gung gestellt werden, stehen B1 zu oder sind B1 von einem Drittlizenzgeber einger&auml;umt worden. Dem Nutzer werden keine Rechte am geistigen Eigentum einger&auml;umt.</p>
<p>Mit der erfolgreichen Übertragung des NFT an den&nbsp;Nutzer&nbsp;gewährt&nbsp;B1&nbsp;dem&nbsp;Nutzer&nbsp;eine weltweite, nicht exklusive,&nbsp;voll bezahlte&nbsp;Lizenz zur Nutzung, Vervielfältigung und Darstellung des NFT ausschlie&szlig;lich für den persönlichen, nicht kommerziellen Gebrauch des&nbsp;Nutzers.&nbsp;Der Nutzer kann die Lizenz nur dann auf einen Dritten &uuml;bertragen, wenn er den NFT &uuml;bertr&auml;gt.</p>
<p>Der&nbsp;Nutzer&nbsp;kann ohne weitere Mitwirkung von B1 &uuml;ber&nbsp;NFTs&nbsp;deren Inhaber er ist, frei verf&uuml;gen. Eine &Uuml;bertragung oder Verkauf der NFTs&nbsp;auf der NFT-Plattform&nbsp;von B1 ist nicht m&ouml;glich.&nbsp;Nutzer&nbsp;haben&nbsp;nur&nbsp;die Möglichkeit,&nbsp;die NFTs auf einem Drittanbieter-Marktplatz zum Verkauf anzubieten, vorbehaltlich der&nbsp;Bestimmungen, die für jedes NFT auf&nbsp;einer&nbsp;NFT-Plattform festgelegt werden können.&nbsp;Es obliegt ausschlie&szlig;lich dem Nutzer zu pr&uuml;fen, welche Rechte mit einem NFT verbunden sind, welche Bedingungen gelten, insbesondere welche Kosten anfallen.</p>
<p>Sicherheit und Technischer Betrieb</p>
<p>B1 unternimmt angemessene technische Anstrengungen, um die Sicherheit der NFT-Plattform zu gew&auml;hrleisten und m&ouml;glichst st&ouml;rungsfrei zur Verf&uuml;gung zu stellen. Insbesondere durch h&ouml;here Gewalt verursachte Ausf&auml;lle der Technik k&ouml;nnen zu einer Unterbrechung der Abrufbarkeit f&uuml;hren. B1&nbsp;kann nicht garantieren, dass die NFT-Plattform und/oder die NFTs frei von Viren und/oder anderen Computercodes sind, die kontaminierende oder zerstörerische Merkmale enthalten können.&nbsp;Es liegt in der Verantwortung des Nutzers, geeignete Computersicherheitsma&szlig;nahmen (einschlie&szlig;lich Antiviren- und anderer Sicherheitskontrollen) zu ergreifen, um seine besonderen Anforderungen an die Informationssicherheit und Zuverlässigkeit zu erfüllen.</p>
<p>Gelegentlich kann es vorkommen, dass B1 die Sportworld f&uuml;r Updates oder Wartungsarbeiten unterbrechen muss. B1 ist jedoch bem&uuml;ht, solche Unterbrechungen minimal zu halten.</p>
<p>F&uuml;r den Fall, dass Anwendungen von Drittanbietern (einschlie&szlig;lich Webseiten, Widgets, Software oder andere Softwaredienstprogramme) mit dem Sportworld Service interagieren, kann die Nutzung der Services dieser Drittanbieter m&ouml;glicherweise den Nutzungsbedingungen von Drittanbietern unterliegen, zu deren Einhaltung der Nutzer verpflichtet bist.</p>
<p>Verg&uuml;tung und Zahlungsweise</p>
<p>Die Preise f&uuml;r Credits oder NFTs ergeben sich aus der vor Abschluss des Bestellvorgangs aufgef&uuml;hrten Preisangabe. S&auml;mtliche Preisangaben verstehen sich einschlie&szlig;lich der jeweils geltenden gesetzlichen Mehrwertsteuer, beinhalten jedoch nicht die vom Nutzer f&uuml;r die jeweilige Transaktion zu zahlenden sog. Gas Fees, also variable Kosten von Drittanbietern, wie Transaktionskosten, z.B. f&uuml;r die Digital Wallet und Internetkosten, auf die B1 keinen Einfluss hat. &nbsp;Solche Geb&uuml;hren und Kosten werden dem&nbsp;Nutzer&nbsp;nicht von&nbsp;B1, sondern von Dritten in Rechnung gestellt&nbsp;und k&ouml;nnen daher im Bestellvorgang nicht angezeigt werden.&nbsp;Es obliegt dem Nutzer sich &uuml;ber diese Kosten vor Erwerb von NFTs zu informieren.</p>
<p>F&uuml;r den Erwerb eines NFTs sind Credits einzusetzen, die ausschlie&szlig;lich in der Sportworld k&auml;uflich erworben oder dem Nutzer im Rahmen einer Marketingaktion zur Verf&uuml;gung gestellt werden. Die Bezahlung der Credits erfolgt, soweit nicht abweichend festgelegt, je nach Vereinbarung &uuml;ber Kreditkartenzahlung, PayPal oder einem sonstigen angebotenen Zahlungsmittel. Eine Barzahlung ist in keinem Fall m&ouml;glich.&nbsp;</p>
<p>F&uuml;r die Zahlung mit bestimmten Zahlungsarten, wie z.B. PayPal, ApplePay, Amazon Pay, muss der Nutzer bei dem jeweiligen Anbieter registriert sein oder sich registrieren. Nachdem Nutzer ihre Zugangsdaten f&uuml;r ihr Konto auf der Seite des konkreten Anbieters eingegeben haben, muss der Nutzer die Zahlungsanweisung mittels der hinterlegten Zahlungsmethode an B1 best&auml;tigen. Schlie&szlig;lich wird der Nutzer zur Sportworld zur&uuml;ckgeleitet, wo der Nutzer den Bestellvorgang abschlie&szlig;t. Die Zahlung wird unmittelbar nach Abgabe der Bestellung durchgef&uuml;hrt.</p>
<p>Die Abrechnungen werden dem Nutzer im Kundenkonto oder per E-Mail zur Verf&uuml;gung gestellt.</p>
<p>Informationen über das vorzeitige Erlöschen des Widerrufsrechtes</p>
<p>Verbrauchern steht grunds&auml;tzlich ein Widerrufsrecht nach Ma&szlig;gabe der Widerrufsbelehrung zu. Die aktuelle Widerrufsbelehrung nebst Widerrufsformular kann sich der Nutzer in seinem Nutzerkonto herunterladen. Ein Widerruf kann m&uuml;ndlich, telefonisch oder in Textform erfolgen.</p>
<p>Das Widerrufsrecht erlischt bei einem Vertrag zur Erbringung von Dienstleistungen, wenn die Dienstleistung vollständig erbracht&nbsp;wurde&nbsp;und wenn der Vertrag&nbsp;den Nutzer&nbsp;zur Zahlung verpflichtet, wenn mit der Ausführung der Dienstleistung erst begonnen&nbsp;wurde, nachdem&nbsp;der Nutzer seine&nbsp;ausdrückliche Zustimmung hierzu erteilt und gleichzeitig&nbsp;seine&nbsp;Kenntnis davon bestätigt&nbsp;hat, dass&nbsp;er sein&nbsp;Widerrufsrecht bei vollständiger Vertragserfüllung verliert. Das Widerrufsrecht erlischt auch bei einem Vertrag über die Lieferung von digitalen&nbsp;Inhalten, die sich nicht auf einem k&ouml;rperlichen Datentr&auml;ger befinden, wenn mit der Ausf&uuml;hrung des Vertrages begonnen wurde und, wenn der Vertrag den Nutzer zur Zahlung verpflichtet, nachdem der Nutzer ausdr&uuml;cklich zugestimmt hat, dass mit der Ausf&uuml;hrung des Vertrages vor Ablauf der Widerrufsfrist beginnen werden soll und gleichzeitig der Nutzer seine Kenntnis davon best&auml;tigt hat, dass der Nutzer durch die Erteilung seiner Zustimmung sein Widerrufsrecht mit Beginn der Ausf&uuml;hrung des Vertrages verliert, und dem Nutzer eine Abschrift oder in der Best&auml;tigung des geschlossenen Vertrages &uuml;bermittelt wurde.</p>
<p>Mit Anklicken des Buttons &bdquo;Kaufen&ldquo; oder einer &auml;hnlichen Formulierung und anschlie&szlig;ender Best&auml;tigung stimmt der Nutzer der Ausf&uuml;hrung des Vertrages vor Ablauf der Widerrufsfrist zu und best&auml;tigt, dass der Nutzer durch seine Zustimmung mit Beginn der Ausf&uuml;hrung des Vertrags sein Widerrufsrecht verliert und keine R&uuml;ckerstattung erfolgt.</p>
<p>Gew&auml;hrleistung und Haftung</p>
<p>Ist ein auf der NFT-Plattform erworbenes NFT mangelhaft, gelten die gesetzlichen Bestimmungen &uuml;ber die Rechte des Nutzers. Ein von B1 erworbenes Produkt ist frei von Sachm&auml;ngeln, wenn es bei Gefahr&uuml;bergang die vereinbarte Beschaffenheit hat. Als Beschaffenheit sind die Einhaltung der Angaben in der Produktbeschreibung vereinbart. Eignungs-, Verwendungs- oder Anwendungsrisiken obliegen dem Nutzer und stellen keinen Mangel dar. B1 &uuml;bernimmt insbesondere keine Garantie, dass ein NFT seinen urspr&uuml;nglichen Wert beh&auml;lt, da der Wert von NFT&nbsp;von Natur aus subjektiv ist&nbsp;oder&nbsp;objektive&nbsp;Faktoren den Wert eines bestimmten&nbsp;NFT&nbsp;wesentlich beeinflussen k&ouml;nnen. Zus&auml;tzlich ist zu ber&uuml;cksichtigen, dass das Regulierungssystem f&uuml;r Blockchain-Technologien und darauf basierte Dienstleistungen und Produkte, wie NFT, nicht vorhersehbar ist, und neue gesetzliche oder regulatorische Vorschriften oder Richtlinien k&ouml;nnen die Entwicklung des Blockchain und NFT-Marktes und damit den potenziellen Nutzen oder Wert von NFT erheblich beeintr&auml;chtigen.</p>
<p>Zuk&uuml;nftige Entwicklungen und &Auml;nderungen dieses Regulierungssystems k&ouml;nnten&nbsp;sich auf&nbsp;die&nbsp;Nutzung der NFT-Plattform&nbsp;und Entwicklung des NFT-Marktes allgemein&nbsp;auswirken,&nbsp;und damit den potenziellen Nutzen oder Wert von NFT erheblich beeintr&auml;chtigen.&nbsp;B1&nbsp;haftet nicht für etwaige Folgen, die sich aus gesetzlichen und regulatorischen Entwicklungen für die Nutzung&nbsp;der Blockchain oder NFTs&nbsp;ergeben.&nbsp;</p>
<p>Es obliegt dem Nutzer, B1 M&auml;ngel in nachvollziehbarer und detaillierter Form unter Angabe der f&uuml;r die M&auml;ngelerkennung zweckdienlichen Informationen mitzuteilen. Die Beschreibung des Mangels hat so detailliert zu erfolgen, dass dieser von B1 genau bestimmt und nachvollzogen werden kann.</p>
<p>Der Nutzer erkennt zudem an, dass&nbsp;B1&nbsp;nicht f&uuml;r die Verf&uuml;gbarkeit externer Websites&nbsp;und Services&nbsp;verantwortlich&nbsp;ist&nbsp;und dass&nbsp;B1&nbsp;keine&nbsp;Services, Produkte oder andere Materialien auf oder von oder &uuml;ber externe Websites&nbsp;und Anbieter&nbsp;unterst&uuml;tzt.</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>Schlussbestimmungen</li>
    </ol>
</div>
<p>Datenspeicherung und Datenschutz</p>
<p>Die&nbsp;Nutzerdaten&nbsp;werden bei uns bis zur vollst&auml;ndigen Abwicklung&nbsp;einer&nbsp;Bestellung (auch zur Abwicklung von Anfragen des&nbsp;Nutzers&nbsp;zur Bestellung) gespeichert, danach f&uuml;r die steuer- und handelsrechtliche Aufbewahrung archiviert.</p>
<p>F&uuml;r die Verarbeitung personenbezogener Daten gilt&nbsp;die&nbsp;Datenschutzerkl&auml;rung&nbsp;von B1, die&nbsp;Nutzer im Nutzerkonto&nbsp;abrufen k&ouml;nnen.</p>
<p>&Auml;nderungen dieser Nutzungsbedingungen</p>
<p>B1 beh&auml;lt sich das Recht vor, die Nutzungsbedingungen zu &auml;ndern. &Auml;nderungen dieser Nutzungsbedingungen werden dem Nutzer &uuml;ber das Nutzerkonto angeboten. Diese &Auml;nderungen werden nur wirksam, wenn der Nutzer diese annimmt.</p>
<p>Die Nutzungsbedingungen kann der Nutzer jederzeit in der jeweils aktuellen Fassung in der Sportworld einsehen und herunterladen.</p>
<p>Au&szlig;ergerichtliche Streitschlichtung</p>
<p>Die EU-Kommission hat gem&auml;&szlig; der EU-Verordnung Nr. 524/2013 eine interaktive Website zur Online-Streitbeilegungsplattform (OS-Plattform) zur Schlichtung au&szlig;ergerichtlicher Streitigkeiten aus Online-Rechtsgesch&auml;ften bereitgestellt. Die OS-Plattform der EU-Kommission ist unter diesem Link abrufbar:&nbsp;https://ec.europa.eu/consumers/odr/&nbsp;an die sich Nutzer jederzeit wenden k&ouml;nnen. Die E-Mail-Adresse von B1 ist im Impressum aufgef&uuml;hrt. An diesem Streitschlichtungsverfahren nimmt B1 nicht teil.</p>
<p>An einem Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle nimmt B1 nicht teil und ist hierzu auch nicht verpflichtet.</p>
<p>B1 ist jedoch bem&uuml;ht, bei Meinungsverschiedenheiten mit den Nutzern eine einvernehmliche L&ouml;sung zu finden. Zur Kl&auml;rung von Fragen kann sich der Nutzer jederzeit an den Sportworld Kundenservice wenden.</p>
<p>Schlussvereinbarungen</p>
<p>Das Vertragsverh&auml;ltnis unterliegt dem Recht der Bundesrepublik Deutschland unter Ausschluss des UN-&Uuml;bereinkommens &uuml;ber Vertr&auml;ge &uuml;ber den internationalen Warenverkauf, soweit nicht auf Grund anwendbaren zwingenden Rechts das Recht des Landes anwendbar ist, in dem die Inhalte oder Dienste dem Nutzer angeboten werden. Dar&uuml;ber hinaus sind die zwingenden Verbraucherschutzbestimmungen anwendbar, die in dem Staat gelten, in dem der Nutzer seinen gew&ouml;hnlichen Aufenthalt und ein Abonnement gebucht hat, sofern diese dem Nutzer einen weitergehenden Schutz gew&auml;hren.</p>
<p>Hat der Nutzer seinen Sitz bzw. Wohnsitz nicht in der Bundesrepublik Deutschland und ist auch kein Aufenthaltsort in der Bundesrepublik Deutschland bekannt, ist der jeweilige Sitz von B1 ausschlie&szlig;licher Gerichtsstand. Im &Uuml;brigen gelten die gesetzlichen Gerichtsst&auml;nde. Diese Gerichtsstandsvereinbarung gilt nicht, soweit durch Gesetz ein ausschlie&szlig;licher Gerichtsstand begr&uuml;ndet ist.&nbsp;</p>
<p>Stand: 09/2023</p>""",
        },
        {
            "locales": ["en-US"],
            "value": """<p>Terms of Use</p>
<div>
    <ol>
        <li>Scope of service</li>
    </ol>
</div>
<p>These Terms of Use are applicable to the registration and use of all content made available by B1SmartTV GmbH with its headquarter in Munich, Ainmillerstra&szlig;e 28, 80801 Munich (Local Court Munich, HRB 235921) (in the following referred to as &quot;B1&quot;) to customer (in the following referred to as &quot;user&quot;) in the Sportworld App, via the Sportworld website or via other distribution channels (in the following referred to as &quot;Sportworld&quot;) free of charge, subject to a registration or subject to a paid subscription (e.g. via paid passes, programme packages and package combinations) (in the following referred to as &quot;content&quot;), the use of a platform, if provided, for the acquisition of so-called non-fungible tokens (NFT), as well as functions and other services.&nbsp;</p>
<p>Certain functions and other services (in the following referred to as &quot;Services&quot;) may be subject to additional or different terms and conditions (in the following referred to as &quot;Special Conditions&quot;, whereby Special Conditions together with these Terms and Conditions of Use are also referred to as &quot;Terms of Use&quot;), which the user must agree to and to which B1 will inform the user in good time prior to the use of such services. In the event and to the extent that Special Conditions contradict these terms and conditions, the Special Conditions shall prevail.&nbsp;</p>
<p>In addition, to the extent that third party providers will be engaged by the User for the use of certain services, B1 will make the User aware of such third party providers prior to the use of such services. Regardless of whether or not third party services and/or services are integrated into Sportworld, such services/services are provided by third party providers under their sole responsibility under the terms of use and privacy policy of the respective third party provider. If the User does not accept these Third Party Provider Terms and Conditions, the User will not be able to use such services, which may also limit the use of the services provided by B1. B1 assumes no liability for third party providers.</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>General conditions for the use of Sportworld</li>
    </ol>
</div>
<p>One-time registration and user account</p>
<p>The user can access, receive and use the content and services via Sportworld, which is available on suitable internet-enabled devices such as SmartTVs, smartphones, tablets, TV sticks and, if applicable, other entertainment systems (in the following together referred to as &quot;distribution channels&quot;) and may have to be installed.&nbsp;</p>
<p>In order to be able to use the content and services which are subject to payment and/or registration, the user must register in Sportworld for the first time and create a Sportworld account (&quot;user account&quot;), via which subscriptions can also be booked. Upon completion of the registration, a free user account is initially set up for the user and the user receives a confirmation of the registration by e-mail. The user has unrestricted access to his user account at any time. Only a limited range of services is available to the user in Sportworld without registration. The user is only obliged to pay if the user has ordered paid contents or services via Sportworld.</p>
<p>The user is obliged to provide the data required for registration, i.e., in particular name, e-mail address and payment data, correctly and completely and to update them immediately in the event of changes. Only persons who have reached the age of majority are entitled to register and open a user account.&nbsp;</p>
<p>The user must enter his or her customer number or e-mail address and password (login data) before using the content and services that are subject to charges and/or registration. It is only permitted to pass on the login data to persons living in the same household. The user is only entitled to allow children and young people to access the content if the content is approved for their age in accordance with the applicable youth protection law and is not excluded from use for other compelling legal reasons.&nbsp;</p>
<p>Subscription Agreement</p>
<p>For using paid content during a subscription period, the user must place additional individual orders of Sportworld offers, such as monthly or annual passes, (&quot;subscription&quot;), which can be placed and managed in the user account.&nbsp;</p>
<p>When ordering paid content, a subscription agreement is concluded between B1 and the user and grants the user access to the selected and booked subscription for the agreed subscription period and the agreed costs. The user will be informed of the duration of the service provision and the costs in each case before the order is placed in Sportworld. After placing the order, the user receives a confirmation by e-mail with all information about the subscription. The user can call up an overview and details of his subscriptions via his user account after placing the order.</p>
<p>The subscriptions in Sportworld are subject to change and do not yet represent a legally binding offer by B1. By activating the order button, the user submits a binding request for placing the order for a subscription. The user can check and correct the entries at any time during the order process. German is the binding language for placing the order and English for Sportworld offers outside of Germany or Austria, as far as the respective national language is not offered. B1 has the discretion to accept the order which is necessary for the conclusion of the subscription agreement and can reject it in particular if there are factual reasons (e.g., insufficient proof of age). The subscription agreement is concluded when the subscription has been activated and the user receives an order confirmation by e-mail. B1 does not intend to store the text of the contract separately. In each case, the content of the subscription results from the details of the order confirmation sent by e-mail (including the offer description and price information valid at the time of the order, which become part of the Subscription Agreement) and the Terms of Use. The corresponding information can be viewed in the user account.&nbsp;</p>
<p>B1 reserves the right to make the provision or use of offers in Sportworld dependent on the user confirming the e-mail address used for placing the order via a confirmation link sent by e-mail.</p>
<p>The various subscriptions can be booked individually and cancelled individually. Should one or more additional programme packages (upgrade) be booked, the terms of the booked subscriptions are applicable in each case, which may not be synchronised with each other.</p>
<p>When the subscription agreement comes into effect, B1 will make the paid content available to the user for streaming live or on-demand. A permanent copy is not created on the user&apos;s device.</p>
<p>Range of programmes</p>
<p>The design and availability of content may vary over time and is usually subject to certain restrictions. You may view content in any country where it is available, however the content (and the language, if any, available) may vary from country to country. The content may only be used within the agreed territory in which B1 has licensed and specifically offers the content to the user. If B1 uses technical measures for this purpose (e.g., geolocation based on the IP address of the internet connection used), the user is not entitled to circumvent or interfere with these measures. The user is entitled to access and use the online content service within the framework of the Regulation of the European Parliament and of the Council on ensuring cross-border portability of online content services in the internal market as long as the user is temporarily present in another EU member state.</p>
<p>B1 is entitled to make only minor changes to the programme offer in subscriptions with reasonable notice, provided that these are still acceptable to the user in good faith in relation to the overall agreed range of programmes, considering the interests of both parties without any further compensation for disadvantages. Such a situation shall be deemed to exist if B1 continues to provide the user with equivalent (&quot;comparable&quot;) content that preserves the overall character of the subscription and the adjustments become necessary due to circumstances that occurred after the conclusion of the subscription agreement. For example, such circumstances justifying a change can be the loss of limited or the loss of unlimited licence rights for subscriptions that are the subject of the subscription agreement through no fault of B1 (loss of rights), or technical reasons that are not the fault of B1 or its vicarious agents (e.g. loss of cable transmission rights, changed requirements for encryption).&nbsp;</p>
<p>Technical operation</p>
<p>The user is no entitled to the availability of the content in a specific format. In Sportworld, the content is available in the respective available formats in standard resolution and the maximum playable picture quality. Not all content is available in all formats such as HD, Ultra-HD and HDR and not all subscriptions allow the reception of content in all formats.</p>
<p>The transmission quality of the content may vary and depends on a range of factors, such as location, the available bandwidth and/or the speed of the internet connection, over which B1 has no control. The user is responsible, at his or her own expense, for meeting the system requirements necessary for the use of Sportworld and for ensuring sufficient and constant data transmission.</p>
<p>B1 undertakes appropriate technical efforts to ensure that the content is available at the agreed time with as little disruption as possible. B1 cannot, however, guarantee that the content will be available. Technical failures caused in particular by force majeure can lead to an interruption of the retrievability. Furthermore, B1 is not responsible for the cancellation or discontinuation of an event or for the ability to show an event as scheduled or advertised, nor for the ability to view an event on any particular device.</p>
<p>From time to time, B1 may need to interrupt Sportworld for updates or maintenance. B1 will, however, endeavour to keep such interruptions to a minimum.</p>
<p>B1 cannot be held responsible if certain TV devices, mobile devices or applications used by the user and their configurations do not work or have an impact on the use of the content or the playback quality. The use of proxy servers may lead to transmission problems. It is prohibited to conceal or disguise the location via other IP addresses or other technical methods. The user is obliged to report any defects that occur, logging any error messages that may be displayed.&nbsp;</p>
<p>In the event that third party applications (including websites, widgets, software, or other software utilities) interact with the Sportworld Service, the use of such third-party services may be subject to the third-party Terms and Conditions of Use with which the user is required to comply.</p>
<p>Restriction on Use</p>
<p>User may only access the content through B1&apos;s authorised distribution channels. The user is authorised to use the subscriptions on a maximum of two (2) TV sets and a maximum of four (4) mobile devices (e.g., tablet, in-car entertainment system) belonging to the same household at the same time. B1 reserves the right to temporarily allow additional devices.</p>
<p>The content is legally protected, in particular by copyright and ancillary copyright. The user may not disable, circumvent, modify, or otherwise undermine any access technology, labelling, or other protection systems, such as digital rights management (DRM), used to protect the content, or geolocation.</p>
<p>The content may only be used for private purposes within the time limits provided for in the subscription agreement and may not be used for commercial purposes. The contents may in particular not be edited, changed, copied, stored, or made accessible to third parties or the public in any way (e.g., by uploading to so-called file or streaming sharing systems).&nbsp;</p>
<p>The user is only entitled to a limited, non-exclusive, non-transferable, and spatially restricted right to access and use the content only within the scope and for the duration of an existing subscription. Except for the foregoing limited right of use, no right, title, or interest in or to any content and/or materials provided is granted or transferred to the user. The user is no longer entitled to access the subscriptions upon termination of the subscription.</p>
<p>If the user does not comply with the Terms of Use, B1 reserves the right to block the user&apos;s account.</p>
<p>Prices and method of payment</p>
<p>The product price is based on the price information given before the order process is completed. All price quotations are inclusive of the applicable statutory value added tax. The fixed monthly fees and other payments are due on the payment date listed in the user account for the booked subscription. Payments for subscriptions are invoiced monthly at the beginning of each subscription period and are due immediately. On the day, the subscription agreement is concluded, the first invoice period begins and ends at the end of the last day of the subscription period. The fees for day tickets and event tickets are due for payment and debited at the time of placing the order for the respective offer. In the case that a free trial period is agreed, the chargeable invoice period shall commence on the agreed date when the user has placed the order for a subscription. Otherwise, the free trial period ends on the last day of the agreed trial period.</p>
<p>Payments within the scope of the business relationship shall be made, unless otherwise specified, via credit card payment, PayPal or another offered means of payment, depending on the agreement. In no case is a cash payment possible.&nbsp;</p>
<p>The user must be registered or register with the respective provider for payment with certain payment methods, e.g., PayPal, ApplePay, Amazon Pay. Once the user has entered his access data for his account on the page of the specific provider, the user must confirm the payment instruction to B1 by means of the deposited payment method. The user is finally redirected back to Sportworld, where the user completes the order process. Payment is made immediately after placing the order.</p>
<p>The user will be provided with the statements for the booked subscriptions in the user account or by e-mail.</p>
<p>Price Adjustments</p>
<p>B1 is entitled to adjust the fees agreed with the user in accordance with the following provisions at its reasonable discretion if the procurement or provision costs on which the subscription is based, such as fees for programme licences, fees for technical services, customer service and other turnover costs, general administrative costs (&quot;total costs&quot;) change after the conclusion of the subscription agreement due to circumstances that could not be foreseen at the time of the conclusion of the subscription agreement and which are not at the discretion of B1.</p>
<p>B1 can only increase the fees once within a calendar year. Eight weeks prior to the effective date, the user will be informed about an impending price increase. B1 will specifically inform the user of any right of termination and the period of notice as well as the consequences of a termination not received in time as part of the notification of the price increase.</p>
<p>The right of termination is only applicable to the subscription affected by the price increase. If the subscription affected by the price increase is a prerequisite for another subscription, however, a termination is also applicable to the latter. In the event that the user does not terminate the subscription or does not do so in time, the subscription shall be continued at the time stated in the notification with the new fees.</p>
<p>Notwithstanding the above provisions, B1 is entitled in the event of an increase in statutory fees, contributions, taxes, and levies, such as value added tax, and obliged in the event of a reduction to adjust the fees accordingly.&nbsp;</p>
<p>Term and termination of subscriptions</p>
<p>All subscriptions shall have the term specified in the respective subscription agreement&nbsp;(&quot;Subscription Period&quot;). The user may terminate a subscription at any time at the end of the agreed term. In the user account, the user can view the term and the next possible termination date. The user can follow the instructions in the user account to cancel the subscription. It is not necessary to indicate reasons for termination.&nbsp;</p>
<p>The subscription agreement for the temporary provision of content (VoD streaming) or for one-time live streams ends automatically upon expiry of the temporary provision or the live stream without the need for termination.</p>
<p>If payments are not only slightly in arrears, B1 may withdraw access to the content concerned for the duration of the arrears and/or refuse to provide further services. It is not possible to place further orders for subscriptions until the end of the payment default.&nbsp;</p>
<p>B1 also reserves the right to delete user accounts that have obviously not been used for a period of more than 12 months. After termination of the user account, B1 has the right to assign an alias (user/username) used by the user to other users.&nbsp;</p>
<p>Even after termination of the customer account and termination of subscriptions, the user is entitled to use free content.</p>
<p>If B1 is no longer able to provide the user with individual content, subscriptions/tickets, or programme combinations due to licensing or technical reasons, B1 has the right to terminate the subscription concerned with a reasonable period of notice.&nbsp;</p>
<p>For both parties, the right to terminate for good cause remains unaffected.</p>
<p>Right of withdrawal</p>
<p>Consumers have a right of withdrawal for subscriptions in accordance with the cancellation policy. The user may download the current cancellation policy and cancellation form the Sportworld account.</p>
<p>The withdrawal from a subscription can be made verbally, by telephone or in text form.</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>General conditions for the purchase of NFT</li>
    </ol>
</div>
<p>NFT platform, availability and definitions</p>
<p>In order to be able to purchase NFTs via Sportworld, the user must register in Sportworld and create a user account, which can also be used to book subscriptions. Upon completion of registration, a free user account is initially created for the user and the user receives a confirmation of registration by e-mail. The user can dispose of his user account at any time without restrictions. A payment obligation of the user exists only if the user has ordered paid contents or services via Sportworld. These terms of use apply to the opening and use of a Sportworld account. B1 reserves the right to temporarily or permanently block the user account in case of suspicious activities and if the user is suspected to have violated or actually violated the Terms of Use or Special Conditions.</p>
<p>Before using the NFT platform, the user is required to enter his customer number or e-mail and password (login data).</p>
<p>The NFT Platform is not available in all countries where Sportworld is available, but only in selected countries. An availability of the NFT platform is displayed in the user account.</p>
<p>The user is prohibited from accessing or using Sportworld (or any of our other services) at, from or through any location where such use is unavailable or in violation of any applicable law. By using Sportworld, User represents and warrants that User is not a citizen or resident of any such jurisdiction, nor will User use Sportworld while located or residing in any such jurisdiction.</p>
<p>NFT is defined as a digital artwork of a cryptographic token registered on a blockchain network, which is non-exchangeable and a non-replicable unique token sold by B1 on Sportworld, currently based on the Polygon Blockchain (https://polygon.technology/). NFT are not securities within the meaning of the German Securities Trading Act (WpHG) or financial instruments within the meaning of the German Banking Act (KWG) or any other similar applicable law and are not legally to be treated as such. NFT are not acquired or used for investment purposes. NFT-Content is defined as all content, files and materials represented by or contained in the purchased NFT that are licensed as part of the purchase of the NFT, including but not limited to graphics, videos, text, trademarks, logos, images and photographs.</p>
<p>Purchase of NFT</p>
<p>The User may, subject to the conclusion of an individual purchase agreement with B1, purchase NFTs for a fixed remuneration in accordance with the procedure described below. The opening of a user account alone, i.e. without the purchase of an NFT, does not result in a purchase and/or payment obligation on the part of the user. The entitlement to purchase NFTs, for example from certain NFT Collections, may be made dependent on certain criteria.</p>
<div>
    <ol>
        <li>Digital Wallet</li>
    </ol>
</div>
<p>&nbsp;</p>
<p>A prerequisite for the acquisition of NFTs is that the user is the owner of a Polygon Blockchain compatible Digital Wallet for receiving, storing, transferring, exchanging or issuing NFTs. The address of this digital wallet must be communicated and linked to the user account. For this purpose, B1 uses the &quot;Wallet-connect&quot; service at https://walletconnect.com/ with the following terms of use (https://walletconnect.com/terms) and privacy policy (https://walletconnect.com/privacy).</p>
<p>&nbsp;</p>
<p>Currently, this service offers the possibility to link a digital wallet from Metamask, Coinbase or another digital wallet compatible with Wallet Connect. If NFT are transferred to an incompatible Digital Wallet, it may result in the permanent unusability of the NFT. B1 does not offer a Digital Wallet itself and is not obligated to do so.&nbsp;</p>
<p>&nbsp;</p>
<p>Further costs may be incurred for the opening or use of a digital wallet, which are to be borne by the user.</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>Selection of NFT</li>
    </ol>
</div>
<p>&nbsp;</p>
<p>The User may select his NFT from existing NFTs, which may be limited to the aforementioned number, or use &quot;My Moment&quot; to capture his personal moment in a unique digital collectible by defining in real time a limited number of short highlight scenes from a game, e.g. the European League of Football, with a length of a few seconds specified by B1, in order to customize/influence the final appearance of the content underlying the NFT, e.g. design it as a 3D animated cube as NFT. It is at B1&apos;s sole discretion to provide such customization options.</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>Acquisition and deposition of credits</li>
    </ol>
</div>
<p>&nbsp;</p>
<p>After selecting an NFT, the user will receive an overview of the selected NFT and the total amount of remuneration. An NFT can only be acquired by redeeming credits previously acquired in Sportworld. The number of credits required as well as their value in euros to purchase the NFT is displayed in the order process. If the user does not have the sufficient number of credits, he must first purchase them in Sportworld.</p>
<p>&nbsp;</p>
<p>The user can select the number of credits to be purchased from the available credits. The user accepts the offer to purchase the selected credit by clicking the button &quot;Buy&quot; or a similar formulation and then confirming it. With the confirmation, the corresponding named number of credits is purchased and credited to the user account upon completion of the payment.</p>
<p>&nbsp;</p>
<p>If the user has been granted a credit by a B1 partner as part of a marketing campaign, this can be redeemed by entering a code received and the credit can be stored in the user account.</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>Acquisition and transfer of NFTs</li>
    </ol>
</div>
<p>The User accepts the offer to purchase the selected NFT by clicking the &quot;Buy&quot; button or a similar wording and subsequently confirming it. Upon confirmation, the corresponding named number of credits will be deducted from the User&apos;s account and the limited NFT will be transferred to the stored Digital Wallet. Provided that a configured NFT, e.g. 3D animated cube as NFT, has been selected and designed via &quot;My Moment&quot;, minting begins with the confirmation, i.e. the NFT is created and published in the blockchain and then transferred to the user&apos;s deposited Digital Wallet. Minting takes place via B1&apos;s own application or via common platforms for minting NFT.</p>
<p>&nbsp;</p>
<p>The transfer of the NFT is deemed to have taken place when the NFT appears in the user&apos;s Digital Wallet, thereby fully documenting the process in the Blockchain.</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>Changes to the order process</li>
    </ol>
</div>
<p>&nbsp;</p>
<p>With the confirmation, the user sends the binding order to B1. From this point on, it is unfortunately no longer possible to change the order or data. The user can terminate the order process at any time before clicking on the confirmation or return to the previous pages to correct any errors or change the purchase.</p>
<p>&nbsp;</p>
<p>Internet access is required for the purchase and transfer of the NFT. The User is solely responsible for any hardware, systems and/or software programs required for the purchase or transfer of the NFT.</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>Confirmation</li>
    </ol>
</div>
<p>&nbsp;</p>
<p>After completion of the purchase, the user receives from B1 an order and order confirmation with all order data and the entire contract text to by e-mail.&nbsp;</p>
<p>For the conclusion of the contract only the German and English language is available in Sportworld.</p>
<p>Copyrights and owners of the NFT</p>
<p>The owner of the NFT is the person who acquires an NFT in accordance with these terms and conditions. This ownership is ensured and verified by a specific protocol (Smart Contract). B1 makes no warranties or promises in relation to Smart Contracts, in particular B1 has no control over the User&apos;s ownership of the NFT and cannot change it.</p>
<p>All intellectual property rights, in particular copyright and trademark rights, in the NFT Platform and all Content made available through the NFT Platform are vested in B1 or have been granted to B1 by a third party licensor. No intellectual property rights are granted to the User.</p>
<p>Upon successful transfer of the NFT to the User, B1 grants the User a worldwide, non-exclusive, fully paid-up license to use, reproduce and display the NFT solely for the User&apos;s personal, non-commercial use. The User may transfer the license to a third party only if the User transfers the NFT.</p>
<p>The user may freely dispose of NFTs of which he is the holder without further involvement of B1. Transfer or sale of the NFTs on B1&apos;s NFT platform is not possible. Users shall only have the option to offer the NFTs for sale on a third-party marketplace, subject to the provisions that may be set for each NFT on an NFT platform. It is the sole responsibility of the user to check which rights are associated with an NFT, which conditions apply, in particular which costs are incurred.</p>
<p>Safety and technical operation</p>
<p>B1 shall make reasonable technical efforts to ensure the security of the NFT platform and to make it available as free of disruptions as possible. In particular, technical failures caused by force majeure may lead to an interruption of the retrievability. B1 cannot guarantee that the NFT Platform and/or the NFTs are free of viruses and/or other computer code that may contain contaminating or destructive features. It is the User&apos;s responsibility to take appropriate computer security measures (including anti-virus and other security controls) to meet its particular information security and reliability requirements.</p>
<p>Occasionally, B1 may need to interrupt Sportworld for updates or maintenance. However, B1 will endeavor to keep such interruptions to a minimum.</p>
<p>In the event that third-party applications (including websites, widgets, software or other software utilities) interact with the Sportworld Service, use of those third-party services may be subject to the third-party terms of use with which the user is required to comply.</p>
<p>Prices and method of payment</p>
<p>The prices for credits or NFTs result from the price quotation listed before completion of the order process. All price quotations are inclusive of the applicable statutory value added tax, but do not include the so-called gas fees to be paid by the user for the respective transaction, i.e. variable costs of third-party providers, such as transaction costs, e.g. for the digital wallet and internet costs, over which B1 has no influence. Such fees and costs are not charged to the User by B1 but by third parties and therefore cannot be displayed in the order process. It is the user&apos;s responsibility to inform himself about these costs before purchasing NFTs.</p>
<p>Credits are to be used for the acquisition of NFTs, which are exclusively purchased in Sportworld or made available to the user within the scope of a marketing campaign. The payment of the credits takes place, as far as not differently specified, depending upon agreement over credit card payment, PayPal or another offered means of payment. A cash payment is not possible in any case.&nbsp;</p>
<p>The user must be registered or register with the respective provider for payment with certain payment methods, e.g., PayPal, ApplePay, Amazon Pay. Once the user has entered his access data for his account on the page of the specific provider, the user must confirm the payment instruction to B1 by means of the deposited payment method. The user is finally redirected back to Sportworld, where the user completes the order process. Payment is made immediately after placing the order.</p>
<p>The user will be provided with the statements for the booked subscriptions in the user account or by e-mail.</p>
<p>Information on the early expiry of the right of withdrawal</p>
<p>Users are generally entitled to a right of cancellation in accordance with the cancellation policy. The user can download the current cancellation policy and cancellation form from his user account. A revocation can be made orally, by telephone or in text form.</p>
<p>The right of revocation expires in the case of a contract for the provision of services if the service has been provided in full and if the contract obliges the user to pay if the performance of the service has only begun after the user has given his express consent to this and at the same time confirmed his knowledge that he loses his right of revocation upon complete fulfillment of the contract. The right of withdrawal shall also expire in the case of a contract for the delivery of digital content that is not on a physical data carrier if the execution of the contract has begun and, if the contract obligates the user to pay after the user has expressly agreed that the execution of the contract should begin before the expiration of the withdrawal period and, at the same time, the user has confirmed his knowledge that, by giving his consent, the user loses his right of withdrawal upon the beginning of the execution of the contract, and a copy or in the confirmation of the concluded contract has been sent to the user.</p>
<p>By clicking the &quot;Buy&quot; button or similar wording and subsequent confirmation, the user agrees to the execution of the contract before the expiry of the withdrawal period and confirms that by agreeing to this, the user loses his right of withdrawal at the beginning of the execution of the contract and no refund will be made.</p>
<p>Warranty and liability</p>
<p>If an NFT purchased on the NFT platform is defective, the statutory provisions governing the rights of the user shall apply. A product purchased by B1 is free of material defects if it has the agreed quality at the time of transfer of risk. The agreed quality is the compliance with the specifications in the product description. Suitability, use or application risks are the responsibility of the user and do not constitute a defect. In particular, B1 does not guarantee that an NFT will retain its original value, as the value of NFT is inherently subjective or objective factors may significantly affect the value of a particular NFT. In addition, it should be noted that the regulatory regime for Blockchain technologies and services and products based thereon, such as NFT, is unpredictable, and new legal or regulatory requirements or policies may materially affect the development of the Blockchain and NFT market and thus the potential benefit or value of NFT.</p>
<p>Future developments and changes to this regulatory regime could affect the use of the NFT platform and development of the NFT market generally, and thus could materially affect the potential benefit or value of NFT. B1 is not liable for any consequences resulting from legal and regulatory developments for the use of the Blockchain or NFTs.</p>
<p>It is the user&apos;s responsibility to notify B1 of any defects in a comprehensible and detailed form, stating the information that is useful for identifying the defect. The description of the defect shall be in such detail that it can be precisely determined and reproduced by B1.</p>
<p>User further acknowledges that B1 is not responsible for the availability of external websites and services and that B1 does not endorse any services, products or other materials on or available from or through external websites and providers.</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>Final Provisions</li>
    </ol>
</div>
<p>Data storage and data protection</p>
<p>User data is stored by B1 until an order has been processed in full (including for the purpose of processing user inquiries about the order), after which it is archived for storage in accordance with tax and commercial law.</p>
<p>The processing of personal data is governed by B1&apos;s privacy policy, which users can access in their user account.</p>
<p>Changes to these Terms of Use</p>
<p>B1 reserves the right to change the Terms of Use. Changes to these Terms of Use will be offered to the user via the user account. These changes only become effective if the user accepts them.</p>
<p>The user can view the current version of the Terms of Use in Sportworld at any time.</p>
<p>Out-of-court dispute resolution</p>
<p>The EU Commission has provided an interactive website for the online dispute resolution platform (OS platform) for the resolution of out-of-court disputes arising from online legal transactions in accordance with EU Regulation No. 524/2013. The EU Commission&apos;s ODR platform can be accessed via this link:&nbsp;https://ec.europa.eu/consumers/odr/ which users can contact at any time.&nbsp;B1&apos;s email address is listed in the imprint. B1 does not participate in this dispute resolution procedure.</p>
<p>B1 does not participate in dispute resolution proceedings before a consumer arbitration board and has no obligation to do so.</p>
<p>B1 will, however, endeavour to find an amicable solution in the event of disagreements with users. The user can contact the Sportworld customer service at any time to clarify any questions.</p>
<p>Final agreements</p>
<p>The contractual relationship is governed by the law of the Federal Republic of Germany to the exclusion of the UN Convention on Contracts for the International Sale of Goods, to the extent that the law of the country in which the content or services are offered to the user is not applicable due to applicable mandatory law. The mandatory consumer protection provisions that are applicable in the country in which the user has his or her habitual residence and has booked a subscription are also applicable, as far as these provide the user with more extensive protection.</p>
<p>In the event that the user does not have his or her headquarters or place of residence in the Federal Republic of Germany and if no place of residence in the Federal Republic of Germany is known, the respective headquarter of B1 shall be the exclusive place of jurisdiction. In all other respects, the statutory places of jurisdiction are applicable. This jurisdiction agreement is not applicable if an exclusive jurisdiction is established by law.&nbsp;</p>
<p>Stand: 09/2023</p>""",
        },
    ],
    "url": "https://sportworld.tv/agb",
}

legal_terms_mp2 = {
    "html": [
        {
            "locales": ["en-US"],
            "value": """<p>Terms of Use</p>
<p>World (without EU and Switzerland)</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>Scope of service</li>
    </ol>
</div>
<p>These Terms of Use are applicable to the registration and use of all content made available by B1SmartTV GmbH with its headquarter in Munich, Ainmillerstra&szlig;e 28, 80801 Munich (Local Court Munich, HRB 235921) (in the following referred to as &quot;B1&quot;) to customer worldwide (except EU and Switzerland) (in the following referred to as &quot;user&quot;) in the Sportworld App, via the Sportworld website or via other distribution channels (in the following referred to as &quot;Sportworld&quot;) free of charge, subject to a registration or subject to a paid subscription (e.g. via paid passes, programme packages and package combinations) (in the following referred to as &quot;content&quot;), the use of a platform, if provided, for the acquisition of so-called non-fungible tokens (NFT), &nbsp;as well as functions and other services.&nbsp;</p>
<p>Certain functions and other services (in the following referred to as &quot;Services&quot;) may be subject to additional or different terms and conditions (in the following referred to as &quot;Special Conditions&quot;, whereby Special Conditions together with these Terms and Conditions of Use are also referred to as &quot;Terms of Use&quot;), which the user must agree to and to which B1 will inform the user in good time prior to the use of such services. In the event and to the extent that Special Conditions contradict these terms and conditions, the Special Conditions shall prevail.&nbsp;</p>
<p>In addition, to the extent that third party providers will be engaged by the User for the use of certain services, B1 will make the User aware of such third party providers prior to the use of such services. Regardless of whether or not third party services and/or services are integrated into Sportworld, such services/services are provided by third party providers under their sole responsibility under the terms of use and privacy policy of the respective third party provider. If the User does not accept these Third Party Provider Terms and Conditions, the User will not be able to use such services, which may also limit the use of the services provided by B1. B1 assumes no liability for third party providers.</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>General conditions for the use of Sportworld</li>
    </ol>
</div>
<p>One-time registration and user account</p>
<p>The user can access receive and use the content and services via Sportworld, which is available on suitable internet-enabled devices such as SmartTVs, smartphones, tablets, TV sticks and, if applicable, other entertainment systems (in the following together referred to as &quot;distribution channels&quot;) and may have to be installed.&nbsp;</p>
<p>To be able to use the content and services which are subject to payment and/or registration, the user must register in Sportworld for the first time and create a Sportworld account (&quot;user account&quot;), via which subscriptions can also be booked. Upon completion of the registration, a free user account is initially set up for the user and the user receives a confirmation of the registration by e-mail. The user has unrestricted access to his user account at any time. Only a limited range of services is available to the user in Sportworld without registration. The user is only obliged to pay if the user has ordered paid contents or services via Sportworld.</p>
<p>The user is obliged to provide the data required for registration, i.e., in particular name, e-mail address and payment data, correctly and completely and to update them immediately in the event of changes. Only persons who have reached the age of majority are entitled to register and open a user account.&nbsp;</p>
<p>The user must enter his or her customer number or e-mail address and password (login data) before using the content and services that are subject to charges and/or registration. It is only permitted to pass on the login data to persons living in the same household. The user is only entitled to allow children and young people to access the content if the content is approved for their age in accordance with the applicable youth protection law and is not excluded from use for other compelling legal reasons.&nbsp;</p>
<p>Subscription Agreement</p>
<p>For using paid content during a subscription period, the user must place additional individual orders of Sportworld offers, such as monthly or annual passes (&quot;subscription&quot;), which can be placed and managed in the user account.&nbsp;</p>
<p>When ordering paid content, a subscription agreement is concluded between B1 and the user and grants the user access to the selected and booked subscription for the agreed subscription period and the agreed costs. The user will be informed of the duration of the service provision and the costs in each case before the order is placed in Sportworld. After placing the order, the user receives a confirmation by e-mail with all information about the subscription. The user can call up an overview and details of his subscriptions via his user account after placing the order.</p>
<p>The subscriptions in Sportworld are subject to change and do not yet represent a legally binding offer by B1. By activating the order button, the user submits a binding request for placing the order for a subscription. The user can check and correct the entries at any time during the order process. German is the binding language for placing the order and English for Sportworld offers outside of Germany or Austria, as far as the respective national language is not offered. B1 has the discretion to accept the order which is necessary for the conclusion of the subscription agreement and can reject it in particular if there are factual reasons (e.g., insufficient proof of age). The subscription agreement is concluded when the subscription has been activated and the user receives an order confirmation by e-mail. B1 does not intend to store the text of the contract separately. In each case, the content of the subscription results from the details of the order confirmation sent by e-mail (including the offer description and price information valid at the time of the order, which become part of the Subscription Agreement) and the Terms of Use. The corresponding information can be viewed in the user account.&nbsp;</p>
<p>B1 reserves the right to make the provision or use of offers in Sportworld dependent on the user confirming the e-mail address used for placing the order via a confirmation link sent by e-mail.</p>
<p>The various subscriptions can be booked individually and cancelled individually. Should one or more additional programme packages (upgrade) be booked, the terms of the booked subscriptions are applicable in each case, which may not be synchronised with each other.</p>
<p>When the subscription agreement comes into effect, B1 will make the paid content available to the user for streaming live or on-demand. A permanent copy is not created on the user&apos;s device.</p>
<p>Range of programmes</p>
<p>The design and availability of content may vary over time and is usually subject to certain restrictions. You may view content in any country where it is available, however the content (and the language, if any, available) may vary from country to country. The content may only be used within the agreed territory in which B1 has licensed and specifically offers the content to the user. If B1 uses technical measures for this purpose (e.g., geolocation based on the IP address of the internet connection used), the user is not entitled to circumvent or interfere with these measures. The user is entitled to access and use the online content service within the framework of the applicable rules and regulation.</p>
<p>B1 is entitled to make only minor changes to the programme offer in subscriptions with reasonable notice, provided that these changes are still acceptable to the user in good faith in relation to the overall agreed range of programmes, considering the interests of both parties without any further compensation for disadvantages. Such a situation shall be deemed to exist if B1 continues to provide the user with equivalent (&quot;comparable&quot;) content that preserves the overall character of the subscription and the adjustments become necessary due to circumstances that occurred after the conclusion of the subscription agreement. For example, such circumstances justifying a change can be the loss of limited or the loss of unlimited licence rights for subscriptions that are the subject of the subscription agreement through no fault of B1 (loss of rights), or technical reasons that are not the fault of B1 or its vicarious agents (e.g. loss of cable transmission rights, changed requirements for encryption).&nbsp;</p>
<p>Technical operation</p>
<p>The user is no entitled to the availability of the content in a specific format. In Sportworld, the content is available in the respective available formats in standard resolution and the maximum playable picture quality. Not all content is available in all formats such as HD, Ultra-HD and HDR and not all subscriptions allow the reception of content in all formats.</p>
<p>The transmission quality of the content may vary and depends on a range of factors, such as location, the available bandwidth and/or the speed of the internet connection, over which B1 has no control. The user is responsible, at his or her own expense, for meeting the system requirements necessary for the use of Sportworld and for ensuring sufficient and constant data transmission.</p>
<p>B1 undertakes appropriate technical efforts to ensure that the content is available at the agreed time with as little disruption as possible. B1 cannot, however, guarantee that the content will be available. Technical failures caused in particular by force majeure can lead to an interruption of the retrievability. Furthermore, B1 is not responsible for the cancellation or discontinuation of an event or for the ability to show an event as scheduled or advertised, nor for the ability to view an event on any particular device.</p>
<p>From time to time, B1 may need to interrupt Sportworld for updates or maintenance. B1 will, however, endeavour to keep such interruptions to a minimum.</p>
<p>B1 cannot be held responsible if certain TV devices, mobile devices or applications used by the user and their configurations do not work or have an impact on the use of the content or the playback quality. The use of proxy servers may lead to transmission problems. It is prohibited to conceal or disguise the location via other IP addresses or other technical methods. The user is obliged to report any defects that occur, logging any error messages that may be displayed.&nbsp;</p>
<p>In the event that third party applications (including websites, widgets, software, or other software utilities) interact with the Sportworld Service, the use of such third-party services may be subject to the third-party Terms and Conditions of Use with which the user is required to comply.</p>
<p>Restriction on Use</p>
<p>User may only access the content through B1&apos;s authorised distribution channels. The user is authorised to use the subscriptions on a maximum of two (2) TV sets and a maximum of four (4) mobile devices (e.g., tablet, in-car entertainment system) belonging to the same household at the same time. B1 reserves the right to temporarily allow additional devices.</p>
<p>The content is legally protected, in particular by copyright and ancillary copyright. The user may not disable, circumvent, modify, or otherwise undermine any access technology, labelling, or other protection systems, such as digital rights management (DRM), used to protect the content, or geolocation.</p>
<p>The content may only be used for private purposes within the time limits provided for in the subscription agreement and may not be used for commercial purposes. The contents may in particular not be edited, changed, copied, stored, or made accessible to third parties or the public in any way (e.g., by uploading to so-called file or streaming sharing systems).&nbsp;</p>
<p>The user is only entitled to a limited, non-exclusive, non-transferable, and spatially restricted right to access and use the content only within the scope and for the duration of an existing subscription. Except for the foregoing limited right of use, no right, title, or interest in or to any content and/or materials provided is granted or transferred to the user. The user is no longer entitled to access the subscriptions upon termination of the subscription.</p>
<p>If the user does not comply with the Terms of Use, B1 reserves the right to block the user&apos;s account.</p>
<p>Prices and method of payment</p>
<p>The product price is based on the price information given before the order process is completed. All price quotations are inclusive of the applicable statutory value added tax. The fixed monthly fees and other payments are due on the payment date listed in the user account for the booked subscription. Payments for subscriptions are invoiced monthly at the beginning of each subscription period and are due immediately. On the day, the subscription agreement is concluded, the first invoice period begins and ends at the end of the last day of the subscription period. The fees for day tickets and event tickets are due for payment and debited at the time of placing the order for the respective offer. In the case that a free trial period is agreed, the chargeable invoice period shall commence on the agreed date when the user has placed the order for a subscription. Otherwise, the free trial period ends on the last day of the agreed trial period.</p>
<p>Payments within the scope of the business relationship shall be made, unless otherwise specified, via credit card payment, PayPal or another offered means of payment, depending on the agreement. In no case is a cash payment possible.&nbsp;</p>
<p>The user must be registered or register with the respective provider for payment with certain payment methods, e.g., PayPal, ApplePay, Amazon Pay. Once the user has entered his access data for his account on the page of the specific provider, the user must confirm the payment instruction to B1 by means of the deposited payment method. The user is finally redirected back to Sportworld, where the user completes the order process. Payment is made immediately after placing the order.</p>
<p>The user will be provided with the statements for the booked subscriptions in the user account or by e-mail.</p>
<p>Price Adjustments</p>
<p>B1 is entitled to adjust the fees agreed with the user in accordance with the following provisions at its reasonable discretion if the procurement or provision costs on which the subscription is based, such as fees for programme licences, fees for technical services, customer service and other turnover costs, general administrative costs (&quot;total costs&quot;) change after the conclusion of the subscription agreement due to circumstances that could not be foreseen at the time of the conclusion of the subscription agreement and which are not at the discretion of B1.</p>
<p>B1 can only increase the fees once within a calendar year. Eight weeks prior to the effective date, the user will be informed about an impending price increase. B1 will specifically inform the user of any right of termination and the period of notice as well as the consequences of a termination not received in time as part of the notification of the price increase.</p>
<p>The right of termination is only applicable to the subscription affected by the price increase. If the subscription affected by the price increase is a prerequisite for another subscription, however, a termination is also applicable to the latter. In the event that the user does not terminate the subscription or does not do so in time, the subscription shall be continued at the time stated in the notification with the new fees.</p>
<p>Notwithstanding the above provisions, B1 is entitled in the event of an increase in statutory fees, contributions, taxes, and levies, such as value added tax, and obliged in the event of a reduction to adjust the fees accordingly.&nbsp;</p>
<p>Term and termination of subscriptions</p>
<p>All subscriptions shall have the term specified in the respective subscription agreement&nbsp;(&quot;Subscription Period&quot;). The user may terminate a subscription at any time at the end of the agreed term. In the user account, the user can view the term and the next possible termination date. The user can follow the instructions in the user account to cancel the subscription. It is not necessary to indicate reasons for termination.&nbsp;</p>
<p>The subscription agreement for the temporary provision of content (VoD streaming) or for one-time live streams ends automatically upon expiry of the temporary provision or the live stream without the need for termination.</p>
<p>If payments are not only slightly in arrears, B1 may withdraw access to the content concerned for the duration of the arrears and/or refuse to provide further services. It is not possible to place further orders for subscriptions until the end of the payment default.&nbsp;</p>
<p>B1 also reserves the right to delete user accounts that have obviously not been used for a period of more than 12 months. After termination of the user account, B1 has the right to assign an alias (user/username) used by the user to other users.&nbsp;</p>
<p>Even after termination of the customer account and termination of subscriptions, the user is entitled to use free content.</p>
<p>If B1 is no longer able to provide the user with individual content, subscriptions/tickets, or programme combinations due to licensing or technical reasons, B1 has the right to terminate the subscription concerned with a reasonable period of notice.&nbsp;</p>
<p>For both parties, the right to terminate for good cause remains unaffected.</p>
<div>
    <ol>
        <li>General conditions for the purchase of NFT</li>
    </ol>
</div>
<p>NFT platform, availability and definitions</p>
<p>In order to be able to purchase NFTs via Sportworld, the user must register in Sportworld and create a user account, which can also be used to book subscriptions. Upon completion of registration, a free user account is initially created for the user and the user receives a confirmation of registration by e-mail. The user can dispose of his user account at any time without restrictions. A payment obligation of the user exists only if the user has ordered paid contents or services via Sportworld. These terms of use apply to the opening and use of a Sportworld account. B1 reserves the right to temporarily or permanently block the user account in case of suspicious activities and if the user is suspected to have violated or actually violated the Terms of Use or Special Conditions.</p>
<p>Before using the NFT platform, the user is required to enter his customer number or e-mail and password (login data).</p>
<p>The NFT Platform is not available in all countries where Sportworld is available, but only in selected countries. An availability of the NFT platform is displayed in the user account.</p>
<p>The user is prohibited from accessing or using Sportworld (or any of our other services) at, from or through any location where such use is unavailable or in violation of any applicable law. By using Sportworld, User represents and warrants that User is not a citizen or resident of any such jurisdiction, nor will User use Sportworld while located or residing in any such jurisdiction.</p>
<p>NFT is defined as a digital artwork of a cryptographic token registered on a blockchain network, which is non-exchangeable and a non-replicable unique token sold by B1 on Sportworld, currently based on the Polygon Blockchain (https://polygon.technology/). NFT are not securities within the meaning of the German Securities Trading Act (WpHG) or financial instruments within the meaning of the German Banking Act (KWG) or any other similar applicable law and are not legally to be treated as such. NFT are not acquired or used for investment purposes. NFT-Content is defined as all content, files and materials represented by or contained in the purchased NFT that are licensed as part of the purchase of the NFT, including but not limited to graphics, videos, text, trademarks, logos, images and photographs.</p>
<p>Purchase of NFT</p>
<p>The User may, subject to the conclusion of an individual purchase agreement with B1, purchase NFTs for a fixed remuneration in accordance with the procedure described below. The opening of a user account alone, i.e. without the purchase of an NFT, does not result in a purchase and/or payment obligation on the part of the user. The entitlement to purchase NFTs, for example from certain NFT Collections, may be made dependent on certain criteria.</p>
<div>
    <ol>
        <li>Digital Wallet</li>
    </ol>
</div>
<p>&nbsp;</p>
<p>A prerequisite for the acquisition of NFTs is that the user is the owner of a Polygon Blockchain compatible Digital Wallet for receiving, storing, transferring, exchanging or issuing NFTs. The address of this digital wallet must be communicated and linked to the user account. For this purpose, B1 uses the &quot;Wallet-connect&quot; service at https://walletconnect.com/ with the following terms of use (https://walletconnect.com/terms) and privacy policy (https://walletconnect.com/privacy).</p>
<p>&nbsp;</p>
<p>Currently, this service offers the possibility to link a digital wallet from Metamask, Coinbase or another digital wallet compatible with Wallet Connect. If NFT are transferred to an incompatible Digital Wallet, it may result in the permanent unusability of the NFT. B1 does not offer a Digital Wallet itself and is not obligated to do so.&nbsp;</p>
<p>&nbsp;</p>
<p>Further costs may be incurred for the opening or use of a digital wallet, which are to be borne by the user.</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>Selection of NFT</li>
    </ol>
</div>
<p>&nbsp;</p>
<p>The User may select his NFT from existing NFTs, which may be limited to the aforementioned number, or use &quot;My Moment&quot; to capture his personal moment in a unique digital collectible by defining in real time a limited number of short highlight scenes from a game, e.g. the European League of Football, with a length of a few seconds specified by B1, in order to customize/influence the final appearance of the content underlying the NFT, e.g. design it as a 3D animated cube as NFT. It is at B1&apos;s sole discretion to provide such customization options.</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>Acquisition and deposition of credits</li>
    </ol>
</div>
<p>&nbsp;</p>
<p>After selecting an NFT, the user will receive an overview of the selected NFT and the total amount of remuneration. An NFT can only be acquired by redeeming credits previously acquired in Sportworld. The number of credits required as well as their value in euros to purchase the NFT is displayed in the order process. If the user does not have the sufficient number of credits, he must first purchase them in Sportworld.</p>
<p>&nbsp;</p>
<p>The user can select the number of credits to be purchased from the available credits. The user accepts the offer to purchase the selected credit by clicking the button &quot;Buy&quot; or a similar formulation and then confirming it. With the confirmation, the corresponding named number of credits is purchased and credited to the user account upon completion of the payment.</p>
<p>&nbsp;</p>
<p>If the user has been granted a credit by a B1 partner as part of a marketing campaign, this can be redeemed by entering a code received and the credit can be stored in the user account.</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>Acquisition and transfer of NFTs</li>
    </ol>
</div>
<p>The User accepts the offer to purchase the selected NFT by clicking the &quot;Buy&quot; button or a similar wording and subsequently confirming it. Upon confirmation, the corresponding named number of credits will be deducted from the User&apos;s account and the limited NFT will be transferred to the stored Digital Wallet. Provided that a configured NFT, e.g. 3D animated cube as NFT, has been selected and designed via &quot;My Moment&quot;, minting begins with the confirmation, i.e. the NFT is created and published in the blockchain and then transferred to the user&apos;s deposited Digital Wallet. Minting takes place via B1&apos;s own application or via common platforms for minting NFT.</p>
<p>&nbsp;</p>
<p>The transfer of the NFT is deemed to have taken place when the NFT appears in the user&apos;s Digital Wallet, thereby fully documenting the process in the Blockchain.</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>Changes to the order process</li>
    </ol>
</div>
<p>&nbsp;</p>
<p>With the confirmation, the user sends the binding order to B1. From this point on, it is unfortunately no longer possible to change the order or data. The user can terminate the order process at any time before clicking on the confirmation or return to the previous pages to correct any errors or change the purchase.</p>
<p>&nbsp;</p>
<p>Internet access is required for the purchase and transfer of the NFT. The User is solely responsible for any hardware, systems and/or software programs required for the purchase or transfer of the NFT.</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>Confirmation</li>
    </ol>
</div>
<p>&nbsp;</p>
<p>After completion of the purchase, the user receives from B1 an order and order confirmation with all order data and the entire contract text to by e-mail.&nbsp;</p>
<p>For the conclusion of the contract only the German and English language is available in Sportworld.</p>
<p>Copyrights and owners of the NFT</p>
<p>The owner of the NFT is the person who acquires an NFT in accordance with these terms and conditions. This ownership is ensured and verified by a specific protocol (Smart Contract). B1 makes no warranties or promises in relation to Smart Contracts, in particular B1 has no control over the User&apos;s ownership of the NFT and cannot change it.</p>
<p>All intellectual property rights, in particular copyright and trademark rights, in the NFT Platform and all Content made available through the NFT Platform are vested in B1 or have been granted to B1 by a third party licensor. No intellectual property rights are granted to the User.</p>
<p>Upon successful transfer of the NFT to the User, B1 grants the User a worldwide, non-exclusive, fully paid-up license to use, reproduce and display the NFT solely for the User&apos;s personal, non-commercial use. The User may transfer the license to a third party only if the User transfers the NFT.</p>
<p>The user may freely dispose of NFTs of which he is the holder without further involvement of B1. Transfer or sale of the NFTs on B1&apos;s NFT platform is not possible. Users shall only have the option to offer the NFTs for sale on a third-party marketplace, subject to the provisions that may be set for each NFT on an NFT platform. It is the sole responsibility of the user to check which rights are associated with an NFT, which conditions apply, in particular which costs are incurred.</p>
<p>Safety and technical operation</p>
<p>B1 shall make reasonable technical efforts to ensure the security of the NFT platform and to make it available as free of disruptions as possible. In particular, technical failures caused by force majeure may lead to an interruption of the retrievability. B1 cannot guarantee that the NFT Platform and/or the NFTs are free of viruses and/or other computer code that may contain contaminating or destructive features. It is the User&apos;s responsibility to take appropriate computer security measures (including anti-virus and other security controls) to meet its particular information security and reliability requirements.</p>
<p>Occasionally, B1 may need to interrupt Sportworld for updates or maintenance. However, B1 will endeavor to keep such interruptions to a minimum.</p>
<p>In the event that third-party applications (including websites, widgets, software or other software utilities) interact with the Sportworld Service, use of those third-party services may be subject to the third-party terms of use with which the user is required to comply.</p>
<p>Prices and method of payment</p>
<p>The prices for credits or NFTs result from the price quotation listed before completion of the order process. All price quotations are inclusive of the applicable statutory value added tax, but do not include the so-called gas fees to be paid by the user for the respective transaction, i.e. variable costs of third-party providers, such as transaction costs, e.g. for the digital wallet and internet costs, over which B1 has no influence. Such fees and costs are not charged to the User by B1 but by third parties and therefore cannot be displayed in the order process. It is the user&apos;s responsibility to inform himself about these costs before purchasing NFTs.</p>
<p>Credits are to be used for the acquisition of NFTs, which are exclusively purchased in Sportworld or made available to the user within the scope of a marketing campaign. The payment of the credits takes place, as far as not differently specified, depending upon agreement over credit card payment, PayPal or another offered means of payment. A cash payment is not possible in any case.&nbsp;</p>
<p>The user must be registered or register with the respective provider for payment with certain payment methods, e.g., PayPal, ApplePay, Amazon Pay. Once the user has entered his access data for his account on the page of the specific provider, the user must confirm the payment instruction to B1 by means of the deposited payment method. The user is finally redirected back to Sportworld, where the user completes the order process. Payment is made immediately after placing the order.</p>
<p>The user will be provided with the statements for the booked subscriptions in the user account or by e-mail.</p>
<p>Warranty and liability</p>
<p>If an NFT purchased on the NFT platform is defective, the statutory provisions governing the rights of the user shall apply. A product purchased by B1 is free of material defects if it has the agreed quality at the time of transfer of risk. The agreed quality is the compliance with the specifications in the product description. Suitability, use or application risks are the responsibility of the user and do not constitute a defect. In particular, B1 does not guarantee that an NFT will retain its original value, as the value of NFT is inherently subjective or objective factors may significantly affect the value of a particular NFT. In addition, it should be noted that the regulatory regime for Blockchain technologies and services and products based thereon, such as NFT, is unpredictable, and new legal or regulatory requirements or policies may materially affect the development of the Blockchain and NFT market and thus the potential benefit or value of NFT.</p>
<p>Future developments and changes to this regulatory regime could affect the use of the NFT platform and development of the NFT market generally, and thus could materially affect the potential benefit or value of NFT. B1 is not liable for any consequences resulting from legal and regulatory developments for the use of the Blockchain or NFTs.</p>
<p>It is the user&apos;s responsibility to notify B1 of any defects in a comprehensible and detailed form, stating the information that is useful for identifying the defect. The description of the defect shall be in such detail that it can be precisely determined and reproduced by B1.</p>
<p>User further acknowledges that B1 is not responsible for the availability of external websites and services and that B1 does not endorse any services, products or other materials on or available from or through external websites and providers.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<div>
    <ol>
        <li>Final Provisions</li>
    </ol>
</div>
<p>Data storage and data protection</p>
<p>User data is stored by B1 until an order has been processed in full (including for the purpose of processing user inquiries about the order), after which it is archived for storage in accordance with tax and commercial law.</p>
<p>The processing of personal data is governed by B1&apos;s privacy policy, which users can access in their user account.</p>
<p>Changes to these Terms of Use</p>
<p>B1 reserves the right to change the Terms of Use. Changes to these Terms of Use will be offered to the user via the user account. These changes only become effective if the user accepts them.</p>
<p>The user can view the current version of the Terms of Use in Sportworld at any time.</p>
<p>Out-of-court dispute resolution</p>
<p>B1 does not participate in dispute resolution proceedings before a consumer arbitration board and has no obligation to do so.</p>
<p>B1 will, however, endeavour to find an amicable solution in the event of disagreements with users. The user can contact the Sportworld customer service at any time to clarify any questions.</p>
<p>Final agreements</p>
<p>The contractual relationship is governed by the law of the Federal Republic of Germany to the exclusion of the UN Convention on Contracts for the International Sale of Goods, to the extent that the law of the country in which the content or services are offered to the user is not applicable due to applicable mandatory law. The mandatory consumer protection provisions that are applicable in the country in which the user has his or her habitual residence and has booked a subscription are also applicable, as far as these provide the user with more extensive protection.</p>
<p>In the event that the user does not have his or her headquarters or place of residence in the Federal Republic of Germany and if no place of residence in the Federal Republic of Germany is known, the respective headquarter of B1 shall be the exclusive place of jurisdiction. In all other respects, the statutory places of jurisdiction are applicable. This jurisdiction agreement is not applicable if an exclusive jurisdiction is established by law.&nbsp;</p>
<p>Last Updated: September 08, 2023</p>""",
        }
    ],
    "url": "https://sportworld.tv/agb",
}


# Function to make network request with bearer token
# TODO: print results in csv, etc as for channels
def make_network_request(data, url):
    print("URL = " + url)
    response = requests.put(url, headers=header, json=data)

    # Perform any necessary processing on response
    # ...

    return response


# Setup dict for network requests based on env
dataDict = [
    [
        # IMPORTANT: Change appconfig for different bundle regions!
        appconfig_prod_international if ENV == "prod" else appconfig_dev,
        PROD_PATH if ENV == "prod" else DEV_PATH,
    ],
    [
        legal_privacy,
        PROD_PATH_LEGAL_PRIVACY if ENV == "prod" else DEV_PATH_LEGAL_PRIVACY,
    ],
    [
        legal_imprint,
        PROD_PATH_LEGAL_IMPRINT if ENV == "prod" else DEV_PATH_LEGAL_IMPRINT,
    ],
    [legal_terms_mp2, PROD_PATH_LEGAL_TERMS if ENV == "prod" else DEV_PATH_LEGAL_TERMS],
]

# Iterate over each JSON value and make network request
for id in id_list_mp2:
    print("Process for {0}".format(id))
    for data, url in dataDict:
        response = make_network_request(data, url=url.format(regionId=id))
        try:
            print(
                "Response for item: {0}".format(id) + response.json()
            )  # Print response JSON (optional)
        except:
            print("Cannot parse body for item: {0}".format(id))
        print(
            str(response.status_code) + " | Response for item: {0}".format(id)
        )  # Print response status code (optional)
