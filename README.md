# reconverSon

Vainqueur Technique Hackaton Wild 2023

- 24h pour penser une problématique et réaliser un projet.
- Théme "Musique"

## La problématique 

Une radio locale souhaite une application pour generer des playlists en fonction des genres et des similarités de titre.

## Notre solution

Nous allons fournir à notre client fictif une solution de recommandation basé sur Streamlit.
- Affichage des musiques en fonction des genres, bpm, time.
- Affichage de recommandation en fonction d'une musique
- Possibilité de créer des playlists (stocké avec Sqlite3)
- Possibilité de like/unlike des musiques
- Générer des playlists en fonction des genres , artistes, durée, bpm
- Possibilté d'écouter un extrait audio
- Exporter la playlist au format JSON


## Amélioration possible
- Ajouter un bdd users pour capter les preferences d'écoute des auditeurs
- Faire evoluer l'algo de recommandation avec l'aspect collaboratif des nouvelles données
- Utiliser un flux direct avec l'API spotify en remplacement d'un dataSet en CSV.
- Concevoir une API pour un accés direct du client à leurs données ( playlist) depuis leur plateforme de diffusion
