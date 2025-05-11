"""
    JSON-file handlings

"""
import json

# haetaan tiedot JSON-tiedostosta (joka on kopio)
def get_data_from_json_file(json_file):
    values_list = []
    try:
        # avaa JSON/tiedosto
        with open(json_file) as json_file:
            data = json.load(json_file)

        if data != []:
            # hae otsikot
            headers = list(data[0].keys())

            # hae tiedot
            for value in data:
                values_list.append(value.values())
        else:
            headers = ['no headers']
            values_list = ['no data']

        return headers, values_list
    except FileNotFoundError:
        print("JSON-file not found")
    except AttributeError:
        print("NoneType")

def getJSON(json_file):
    try:
        with open(json_file) as json_file:
            data = json.load(json_file)
            return data

    except FileNotFoundError:
        print("JSON-file not found")