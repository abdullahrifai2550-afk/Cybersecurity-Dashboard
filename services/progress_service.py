class ProgressService:
    @staticmethod
    def berechne_modul_fortschritt(abgeschlossene_module, gesamt_module):
        if gesamt_module == 0:
            return 0
        return round((abgeschlossene_module / gesamt_module) * 100, 2)
    @staticmethod
    def berechne_zeit_fortschritt(aktuelles_semester, geplante_semester):
        if geplante_semester == 0:
            return 0
        return round((aktuelles_semester / geplante_semester) * 100, 2)