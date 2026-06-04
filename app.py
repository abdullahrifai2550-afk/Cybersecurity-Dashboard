from models.student import Student
from models.studiengang import Studiengang
from models.modul import Modul
from models.belegung import Belegung
from models.modul_status import ModulStatus

from services.gpa_service import GpaService
from services.progress_service import ProgressService
from services.data_manager import DataManager

from views.dashboard_view import DashboardView


daten = DataManager.lade_daten("data/student_data.json")

student = Student(
    daten["name"],
    daten["aktuelles_semester"],
    daten["ziel_gpa"]
)

studiengang = Studiengang(
    "Cybersecurity",
    daten["geplante_semester"],
    daten["gesamt_module"]
)

module = [
    Belegung(Modul("Python", 5), 4.0, "26.04.2026", ModulStatus.BESTANDEN),
    Belegung(Modul("Datenschutz und IT-Sicherheit", 5), 4.0, "12.02.2026", ModulStatus.BESTANDEN),
    Belegung(Modul("Betriebssysteme und Rechnernetze", 5), 2.7, "27.03.2026", ModulStatus.BESTANDEN),
    Belegung(Modul("Wissenschaftliches Arbeiten", 5), 2.7, "12.02.2026", ModulStatus.BESTANDEN)
]

for belegung in module:
    student.add_belegung(belegung)

aktueller_gpa = GpaService.berechne_gpa(student.belegungen)

modul_fortschritt = ProgressService.berechne_modul_fortschritt(
    daten["abgeschlossene_module"],
    daten["gesamt_module"]
)

zeit_fortschritt = ProgressService.berechne_zeit_fortschritt(
    daten["aktuelles_semester"],
    daten["geplante_semester"]
)

DashboardView.zeige_dashboard(
    student,
    studiengang,
    aktueller_gpa,
    modul_fortschritt,
    zeit_fortschritt
)