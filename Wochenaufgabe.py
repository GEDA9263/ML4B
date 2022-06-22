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
st.write('Als Datenset wird zum trainieren und testen das LAION5B Datenset verwenden, welches eine Sammlung von 6 Milliarden Bildern und 240 TB an Größe darstellt.  \n'
         'In der nachfolgenden Tabelle ist ein Ausschnitt aus einem Subset dargestellt, welchen man benutzen kann um die entsprechenden Bilder mithilfe der URL zu downloaden.  \n'
         'Hierzu einfach eine beliebige Zeile selektieren, das ausgewählte Bild wird anschließend angezeigt.')


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

st.subheader("03.05.22 Gruppenaufteilung / Erste Schritte")

with st.expander("See more"):
     st.write("""
        In der ersten Woche haben wir mit Streamlit eine kleine erste App gebaut und die Installation der erforderlichen Programme durchgeführt. Es gab kleinere Schwierigkeiten beim Einarbeiten, da viele neue Programme auf einmal benötigt wurden und wir uns zuerst einen Überblick machen mussten, welche welches Programm welche Funktion erfüllt.
     """)


st.subheader("04.05.22 Ersten zwei Phasen des CRISP-DM Data understanding")

with st.expander("See more"):
     st.write("""
        In der Zweiten Woche haben wir uns näher mit unserem Datensatz auseinandergesetzt und uns genauer überlegt, was wir mit unserem Projekt eigentlich machen wollen. Zunächst haben wir hierfür Ideen gesammelt und uns dann auf Emergency Vehicles geeinigt. Das Datenset ist zwar sehr groß, aber einfach zu filtern mit Hilfe eines Web Programms (hier einfügen), zudem liegt pro Bild bereits eine Bildunterschrift in verschiedenen Sprachen vor. Als erstes haben wir uns auf die Sprache Englisch festgelegt.
        """)


st.subheader("11.05.22 Related Work")

with st.expander("See more"):
     st.write("""
        In dieser Woche haben wir begonnen zu recherchieren. Zunächst jeder für sich, mit verschiedenen Suchmaschinen geschaut was man findet. Als erstes hat jeder sich generell eingelesen über Machine Learning im Image Captioning Bereich um dann gezielt nach Emergency Vehicle Erkennung zu suchen. Tatsächlich waren auch einige relevante Paper dabei, teilweise sogar mit Code.
        """)


st.subheader("18.05.22 Datapreperation")

with st.expander("See more"):
     st.write("""
        Zunächst haben wir den Datensatz eingeschränkt. Mit den Suchbegriffen „vehicle“ „emergency vehicle“ „traffic“ etc. Schnell haben wir gemerkt, dass für unser Thema der Datensatz zu klein ist, um ein Algorithmus sinnvoll zu trainieren. Außerdem hatten wir Schwierigkeiten mit Sinnvollen Bildern, da zum Beispiel viele Spielzeugautos mit in unserem Datensatz waren.
        """)


st.subheader("25.05.22 Austausch und aktueller Stand")

with st.expander("See more"):
     st.write("""Nachdem wir unseren aktuellen Stand der Recherche präsentiert haben, haben wir als Feedback bekommen uns nicht ganz so zu beschränken und noch einmal einen Schritt zurück zu gehen. Daraufhin haben wir noch einmal begonnen zu Recherchieren und sind auf ein Git repository gestoßen, das vielversprechend aussah. Somit haben wir unser Thema mehr hin zu einem General Purpose Image Captioning Algorithmus verändert. Der neue Datensatz, den wir mit diesem Model gefunden haben, hat sogar 4 Captions pro Bild. Zudem hätten wir den alten Datensatz aufwendig an das benötigte Format anpassen müssen.
    """)


st.subheader("01.06.22 Modeling")

with st.expander("See more"):
     st.write("""Diese Woche haben wir dafür genutzt unseren Algorithmus zum Laufen zubringen. Zunächst hatten wir versucht mit den alten Datenset zuarbeiten. Was aufgrund des Datenformats nicht funktioniert hat. Zudem nutzen wir drei Modelle: Inception v3 tensorflow Manchine Learning und Text vectorasation Sowie ein Imagecaptioning Model. Hier ist viel Arbeit reingeflossen, um diese drei Modelle zusammen zum Laufen zu bringen.
    """)


st.subheader("08.06.22 Fragesession")

with st.expander("See more"):
     st.write("""Die Fragestunde haben wir genutzt, um abzuklären ob auch unser neuer Datensatz verwendet werden darf. Nach dem wir diesen nutzen dürfen, kam nun der Versuch unser trainiertes Model auf Streamlit zum Laufen zu bringen. Da wir 3 Modelle in Streamlit Laufen lassen müssen, damit unser Captioning funktioniert, sind wir schnell an die Grenzen von Streamlit gestoßen. Zum einen muss das imagecaptioning model  laufen und vorher sind noch zwei Modelle um die Bilder pre Prozessen zu können. Außerdem muss das Dictionary immer neu aufgebaut werden weil es sonst überschrieben wird. Nach dem wir sehr viel Arbeit reingesteckt haben, haben wir irgendwann einsehen müssen, dass es leider nicht Funktioniert, da wir einfach zu große Datenmengen verarbeiten. 
   """)


st.subheader("15.06.22 Evaluation")

with st.expander("See more"):
     st.write("""Für die Evaluation haben wir ein paar Beispiele, um zu veranschaulichen, wie viel besser das Programm mit zunehmenden Training wird.
      """)
     
     st.write("""Zwischenzeitlich hatten wir noch mit einen paar Bugs zu kämpfen zum Beispiel wurden uns immer die maximale Anzahl an Wörter in der Caption ausgegeben, anstatt eine Sinnvolle Caption. So ist zum Beispiel dieser Wörtersalat entstanden:    
     """)

st.image("brokencaption.jpg")

st.subheader("22.06.22 Deployment - Feinschliff der Streamlit App")

with st.expander("See more"):
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
        
    st.image("10epochen.jpg")

with col2:
         st.image("20epochen.jpg")
         
         
         
with st.expander("Epoche 50 und LossPlot"):
    col1, col2 = st.columns(2)
with col1:
        
    st.image("10epochen.jpg")

with col2:
         st.image("20epochen.jpg")
         
         

