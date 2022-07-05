import streamlit as st

st.set_page_config(
    page_title="Evaluation",
    page_icon="👍",
)

st.header("👍 - 15.06.22 - Evaluation")
st.write("""Für die Evaluation haben wir ein paar Beispiele, um zu veranschaulichen, wie viel besser das Programm mit zunehmenden Training wird.""")
st.write("""Zwischenzeitlich hatten wir noch mit ein paar Bugs zu kämpfen, zum Beispiel wurden uns immer die maximale Anzahl an Wörter in der Caption ausgegeben, anstatt eine Sinnvolle Caption. So ist zum Beispiel dieser Wörtersalat entstanden:    
         """)
st.image("Trainingsbilder/brokencaption.jpg")

st.write("Ab und an war jedoch auch eine ziemlich lustige Vorhersage dabei:")
st.image("Trainingsbilder/brown_cow.jpg")
