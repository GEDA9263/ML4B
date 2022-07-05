import streamlit as st

st.set_page_config(
    page_title="Data Understanding",
    page_icon="💡",
)

st.header("💡 - 04.05.22 - CRISP-DM Data Understanding")

st.markdown(
      """
      In der zweiten Woche haben wir uns näher mit unserem Datensatz auseinandergesetzt und uns genauer überlegt, was wir mit unserem Projekt eigentlich machen möchten.
      Zunächst haben wir hierfür Ideen gesammelt. Unsere ersten Ideen beinhalteten:
      - Pilze
      - Sitzgelegenheiten
      - Zootiere
      - Autos, Traktoren und Baufahrzeuge
    
      Letztendlich haben wir uns auf Emergency Vehicles geeinigt.<br>  
          
      Das LAION5B Datenset ist sehr groß, aber mit Hilfe eines Web Programms kann man Teile davon einfach filtern ✂️ (https://rom1504.github.io/clip-retrieval/?back=https%3A%2F%2Fknn5.laion.ai&index=laion5B&useMclip=false) Zudem liegt pro Bild bereits eine Bildunterschrift in verschiedenen Sprachen vor.
      """
)
