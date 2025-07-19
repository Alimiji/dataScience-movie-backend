# %%
from database import SessionLocal
from query_helper import *

# Créer une session
db = SessionLocal()

# %%
# Tester la récupération de films
movies = get_movies(db, limit=5, genre="Comedy")

for movie in movies:
    print(f"ID: {movie.movieId}, Titre: {movie.title}, Genres: {movie.genres}")


# Test sur la récupération des ratings

print("Affichage des 50 premiers ratings supérieure ou égale à 3")

ratings = get_ratings(db, limit = 50, min_rating = 3)

    # Affichage des ratings récupérés

for rate in ratings:
    print(f"User ID:  {rate.userId}  Movie ID: {rate.movieId} Rating : {rate.rating}") 

# %%
# Fermer la session
db.close()