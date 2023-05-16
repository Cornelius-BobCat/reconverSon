import streamlit as st
import pandas as pd
from PIL import Image
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import sqlite3
import math


# DEFINE CONST
curl = 'https://open.spotify.com/track/'
heart = 'img/heart.png'
cover_false = 'https://i.ibb.co/ZWSPvxB/nf.png'
radio_ets = 'img/radio.png'
check = 'https://i.ibb.co/thyXK5c/check.png'

# INIT FONCTION 
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

def raccourcir_chaine(chaine, nb_caracteres_max=30):
    if len(chaine) <= nb_caracteres_max:
        return chaine
    else:
        raccourci = chaine[:nb_caracteres_max-3] + '...'
        return raccourci

def is_like(conn, track_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM playlist WHERE track_id=?", (track_id,))
    rows = cursor.fetchall()
    if len(rows) == 0:
        return False
    else:
        return True

def create_playlist_db(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS playlist
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       track_id TEXT NOT NULL,
                       more TEXT NOT NULL)''')
    conn.commit()
    return conn

def add_track_to_playlist(conn, track_id, more='racine'):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO playlist (track_id, more) VALUES (?,?)", (track_id,more))
    conn.commit()

def delete_track_from_playlist(conn, track_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM playlist WHERE track_id = ?", (track_id,))
    conn.commit()

def ms_to_minutes(millis):
    minutes = millis // 60000
    return minutes
def ms_to_hours(millis):
    hours = millis / 3600000
    return hours
def ms_to_min_sec(millis):
    minutes = millis // 60000
    seconds = (millis // 1000) % 60
    return f"{minutes:02d}:{seconds:02d}"

def is_square_image(file_path):
    # Vérifie si une image a un format carré 1:1
    img = Image.open(file_path)
    return img.size[0] == img.size[1]

def get_image_urls(id):
    img_series = df_cover.loc[df_cover['track_id'] == id, 'image_url']
    if type(img_series.iloc[0]) == str:
        return img_series.iloc[0]
    else:   
        return cover_false

def get_track_name(id):
    getname = df.loc[df['track_id'] == id, 'track_name']
    if type(getname.iloc[0]) == str:
        return getname.iloc[0]
    else:
        return 'Titre introuvable' 

def get_sound_urls(id):
    track_info = df_cover.loc[df_cover['track_id'] == id, 'son_url']
    if type(track_info.iloc[0]) == str:
        st.audio(track_info.iloc[0])
    
def row_5(list_):

    col1, col2, col3, col4 = st.columns([2,5,2,5])
    if len(list_)>0:
        with col1:
            img_urls = get_image_urls(list_[0])
            html_code = f'<a href="{curl+list_[0]}"><img width="80px" src="{img_urls}"></a>'
            st.markdown(html_code, unsafe_allow_html=True)
        with col2:
            st.write("""<span style="font-size:15px; font-weight:bold">""",raccourcir_chaine(get_track_name(list_[0])),"""<span>""", unsafe_allow_html=True)
        
            collike, colson = st.columns([2,8])
            with collike:
                if is_like(db_conn, list_[0]):
                    st.image(heart, width=15)
                else:
                    m = st.markdown("""
                    <style>
                    div.stButton > button:first-child {
                        background: #E02800;
                        border: none;
                        color: white;
                        font-size: 9px;
                        padding: 2px 5px;
                    }
                    div.stButton > button:first-child:hover{
                        border:none;
                        background: #901A00;
                    }
                    </style>""", unsafe_allow_html=True)

                    if st.button("like", key=list_[0]):
                        add_track_to_playlist(db_conn, list_[0])
                        st.write(f"""<img src="{check}" width="15px"> """, unsafe_allow_html=True)
                with colson:
                    get_sound_urls(list_[0])

            if len(list_)>1:
                with col3:
                    img_urls = get_image_urls(list_[1])
                    html_code = f'<a href="{curl+list_[1]}"><img width="80px" src="{img_urls}"></a>'
                    st.markdown(html_code, unsafe_allow_html=True)

                with col4:
                    st.write("""<span style="font-size:15px; font-weight:bold">""",raccourcir_chaine(get_track_name(list_[1])),"""<span>""", unsafe_allow_html=True)
                    collike, colson = st.columns([2,8])
                    with collike:
                        if is_like(db_conn, list_[1]):
                            st.image(heart, width=15)
                        else:
                            m = st.markdown("""
                            <style>
                            div.stButton > button:first-child {
                                background: #E02800;
                                border: none;
                                color: white;
                                font-size: 9px;
                                padding: 2px 5px;
                            }
                            div.stButton > button:first-child:hover{
                                border:none;
                                background: #901A00;
                            }
                            </style>""", unsafe_allow_html=True)

                            if st.button("like", key=list_[1]):
                                add_track_to_playlist(db_conn, list_[1])
                                st.write(f"""<img src="{check}" width="15px"> """, unsafe_allow_html=True)
                    with colson:
                        get_sound_urls(list_[1])
                    
def row_top(list_):

    col1, col2, col3 = st.columns(3)
    if len(list_)>0:
        with col1:
            img_urls = get_image_urls(list_[0])
            html_code = f'<a href="{curl+list_[0]}"><img width="250px" src="{img_urls}"></a>'
            # Affichage du code HTML
            st.markdown(html_code, unsafe_allow_html=True)
            get_sound_urls(list_[0])
            if is_like(db_conn, list_[0]):
                st.image(heart, width=15)
            else:
                m = st.markdown("""
                <style>
                div.stButton > button:first-child {
                    background: #E02800;
                    border: none;
                    color: white;
                    font-size: 9px;
                    padding: 2px 5px;
                }
                div.stButton > button:first-child:hover{
                    border:none;
                    background: #901A00;
                }
                </style>""", unsafe_allow_html=True)

                if st.button("like", key=list_[0]):
                    add_track_to_playlist(db_conn, list_[0])
                    st.write(f"""<img src="{check}" width="15px"> """, unsafe_allow_html=True)
        if len(list_)>1:
            with col2:
                img_urls = get_image_urls(list_[1])
                html_code = f'<a href="{curl+list_[1]}"><img width="250px" src="{img_urls}"></a>'
                # Affichage du code HTML
                st.markdown(html_code, unsafe_allow_html=True)      
                get_sound_urls(list_[1])
                if is_like(db_conn, list_[1]):
                    st.image(heart, width=15)
                else:
                    m = st.markdown("""
                    <style>
                    div.stButton > button:first-child {
                        background: #E02800;
                        border: none;
                        color: white;
                        font-size: 9px;
                        padding: 2px 5px;
                    }
                    div.stButton > button:first-child:hover{
                        border:none;
                        background: #901A00;
                    }
                    </style>""", unsafe_allow_html=True)

                    if st.button("like", key=list_[1]):
                        add_track_to_playlist(db_conn, list_[1])
                        st.write(f"""<img src="{check}" width="15px"> """, unsafe_allow_html=True)
                
            if len(list_)>2:
                with col3:
                    img_urls = get_image_urls(list_[2])
                    html_code = f'<a href="{curl+list_[2]}"><img width="250px" src="{img_urls}"></a>'
                    # Affichage du code HTML
                    st.markdown(html_code, unsafe_allow_html=True)
                    get_sound_urls(list_[2])
                    if is_like(db_conn, list_[2]):
                        st.image(heart, width=15)
                    else:
                        m = st.markdown("""
                        <style>
                        div.stButton > button:first-child {
                            background: #E02800;
                            border: none;
                            color: white;
                            font-size: 9px;
                            padding: 2px 5px;
                        }
                        div.stButton > button:first-child:hover{
                            border:none;
                            background: #901A00;
                        }
                        </style>""", unsafe_allow_html=True)

                        if st.button("like", key=list_[2]):
                            add_track_to_playlist(db_conn, list_[2])
                            st.write(f"""<img src="{check}" width="15px"> """, unsafe_allow_html=True)


# END FONCITON $
add_logo()
db_conn = create_playlist_db("list.bdd")
# INIT DB et BDD
db_conn = create_playlist_db("list.bdd")
df = pd.read_csv('DataFrame_Musique.csv')
df_cover = pd.read_csv('df_img.csv')
df_sound = pd.read_csv('df_sound.csv')


# DEFINITION DES VAR
genres_uniques = df["genre"].explode().unique()
artistes_uniques = df["artist_name"].explode().unique()
titre_musiques = df["track_name"].explode().unique()
duree_max  = ms_to_minutes(math.ceil(df["duration_ms"].max()))
duree_min  = ms_to_minutes(math.floor(df["duration_ms"].min()))

col0, col01 = st.columns(2)
with col0:
    f_genre = st.multiselect('GENRES',genres_uniques, max_selections=5)
with col01:
    f_artiste = st.multiselect('ARTISTE',artistes_uniques, max_selections=5)

col1, col2, col3 = st.columns(3)
with col1:
    f_r = st.slider('Durée écoute en heure', 1, 72, 8)
with col2:
    f_bpm = st.slider('BPM',30, 300, (100, 200)) # bpm == tempo
with col3:
    name_play = st.text_input('nom de la playlist')

col4, col5 = st.columns([4,1])
    
with col5:
    # slide one point sur popularity
    btn_genre = st.button('Créer la playlist')

c = db_conn.cursor()
c.execute('SELECT DISTINCT more FROM playlist')
resultats = c.fetchall()
liste_more_exist = [row[0] for row in resultats]

if btn_genre:
    if name_play != '':
        name_play = name_play.strip()
        if name_play not in liste_more_exist:
            
            # Filtrer le dataframe pour cette plage de durée
            filtered_df = df[df['duration_ms'].between(duree_min * 60 * 1000, duree_max * 60 * 1000)]
            
            # Appliquer le filtre par genre, si des genres ont été sélectionnés
            if f_genre:
                selected_genres = f_genre
                filtered_df = filtered_df[filtered_df["genre"].isin(selected_genres)]
            if f_artiste:
                selected_artist = f_artiste
                filtered_df = filtered_df[filtered_df["artist_name"].isin(selected_genres)]
            if f_bpm :
                bpm_min, bpm_max = f_bpm
                filtered_df = filtered_df[df['tempo'].between(bpm_min, bpm_max)].sort_values('popularity', ascending = False)

            #ms_to_hours()
            filtered_df = filtered_df.head(1800) # on part du priincipe que la durée moyenne est respecter env 4 min
            tracks_floor_chunk_knn = [filtered_df[i:i] for i in range(0, len(filtered_df), 2)]
            max_time = f_r
            cpt_time = 0
            liste = []
            st.write('Ta playlist dispo sur la page "Playlist"')

            for ligneMusic in range(len(filtered_df)):
                duree_h = ms_to_hours(int(filtered_df['duration_ms'].iloc[ligneMusic]))
                cpt_time += duree_h
                if cpt_time < max_time: # si on est encore en dessous du temps playlist users
                    liste.append(filtered_df['track_id'].iloc[ligneMusic])
                    col1, col2 = st.columns([3,7])
                    with col1:
                        st.image(get_image_urls(filtered_df['track_id'].iloc[ligneMusic]), width=100)
                    with col2:
                        get_sound_urls(filtered_df['track_id'].iloc[ligneMusic])
                    add_track_to_playlist(db_conn,filtered_df['track_id'].iloc[ligneMusic], more = name_play)
        else:
            st.write('La playlist existe déja')
    else:
        st.write('Tu dois mettre un nom pour ta playlist , c\'est obligatore.')