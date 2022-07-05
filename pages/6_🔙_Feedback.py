import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Feedback",
    page_icon="🔙",
)

st.header("🔙 - 25.05.22 - Feedback")
st.markdown("""Nachdem wir unseren aktuellen Stand der Recherche präsentiert haben, haben wir als Feedback bekommen uns nicht ganz so zu beschränken und noch einmal einen Schritt zurück zu gehen. Daraufhin haben wir erneut begonnen zu Recherchieren und sind auf ein Git repository gestoßen, welches vielversprechend aussah. Somit haben wir unser Thema eher in die Richtung des General Purpose Image Captioning Algorithmus verändert. 

Der neue Datensatz Microsoft Coco den wir mit diesem Model gefunden haben, hat den großen Vorteil, dass dieser 5 Captions pro Bild hat. Jeder dieser Captions wurde von einem Menschen verfasst. Die Qualität des verwendeten Datensatzes war viel besser, deshalb entschlossen wir uns, diesen auch zu benutzen.
   
   Hier ein kleiner Ausschnitt aus dem Datenset: 
   """)

images = ['https://farm4.staticflickr.com/3210/3016304198_977b66924f_z.jpg',
          'https://farm3.staticflickr.com/2009/2456971230_5db8094526_z.jpg',
          'https://farm4.staticflickr.com/3060/2971251148_d241e54ae2_z.jpg'
         ]

images2 = ['https://farm3.staticflickr.com/2191/2187671374_8195774f3b_z.jpg',
           'https://farm9.staticflickr.com/8522/8581450876_b7bca30450_z.jpg',
           'https://farm6.staticflickr.com/5490/9187151684_5f54e2fa26_z.jpg'
          ]

images3 = ['https://farm3.staticflickr.com/2224/2483765539_4babc436c5_z.jpg',
           'https://farm6.staticflickr.com/5522/9294690250_f1d3924b7f_z.jpg',
           'https://farm4.staticflickr.com/3396/3447807165_e5052e9d4d_z.jpg'
          ]

captions = ['a man braiding the mane of a horse',
            'a group of vehicles passing through an intersection',
            'a seaplane lands in a bay where a cruise ship is docked',
           ]

captions2 = ['a group of snowboarders posing for a photograph',
             'a meal on a paper plate set on a wood table.',
             'the white bus is going down the quiet city street.'
            ]

captions3 = ['an old fire hydrant with some graffiti on it',
            'a baseball player on the field warming up with his bat.',
             'a man in a field who is flying a kite.'
             ]
col1, col2, col3 = st.columns(3)
with col1:
    st.image(images, captions)
with col2:
    st.image(images2, captions2)
with col3:
    st.image(images3, captions3)
