import streamlit as st


class DashboardView:
    @staticmethod
    def zeige_dashboard(student, studiengang, aktueller_gpa, modul_fortschritt, zeit_fortschritt):
        st.set_page_config(page_title="Cybersecurity Study Dashboard", layout="wide")

        st.title("Cybersecurity Study Dashboard")

        st.subheader("Student Information")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Student", student.name)

        with col2:
            st.metric("Aktuelles Semester", student.aktuelles_semester)

        with col3:
            st.metric("Ziel-GPA", student.ziel_gpa)

        st.subheader("GPA Übersicht")

        st.metric("Aktueller GPA", aktueller_gpa)

        if aktueller_gpa <= student.ziel_gpa:
            st.success("Das GPA-Ziel wurde erreicht.")
        else:
            st.warning("Das GPA-Ziel wurde noch nicht erreicht.")

        st.subheader("Modulfortschritt")

        st.progress(modul_fortschritt / 100)
        st.write(f"{modul_fortschritt}% der Module wurden abgeschlossen.")

        st.subheader("Zeitfortschritt")

        st.progress(zeit_fortschritt / 100)
        st.write(f"{zeit_fortschritt}% der geplanten Studiendauer wurden erreicht.")

        st.subheader("Studiengang")

        st.write(f"Studiengang: {studiengang.name}")
        st.write(f"Geplante Semester: {studiengang.geplante_semester}")
        st.write(f"Gesamtanzahl Module: {studiengang.gesamt_module}")

        st.subheader("Abgeschlossene Module")

        for belegung in student.belegungen:
            st.write(
                f"{belegung.modul.name} | ECTS: {belegung.modul.ects} | "
                f"Note: {belegung.note} | Status: {belegung.status.value}"
            )