import streamlit as st
import pickle
import requests

import urllib.parse
import requests

import os
OMDB_API_KEY = os.getenv("1a40d5dc", "")


def fetch_poster(title):
    api_key = "1a40d5dc"  # put your real OMDb API key here
    query = urllib.parse.quote(title)
    url = f"http://www.omdbapi.com/?t={query}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    print(f"[DEBUG] Fetching poster for: {title}")
    print(f"[DEBUG] OMDb response: {data}")

    if data.get("Response") == "True" and data.get("Poster") != "N/A":
        return data.get("Poster")
    else:
        return "https://via.placeholder.com/300x450.png?text=No+Poster+Found"


# Recommender function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_title = movies.iloc[i[0]].title
        recommended_movies.append(movie_title)
        recommended_posters.append(fetch_poster(movie_title))
    return recommended_movies, recommended_posters


# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI
st.title("🎬 Movie Recommender System")

selected_movie_name = st.selectbox("Select your movie", movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.image(posters[idx], width="stretch")   # ✅ updated
            st.text(names[idx])
