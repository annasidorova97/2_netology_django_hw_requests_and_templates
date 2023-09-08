from csv import DictReader


def get_list_of_dicts(csv_file, list_of_dicts=None):
    if list_of_dicts is None:
        list_of_dicts = []
    with open(csv_file, newline='') as csvfile:
        reader = DictReader(csvfile)
        for row in reader:
            list_of_dicts.append({row['Name'], row['Street'], row['District']})
    return list_of_dicts
