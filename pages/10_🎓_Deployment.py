import streamlit as st

st.set_page_config(
    page_title="Deployment",
    page_icon="🎓",
)

st.header("22.06.22 - Deployment")
st.markdown("""Die letzten Tage vor der Abgabe haben wir gebraucht, um die Streamlit app aufzuhübschen. Einige der Änderungen waren z.B.:
            - Umstellung der App von Single auf Multipage 
            - Einbinden der selbst erzeugten Datensätze und Zugriff auf die Bilder
            - Ein kleiner Ausschnitt aus dem MS COCO Datenset
            - Einbinden von Ergebnissen während des Trainings
            - Implementierung der Funktion ein Bild zu untertiteln
            
            Im Reiter Testing kann man ein eigenes Bild einem Modell, welches auf 200.000 Datenpunkten trainiert wurde übergeben und sich eine Bildunterschrift generieren lassen.
            Leider funktionieren die entsprechenden Python Packages nicht sonderlich gut mit Streamlit, weswegen man alle 5-6 Bilder den Cache einmal clearen sollte
            um einen Absturz der App vorzubeugen. 
            Außerdem funktoniert das untertiteln der Bilder signifikant besser, wenn nicht viele Sachen auf dem Bild zu sehen sind. Im Zweifelsfall kann es zu sehr langen und 
            ungenauen Captions kommen, da das Modell die schiere Menge an Features schlecht verarbeiten kann. Beispiele für gute Bilder sind im Reiter Feedback zu sehen.
           
   
   
   """)
