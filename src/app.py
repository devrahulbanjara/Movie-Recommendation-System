import pickle
import pandas as pd
import streamlit as st
import requests

# Load the movie dictionary and similarity matrix
movies_dict = pickle.load(open("models/movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('models/similarity.pkl', "rb"))

API_KEY = "f5a4009af4994c388e02867e59197cd2"
BASE_URL = "https://api.themoviedb.org/3/movie"

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    top_5 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []
    for i in top_5:
        recommend_movies.append(movies.iloc[i[0]])
    return recommend_movies

def get_movie_poster(movie_id):
    response = requests.get(f"{BASE_URL}/{movie_id}?api_key={API_KEY}&language=en-US")
    data = response.json()
    return f"https://image.tmdb.org/t/p/w500{data['poster_path']}" if 'poster_path' in data else None

# Streamlit UI
st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬", layout="wide")
st.title("Movie Recommendation System")
st.write("Enter a movie name to get similar movie recommendations:")

movie_name = st.text_input("Movie Name:", placeholder="e.g., Inception")

if st.button("Recommend"):
    if movie_name:
        try:
            recommended_movies = recommend(movie_name)
            st.subheader("Recommended Movies:")
            cols = st.columns(5)  # Create columns for the posters
            for i, movie in enumerate(recommended_movies):
                with cols[i % 5]:  # Display in columns
                    st.image(get_movie_poster(movie.id), width=150)
                    st.write(movie.title)
        except IndexError:
            st.error("Movie not found. Please check the name and try again.")
    else:
        st.warning("Please enter a movie name.")

st.markdown("""
    <style>
    .stButton > button {
        background-color: #1f77b4;
        color: white;
        font-size: 16px;
        border: None;
        border-radius: 5px;
        padding: 10px;
        transition: background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #0e5a9c;
    }
    </style>
""", unsafe_allow_html=True)
