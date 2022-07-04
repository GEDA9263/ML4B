import streamlit as st
import pandas as pd

st.header("18.05.22 - Data Preparation")
st.write("""
        Zunächst haben wir den Datensatz eingeschränkt. Mit den Suchbegriffen „vehicle“, „emergency vehicle“ und „traffic“ etc. Schnell haben wir gemerkt, dass der Datensatz für unser Thema zu klein ist, um einen Algorithmus sinnvoll zu trainieren. Außerdem hatten wir Schwierigkeiten sinnvolle Bilder zu finden, da beispielsweise viele Spielzeugautos mit in unserem Datensatz waren.
        """)

df = pd.read_json('trafficSubset.json')
selection = aggrid_interactive_table(df)

if len(selection["selected_rows"]) > 0:
    st.write("Hier ist das ausgewählte Bild! ")
    url = selection["selected_rows"][0]["url"]
    id = selection["selected_rows"][0]["id"]
    filename = str(id) + '.jpg'
    bool = os.path.exists('pictures/' + filename)
    if not bool:
        r = requests.get(url, allow_redirects=True)
        open("pictures/" + str(id) + '.jpg', "wb").write(r.content)
    st.image('pictures/' + str(id) + '.jpg')
    st.write(selection["selected_rows"][0]["caption"])
