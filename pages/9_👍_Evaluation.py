import streamlit as st

st.set_page_config(
    page_title="Evaluation",
    page_icon="👍",
)

st.header("👍 - 15.06.22 - Evaluation")
st.markdown("""Zur Evaluation unserer Modelle haben wir einen Loss Plot erstellt, damit wir den Loss des Modells zum Zeitpunkt des Trainings dokumentieren und auswerten können.

Zwischenzeitlich hatten wir mit Bugs zu kämpfen. Zum Beispiel wurden uns immer die maximale Anzahl an Wörtern, anstatt einer sinnvollen Anzahl, in der Caption ausgegeben. So ist zum Beispiel dieser Wörtersalat entstanden:    
""")

st.image("Trainingsbilder/brokencaption.jpg")

st.write("Ab und an war jedoch auch eine ziemlich lustige Vorhersage dabei:")
st.image("Trainingsbilder/brown_cow.jpg")
