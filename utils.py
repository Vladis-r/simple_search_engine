import csv
import json


def cvs_into_json(path_to_csv, path_to_json):
    with open(path_to_csv, encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)

    with open(path_to_json, "w", encoding='utf-8') as json_file:
        json.dump(rows, json_file, ensure_ascii=False)
