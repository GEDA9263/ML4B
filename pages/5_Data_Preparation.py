import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
import requests
import os.path

option = st.selectbox("Wählen Sie bitte das Datenset aus", ('Verkehr', 'Notfallfahrzeuge', 'Random'))
st.header("18.05.22 - Data Preparation")
st.write("""
        Zunächst haben wir den Datensatz eingeschränkt. Mit den Suchbegriffen „vehicle“, „emergency vehicle“ und „traffic“ etc. Schnell haben wir gemerkt, dass der Datensatz für unser Thema zu klein ist, um einen Algorithmus sinnvoll zu trainieren. Außerdem hatten wir Schwierigkeiten sinnvolle Bilder zu finden, da beispielsweise viele Spielzeugautos mit in unserem Datensatz waren.
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
elif(option == 'Notfallfahrzeuge'):
        subset = 'emergencyVehicleSubset.json'
elif(option == 'Random'):
        subset = 'clipsubset.json.json'

        
if(optin != ''):
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
