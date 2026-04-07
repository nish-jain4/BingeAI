import streamlit as st
import pandas as pd
import requests
import pickle
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Load the processed data and similarity matrix
with open('movie_recommender.pkl', 'rb') as file:
    df_2, cosine_sim = pickle.load(file)


@st.cache_resource
def get_tmdb_session():
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session

# Function to get movie recommendations
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = df_2[df_2['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Get top 10 similar movies
    movie_indices = [i[0] for i in sim_scores]
    return df_2[['title', 'movie_id']].iloc[movie_indices]

# Fetch movie poster from TMDB API
def fetch_poster(movie_id):
    movie_id = int(movie_id)
    if 'poster_cache' not in st.session_state:
        st.session_state.poster_cache = {}

    if movie_id in st.session_state.poster_cache:
        return st.session_state.poster_cache[movie_id]

    api_key = 'c9a558e8f68f674d06c4803aa9bb8066'  # Replace with your TMDB API key
    url = f'https://api.themoviedb.org/3/movie/{movie_id}'
    try:
        response = get_tmdb_session().get(url, params={"api_key": api_key}, timeout=10)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
            st.session_state.poster_cache[movie_id] = poster_url
            return poster_url
    except requests.RequestException:
        return None
    return None

# Streamlit UI
st.title("Movie Recommendation System")

selected_movie = st.selectbox("Select a movie:", df_2['title'].values)

if st.button('Recommend'):
    recommendations = get_recommendations(selected_movie)
    st.write("Top 10 recommended movies:")

    # Create a 2x5 grid layout
    for i in range(0, 10, 5):  # Loop over rows (2 rows, 5 movies each)
        cols = st.columns(5)  # Create 5 columns for each row
        for col, j in zip(cols, range(i, i+5)):
            if j < len(recommendations):
                movie_title = recommendations.iloc[j]['title']
                movie_id = recommendations.iloc[j]['movie_id']
                poster_url = fetch_poster(movie_id)
                with col:
                    if poster_url:
                        st.image(poster_url, width=130)
                    else:
                        st.caption("Poster unavailable")
                    st.write(movie_title)
