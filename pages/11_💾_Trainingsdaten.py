import streamlit as st

st.title("Bilder")
option = st.sidebar.selectbox('Bitte wählen sie die Daten aus', ('Epoche 10', 'Epoche 20'))

if(option == 'Epoche 10'):
    col1, col2 = st.columns(2)
    with col1:
        st.image("Trainingsbilder/Pferde/Pferde_10_Epochen.jpg", width=720)
    with col2:
        st.image("Trainingsbilder/Elefanten/10 Epochen Elefant.png", width=720)
        
        
with st.expander("Epoche 10"):
    col1, col2 = st.columns(2)
with col1:    
    st.image("Trainingsbilder/Pferde/Pferde_10_Epochen.jpg")
with col2:
    st.image("Trainingsbilder/Elefanten/10 Epochen Elefant.png")
         
          
with st.expander("Epoche 20"):
    col1, col2 = st.columns(2)
with col1:    
    st.image("Trainingsbilder/Pferde/Pferde_20_Epochen.jpg")
with col2:
    st.image("Trainingsbilder/Elefanten/30 Epochen Elefant.png")
         
             
with st.expander("Epoche 30"):
    col1, col2 = st.columns(2)
with col1:    
    st.image("Trainingsbilder/Pferde/Pferde_30_Epochen.jpg")
with col2:
    st.image("Trainingsbilder/Elefanten/30 Epochen Elefant.png")


with st.expander("Epoche 40"):
    col1, col2 = st.columns(2)
with col1:    
    st.image("Trainingsbilder/Pferde/Pferde_40_Epochen.jpg")
with col2:
    st.image("Trainingsbilder/Elefanten/40 Epochen Elefant.png")


with st.expander("Epoche 50"):
    col1, col2 = st.columns(2)
with col1:    
    st.image("Trainingsbilder/Pferde/Pferde_50_Epochen.jpg")
with col2:
    st.image("Trainingsbilder/Elefanten/50 Epochen Elefant.png")

with st.expander("Epoche 60 & 70"):
    col1, col2 = st.columns(2)
with col1:    
    st.image("Trainingsbilder/Pferde/Pferde_60_Epochen.jpg")
with col2:
    st.image("Trainingsbilder/Elefanten/60 Epochen Elefant.png")
    st.image("Trainingsbilder/Elefanten/70 Epochen Elefant.png")
         
         
with st.expander("Epochen Loss Plot"):
          st.image("Trainingsbilder/Pferde/Pferde_Loss_Plot.jpg")
