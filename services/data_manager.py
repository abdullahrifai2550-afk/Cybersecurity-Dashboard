import json


class DataManager:
    @staticmethod
    def lade_daten(dateipfad):
        try:
            with open(dateipfad, "r", encoding="utf-8") as datei:
                return json.load(datei)
        except FileNotFoundError:
            return {}

    @staticmethod
    def speichere_daten(dateipfad, daten):
        with open(dateipfad, "w", encoding="utf-8") as datei:
            json.dump(daten, datei, indent=4)