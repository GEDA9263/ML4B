import streamlit as st

st.set_page_config(
    page_title="Modeling",
    page_icon="🖥️",
)

st.header("🖥️ - 01.06.22 - Modeling")
st.markdown("""
In dieser Woche haben wir angefangen unser Model zu trainieren.
Wir haben uns auf 40.000 Bilder beschränkt, das heißt es waren 200.000 Bildunterschriften. Von diesen 200.000 Datensätzen haben wir 160.000 zum Trainieren genutzt und die restlichen 40.000 zum validieren des Models.

Als erstes haben wir Inception V3 genutzt um die Bilder vorzuverarbeiten. Danach haben wir die Bildunterschriften mithilfe des TextVectorization layers in Integer Sequenzen transformiert. Hierbei haben wir eine maximale Länge von 50 Wörtern pro Catpion gewählt. Außerdem sind nur die 5.000 häufigsten Wörter aller Bildunterschriften zur Erzeugung erlaubt.

Aus den Daten von Inception V3 wird ein Vektor generiert. Dieser durchläuft den CNN Encoder, welcher aus einem single Fully connected layer besteht und wird anschließend durch den Decoder geschickt, um das nächste Wort vorherzusagen.
  """)
