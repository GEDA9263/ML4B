import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
import requests
import os.path


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


df = pd.read_json('DogSubset.json')

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
        theme="light",
        update_mode=GridUpdateMode.MODEL_CHANGED,
        allow_unsafe_jscode=True,
    )

    return selection


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

st.title("Chronologischer Ablauf")

st.subheader("03.05.22 ")

with st.expander("Gruppenaufteilung / Erste Schritte"):
     st.write("""
        In der ersten Woche haben wir mit Streamlit eine kleine erste App gebaut und die Installation der erforderlichen Programme durchgeführt. Es gab kleinere Schwierigkeiten beim Einarbeiten, da viele neue Programme auf einmal benötigt wurden und wir uns zuerst einen Überblick machen mussten, welche welches Programm welche Funktion erfüllt.
     """)


st.subheader("04.05.22 ")

with st.expander("Ersten zwei Phasen des CRISP-DM Data understanding"):
     st.write("""
        In der Zweiten Woche haben wir uns näher mit unserem Datensatz auseinandergesetzt und uns genauer überlegt, was wir mit unserem Projekt eigentlich machen wollen. Zunächst haben wir hierfür Ideen gesammelt und uns dann auf Emergency Vehicles geeinigt. Das Datenset ist zwar sehr groß, aber einfach zu filtern mit Hilfe eines Web Programms (hier einfügen), zudem liegt pro Bild bereits eine Bildunterschrift in verschiedenen Sprachen vor. Als erstes haben wir uns auf die Sprache Englisch festgelegt.
        """)


st.subheader("11.05.22 ")

with st.expander("Related Work"):
     st.write("""
        In dieser Woche haben wir begonnen zu recherchieren. Zunächst hat jeder für sich mit verschiedenen Suchmaschinen recherchiert. Wir haben uns generell  über Machine Learning im Image Captioning Bereich eingelesen, um gezielt nach Emergency Vehicle Erkennungen zu suchen. Tatsächlich waren auch einige relevante Paper dabei, teilweise sogar mit Code.
        """)


st.subheader("18.05.22 ")

with st.expander("Datapreperation"):
     st.write("""
        Zunächst haben wir den Datensatz eingeschränkt. Mit den Suchbegriffen „vehicle“, „emergency vehicle“ und „traffic“ etc. Schnell haben wir gemerkt, dass der Datensatz für unser Thema zu klein ist, um einen Algorithmus sinnvoll zu trainieren. Außerdem hatten wir Schwierigkeiten sinnvolle Bilder zu finden, da beispielsweise viele Spielzeugautos mit in unserem Datensatz waren.
        """)


st.subheader("25.05.22 ")

with st.expander("Austausch und aktueller Stand"):
     st.write("""Nachdem wir unseren aktuellen Stand der Recherche präsentiert haben, haben wir als Feedback bekommen uns nicht ganz so zu beschränken und noch einmal einen Schritt zurück zu gehen. Daraufhin haben wir erneut begonnen zu Recherchieren und sind auf ein Git repository gestoßen, welches vielversprechend aussah. Somit haben wir unser Thema eher in die Richtung des General Purpose Image Captioning Algorithmus verändert. Der neue Datensatz den wir mit diesem Model gefunden haben, hat sogar 4 Captions pro Bild. Zudem hätten wir den alten Datensatz aufwendig an das benötigte Format anpassen müssen.
    """)


st.subheader("01.06.22 ")

with st.expander("Modeling"):
     st.write("""Diese Woche haben wir dafür genutzt, unseren Algorithmus zum Laufen zu bringen. Zunächst hatten wir versucht mit dem alten Datenset zu arbeiten. Was aufgrund des Datenformats nicht funktioniert hat. Zudem nutzen wir drei Modelle: Inception v3 tensorflow Machine Learning und Text vectorasation Sowie ein Imagecaptioning Model. Hier ist viel Zeit und Arbeit reingeflossen, um diese drei Modelle zusammen zum Laufen zu bringen.
    """)


st.subheader("08.06.22 ")

with st.expander("Fragesession"):
     st.write("""Die Fragestunde haben wir genutzt, um abzuklären ob auch unser neuer Datensatz verwendet werden darf. Nachdem wir diesen nutzen dürfen, kam nun der Versuch unser trainiertes Model auf Streamlit zum Laufen zu bringen. Da wir 3 Modelle in Streamlit laufen lassen müssen damit unser Captioning funktioniert, sind wir schnell an die Grenzen von Streamlit gestoßen. Zum einen muss das imagecaptioning model laufen und vorher sind noch zwei Modelle um die Bilder pre Prozessen zu können. Außerdem muss das Dictionary immer neu aufgebaut werden weil es sonst überschrieben wird. Nachdem wir sehr viel Arbeit reingesteckt haben, haben wir einsehen müssen, dass es leider nicht funktioniert, da wir einfach zu große Datenmengen verarbeiten. 
   """)


st.subheader("15.06.22 ")

with st.expander("Evaluation"):
     st.write("""Für die Evaluation haben wir ein paar Beispiele, um zu veranschaulichen, wie viel besser das Programm mit zunehmenden Training wird.
      """)
     
     st.write("""Zwischenzeitlich hatten wir noch mit ein paar Bugs zu kämpfen, zum Beispiel wurden uns immer die maximale Anzahl an Wörter in der Caption ausgegeben, anstatt eine Sinnvolle Caption. So ist zum Beispiel dieser Wörtersalat entstanden:    
     """)

st.image("brokencaption.jpg")

st.subheader("22.06.22 ")

with st.expander("Deployment - Feinschliff der Streamlit App"):
     st.write("""Die letzten Tage vor der Abgabe haben wir nun gebraucht, um die Streamlit app aufzuhübschen.
     """)


st.text("")
st.text("")
st.markdown("***")
st.text("")
st.text("")

st.title("Beispielbilder")


with st.expander("Epochen 10 und 20"):
    col1, col2 = st.columns(2)
with col1:
        
    st.image("10epochen.jpg")

with col2:
         st.image("20epochen.jpg")
         
         
         
with st.expander("Epochen 30 und 40"):
    col1, col2 = st.columns(2)
with col1:
        
    st.image("30epochen.jpg")

with col2:
         st.image("40epochen.jpg")
         
         
         
with st.expander("Epoche 50 und Epoche 60"):
    col1, col2 = st.columns(2)
with col1:
        
    st.image("50epochen.jpg")

with col2:
         st.image("60epochen.jpg")
         
         
with st.expander("Epochen Loss Plot"):
          st.image("epochen.jpg")

