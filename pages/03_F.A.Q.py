import pandas as pd
import streamlit as st

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://i.ibb.co/Fs4gnZX/radio.png);
                background-repeat: no-repeat;
                background-position: center;
                padding-top: 120px;
                background-position: 30px 20px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
add_logo()
heart = 'https://i.ibb.co/9s13bzT/heart.png'
logo = 'https://i.ibb.co/D7fqn7J/logo.png'
st.header('Bienvenue F.A.Q')

st.subheader('Plateforme')
st.write('La plateforme permet de sélectionner des titres de musique en fonction des filtres et d\'une recommandation basée sur un algorithme de proximité')

st.subheader('Fonctionnalité')
st.write('Recherche par filtres de genres et caractéristiques, recherche par similarité du titre, ajout de titre dans une playlist via les boutons "like", suppression des musiques dans la playlist, découverte de musique par une roue aléatoire ')

st.subheader('Home')
st.write('Regroupe le Top 15 des musiques par popularité. Mise en avant du TOP 3')

st.subheader('Playlist')
st.write('Affiche les titres likés par l\'utilisateur, la durée totale de la playlist')

st.subheader('Lucky Sound')
st.write('Permet de découvrir par un système aléatoire une musique')

st.subheader('Options')
st.write('Mise en avant du TOP 3 sur chaque page')
st.write('Dans chaque page, l\'utilisateur peut liker une musique avec le bouton "like" ( rouge). ')
st.write(f"""Dans chaque page, l\'utilisateur peut voir ses musiques likées grâce à l\'icône : <img src="{heart}" width="15px" >""", unsafe_allow_html=True)
st.write("L'application fonctionne ave  un extrait de baase de donéne, il se peut que des element comme les images manquent. Les sons extraits sont proposé via API (mode dev) de spotify, il est possible qu'aprés une utilisation , les extraits ne soient plus accésibles.")

st.subheader('Copyright & Aide')
st.markdown('[Vincent Cornélius](https://www.linkedin.com/in/corneliusvincent/) - [Manuel Musy](https://www.linkedin.com/in/manuel-musy/) - [Mathieu Beauvois](https://www.linkedin.com/in/mathieu-beauvois-121203137/) - [Alexandre Thigé](https://www.linkedin.com/in/athige/) - [Marie Lefebvre](https://www.linkedin.com/in/marie-lefebvre-50654a269/) - [Victoria Gaullier](https://www.linkedin.com/in/victoria-gaullier-4a03b926a/)')
st.write(f"""<p style="text-align:center"><img src="{logo}" max-height="25px" width="150px" ></p>""", unsafe_allow_html=True)
