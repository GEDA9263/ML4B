import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
import requests
import os.path

st.set_page_config(
    page_title="Data Preparation",
    page_icon="🍳",
)

option = st.sidebar.selectbox("Wählen Sie bitte das Datenset aus", ('Verkehr', 'Fahrzeuge'))
st.header("🍳 - 18.05.22 - Data Preparation")

st.write(""" 
        In dieser Woche ging es darum, unsere Daten auf- bzw. vorzubereiten.
        """)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Gewünschte Daten")
    st.markdown("""
            - Einsatzfahrzeuge
            - Verkehrsbilder
            - Englische Bildunterschriften            
           """)

with col2:
    st.subheader("Unerwünschte Daten")
    st.markdown("""
            - Tiere
            - Menschen
            - Häuser            
           """)


st.write("""
        Dazu haben wir den Datensatz mit den Suchbegriffen „vehicle“, „emergency vehicle“ und „traffic“ etc eingeschränkt. Schnell haben wir gemerkt, dass der Datensatz für unser Thema zu klein ist, um einen Algorithmus sinnvoll trainieren zu können. Außerdem hatten wir Schwierigkeiten sinnvolle Bilder zu finden, da beispielsweise viele Spielzeugautos mit in unserem Datensatz waren.
       Abschließend ein Einblick in unsere Datensätze:
       """)



def aggrid_interactive_table(df: pd.DataFrame):
    """Creates an st-aggrid interactive table based on a dataframe.
    Args:
        df (pd.DataFrame]): Source dataframe
    Returns:
        dict: The selected row
    """
    options = GridOptionsBuilder.from_dataframe(
        df, enableRowGroup=True, enableValue=True, enablePivot=True
    )

    options.configure_side_bar()

    options.configure_selection("single")
    selection = AgGrid(
        df,
        enable_enterprise_modules=True,
        gridOptions=options.build(),
        theme="dark",
        update_mode=GridUpdateMode.MODEL_CHANGED,
        allow_unsafe_jscode=True,
    )

    return selection

subset = ""
if (option == 'Verkehr'):
        subset = 'trafficSubset.json'
elif(option == 'Fahrzeuge'):
        subset = 'clipsubset.json'

        
if(option != ''):
        df = pd.read_json(subset)
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
