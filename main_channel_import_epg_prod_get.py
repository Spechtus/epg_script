from pathlib import Path
import os
import requests
import json
import csv

# Ein Script um alle Channels im Google Sheet von Metaprofile mit den aktuellen Channels abzugleichen
# 1.: Einfach alle Inhalte in ein neues Sheet kopieren und als csv mit dem Namen "channels.csv" downloaden
#     IMPORTANT: Im Google Sheets sind auf Zeile und Spalte 1 kein Content, diese weglöschen, falls man mit STRG+A kopiert hat!
# 2.: Die Liste dann einfach in das directory "epg_script" kopieren und das script "main_channel_import_epg_prod_post.py" ausführen

# Set path to working directory, as we use relative paths
new_path = Path(__file__).parent
os.chdir(new_path)

# Load token into file
with open("secret/sportworldAPI_key_prod.txt",
          encoding="UTF-8") as bearer_token:
    sportworld_API_token = bearer_token.read()

# Define header, URL and query
header = {
    "Authorization": "Bearer " + sportworld_API_token,
    "Content-Type": "application/json",
}

# Get regions
response_regions = requests.get(
    "https://sportworld.api.b1smarttv.com/v3/console/regions?limit=200",
    headers=header,
    timeout=10,
)
REGIONS = json.loads(response_regions.text)
print(REGIONS)

# channel_name --> row[1]
# county code of availavility --> row[6]
# channel_id --> row[14]


def build_json_for_update(channel_name: str,
                          channel_country_codes_of_availability: str,
                          channel_id: str) -> dict:
    update_json = {
        "id": "",
        "enabled": True,
        "name": [],
        "epgId": "",
        "epgType": "TvProfil",
        "regionIds": "",
        "accessRightIds": [],
        "watchable": True,
        "public": True,
    }

    name_dict = {"value": "", "locales": ["de-DE", "en-US"]}

    regions_list = []

    country_code_list = channel_country_codes_of_availability.split(",")

    # Add regions ids to regions_list
    for country in country_code_list:
        for region in REGIONS["items"]:
            if country in region["countryCodes"]:
                regions_list.append(region["id"])

    update_json["id"] = "sw$" + channel_id
    update_json["epgId"] = channel_id
    update_json["regionIds"] = regions_list

    name_dict["value"] = channel_name

    update_json["name"].append(name_dict)

    return update_json


def get_json(json_file, csv_writer, csv_row):
    response_channels = requests.get(
        "https://sportworld.api.b1smarttv.com/v3/console/channels/" +
        json_file["id"],
        headers=header,
        timeout=10,
    )
    if response_channels.status_code == 200:
        print(
            str(response_channels.status_code) + " | Channel " +
            response_channels.json()["id"].split("$")[1] +
            " integrated into Sportworld!")
        csv_writer.writerow({
            "channel_name":
            csv_row[1],
            "channel_id":
            csv_row[14],
            "country_code":
            csv_row[6],
            "in_SW":
            "Yes(" + str(response_channels.status_code) + ")",
        })
    elif response_channels.status_code == 404:
        print(
            str(response_channels.status_code) + " | Channel " +
            json_file["id"].split("$")[1] + " not yet in Sportworld!")
        csv_writer.writerow({
            "channel_name":
            csv_row[1],
            "channel_id":
            csv_row[14],
            "country_code":
            csv_row[6],
            "in_SW":
            "No(" + str(response_channels.status_code) + ")",
        })
    else:
        print(response_channels.status_code + " | Channel " +
              json_file["id"].split("$")[1])
        csv_writer.writerow({
            "channel_name":
            csv_row[1],
            "channel_id":
            csv_row[14],
            "country_code":
            csv_row[6],
            "in_SW":
            "No(" + str(response_channels.status_code) + ")",
        })


if __name__ == "__main__":
    # load csv with open channels
    with open("channels.csv") as csv_reader_file:
        with open("output-exists.csv", "w", newline="") as csv_writer_file:
            fieldnames = [
                "channel_name", "channel_id", "country_code", "in_SW"
            ]
            csv_writer = csv.DictWriter(csv_writer_file, fieldnames=fieldnames)
            csv_reader = csv.reader(csv_reader_file, delimiter=",")

            csv_writer.writeheader()

            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    print("Row#: ", line_count)
                    print("Channel name: ", row[1])
                    print("County codes of availavility: ", row[6])
                    print("Channel ID: ", row[14])

                    # Build the json for the post
                    json_to_post_to_sportworld = build_json_for_update(
                        row[1], row[6], row[14])

                    # Post json to sportworld backend
                    get_json(json_to_post_to_sportworld, csv_writer, row)
                    print()

                    line_count += 1
