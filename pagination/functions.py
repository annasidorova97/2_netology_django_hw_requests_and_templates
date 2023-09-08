import os
from csv import DictReader


def get_list_of_dicts(csv_file, list_of_dicts=None):
    if list_of_dicts is None:
        list_of_dicts = []
    with open(csv_file, newline='') as csvfile:
        reader = DictReader(csvfile)
        for row in reader:
            list_of_dicts.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    return list_of_dicts


def abs_path_to_file(path: str):
    current_path = os.getcwd()
    full_path = '\\'.join([current_path, path])
    return full_path
