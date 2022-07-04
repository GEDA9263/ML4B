import streamlit as st

st.title("Bilder")
option = st.sidebar.selectbox('Bitte wählen sie die Daten aus', ('Epoche 10', 'Epoche 20', 'Epoche 30', 'Epoche 40', 'Epoche 50', 'Epoche 60', 'Epoche 70', 'Verlustgrafik'))
breite = 720

if(option == 'Epoche 10'):
    st.image("Trainingsbilder/Pferde/Pferde_10_Epochen.jpg", width=breite)
    st.image("Trainingsbilder/Elefanten/10 Epochen Elefant.png", width=breite)        
elif(option == 'Epoche 20'):
    st.image("Trainingsbilder/Pferde/Pferde_20_Epochen.jpg", width=breite)
    st.image("Trainingsbilder/Elefanten/20 Epochen Elefant.png",  width=breite)
elif(option == 'Epoche 30'):
    st.image("Trainingsbilder/Pferde/Pferde_30_Epochen.jpg", width=breite)
    st.image("Trainingsbilder/Elefanten/30 Epochen Elefant.png",  width=breite)
elif(option == 'Epoche 40'):
    st.image("Trainingsbilder/Pferde/Pferde_40_Epochen.jpg", width=breite)
    st.image("Trainingsbilder/Elefanten/40 Epochen Elefant.png",  width=breite0)
elif(option == 'Epoche 50'):
    st.image("Trainingsbilder/Pferde/Pferde_50_Epochen.jpg", width=breite)
    st.image("Trainingsbilder/Elefanten/50 Epochen Elefant.png",  width=breite)
elif(option == 'Epoche 60'):
    st.image("Trainingsbilder/Pferde/Pferde_60_Epochen.jpg", width=breite)
    st.image("Trainingsbilder/Elefanten/60 Epochen Elefant.png",  width=breite)
elif(option == 'Epoche 70'):
    st.image("Trainingsbilder/Elefanten/70 Epochen Elefant.png",  width=breite)
elif(option == 'Verlustgrafik'):
     st.image("Trainingsbilder/Pferde/Pferde_Loss_Plot.jpg", caption= 'Verlustgrafik der Pferde', width=int((breite/2)))
     st.image("Trainingsbilder/Elefanten/Verlustdiagramm 70 Epochen.png", caption = 'Verlustgrafik der Elefanten', width=int((breite/2)))
