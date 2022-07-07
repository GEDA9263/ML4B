import streamlit as st

st.set_page_config(
    page_title="Trainingsbilder",
    page_icon="💾",
)

st.title("💾 - Trainingsbilder")
option = st.sidebar.selectbox('Bitte wählen sie die Epoche aus zu der Sie die Daten sehen möchten', ('Rohbilder','Epoche 10', 'Epoche 20', 'Epoche 30', 'Epoche 40', 'Epoche 50', 'Epoche 60', 'Epoche 70'))
breite = 720

if(option == 'Rohbilder'):
    st.image("Trainingsbilder/Pferde/Pferde.jpg", caption= 'two horses walking down a path beside a fence', width=breite)
    st.image("Trainingsbilder/Elefanten/Elefanten.jpg", caption='a baby elephant walking next to a large elephant', width=breite)       
    st.image("Trainingsbilder/Human/Humans.jpg", caption='a lot of people around and under a tent in a city', width=breite)        
elif(option == 'Epoche 10'):
    st.image("Trainingsbilder/Pferde/Pferde_10_Epochen.jpg", width=breite)
    st.image("Trainingsbilder/Elefanten/10 Epochen Elefant.png", width=breite)
    st.image("Trainingsbilder/Human/Human 10 Epochen.jpg", width=breite)        
elif(option == 'Epoche 20'):
    st.image("Trainingsbilder/Pferde/Pferde_20_Epochen.jpg", width=breite)
    st.image("Trainingsbilder/Elefanten/20 Epochen Elefant.png",  width=breite)
    st.image("Trainingsbilder/Human/Human 20 Epochen.jpg", width=breite)        
elif(option == 'Epoche 30'):
    st.image("Trainingsbilder/Pferde/Pferde_30_Epochen.jpg", width=breite)
    st.image("Trainingsbilder/Elefanten/30 Epochen Elefant.png",  width=breite)
    st.image("Trainingsbilder/Human/Human 30 Epochen.jpg", width=breite)        
elif(option == 'Epoche 40'):
    st.image("Trainingsbilder/Pferde/Pferde_40_Epochen.jpg", width=breite)
    st.image("Trainingsbilder/Elefanten/40 Epochen Elefant.png",  width=breite)
    st.image("Trainingsbilder/Human/Human 40 Epochen.jpg", width=breite)        
elif(option == 'Epoche 50'):
    st.image("Trainingsbilder/Pferde/Pferde_50_Epochen.jpg", width=breite)
    st.image("Trainingsbilder/Elefanten/50 Epochen Elefant.png",  width=breite)
    st.image("Trainingsbilder/Human/Human 50 Epochen.jpg", width=breite)        
elif(option == 'Epoche 60'):
    st.image("Trainingsbilder/Pferde/Pferde_60_Epochen.jpg", width=breite)
    st.image("Trainingsbilder/Elefanten/60 Epochen Elefant.png",  width=breite)
    st.image("Trainingsbilder/Human/Human 60 Epochen.jpg", width=breite)        
elif(option == 'Epoche 70'):
    st.image("Trainingsbilder/Elefanten/70 Epochen Elefant.png",  width=breite)
    st.image("Trainingsbilder/Human/Human 70 Epochen.jpg", width=breite)        
