"""
    Logic
"""
import pathlib
import pprint as p
import file_handling as handle

def get_datafiles():
    #return os.listdir("JSON-data")
    return [f for f in pathlib.Path("JSON-data").glob("*.json")]

def nominators():
    values = handle.getJSON("JSON-data/kv2025_nominators.json")
    p.pprint(values["@identity-code"])
    p.pprint(values["@election-type"])
    p.pprint(values["election"]["country-data"]["nominator"][1])

def run():
    print("")
    nominators()