import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
import requests
import os.path


st.set_page_config(
    page_title="Projektpräsentation",
    page_icon="📽️",
)

st.title('Projektpräsentation')
st.subheader('Teamvorstellung')

st.write('Wir sind Gruppe 11 und bestehen aus Jorgo, Debora und Daniel. Wir alle studieren Wirtschaftsinformatik im 4. Semester.')

st.subheader('Projektvorstellung')
st.write('Wir haben uns als Projekt für Image Captioning entschieden.  \n' 
         'Das heißt, es soll ein Modell trainiert werden, welches in der Lage ist eine Bildunterschrift für Bilder einer spezifischen Domäne, also innerhalb eines spezifischen Bereiches, zu erzeugen.')

st.subheader('Datenset')
st.write('Ursprünglich wurde uns das LAION5B Datenset als Trainingsdatenset zur Verfügung gestellt. Im Laufe des Semesters haben wir uns jedoch gegen dieses Datenset entschieden. \n'
         'Als Datenset zum trainieren und testen verwenden wir das MicrosoftCoco 2014 train/validation split Datenset, welches eine Sammlung von 82 Tausend Bildern und 13 GB an dazugehörigen Daten darstellt.  \n'
         'Um Bildunterschriften für unseren Show-Case zu generieren, selektieren Sie bitte eine beliebige Zeile, das ausgewählte Bild wird anschließend mit der automatisch generierter Bildunterschrift, sowie der originalen Bildunterschrift angezeigt.')


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


df = pd.read_json('Subsets/DogSubset.json')

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

         
st.text("")
st.text("")
st.markdown("***")
st.text("")
st.text("")


