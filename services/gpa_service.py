class GpaService:
    @staticmethod
    def berechne_gpa(belegungen):
        bestandene_belegungen = []

        for belegung in belegungen:
            if belegung.note is not None:
                bestandene_belegungen.append(belegung)

        if len(bestandene_belegungen) == 0:
            return 0.0

        gesamt_note = 0

        for belegung in bestandene_belegungen:
            gesamt_note += belegung.note

        return round(gesamt_note / len(bestandene_belegungen), 2)