class Student:
        def __init__(self, name, aktuelles_semester, ziel_gpa):
            self.name = name
            self.aktuelles_semester = aktuelles_semester
            self.ziel_gpa = ziel_gpa
            self.belegungen = []  # Liste von Belegung-Objekten
        def add_belegung(self, belegung):
            self.belegungen.append(belegung)