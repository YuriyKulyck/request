import requests
import json
import random

valcode = input("Value type:")
date = input("Data archive object:")

a = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode}&date={date}&json")

if a.status_code == 200:
    data = json.loads(a.text)
    print(data[0]["txt"], data[0]["rate"])