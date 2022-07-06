import streamlit as st

st.set_page_config(
    page_title="Fragesession",
    page_icon="❔",
)

st.header("❔ - 08.06.22 - Fragesession")
st.markdown("""Die Fragestunde haben wir genutzt, um abzuklären ob auch unser neuer Datensatz verwendet werden darf. Nachdem wir diesen nutzen dürfen, kam nun der Versuch unser trainiertes Model auf Streamlit zum Laufen zu bringen. 
Wir mussten Inception V3, Encoder und Decoder zum laufen bringen und man musste jedes mal das Dictionary neu erzeugen lassen damit unser Captioning funktioniert. Dadurch sind wir schnell an die Grenzen von Streamlit gestoßen. 
Nachdem wir sehr viel Arbeit reingesteckt haben, haben wir einsehen müssen, dass es vorerst nicht funktioniert, da wir einfach zu große Datenmengen verarbeiten. 
   """)
